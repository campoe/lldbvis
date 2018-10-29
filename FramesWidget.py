from PyQt4.QtGui import *
from Debugger import Debugger
from Observer import Observer
from PyQt4.QtCore import Qt
from lldb import *


class FramesWidget(QWidget):
    def __init__(self, *args):
        QWidget.__init__(self, *args)
        self.debugger = Debugger()

        self.setLayout(QVBoxLayout())

        self.threadCombo = QComboBox()
        self.layout().addWidget(self.threadCombo)

        self.frameList = QListWidget()
        self.frameList.setSelectionMode(QAbstractItemView.SingleSelection)
        self.layout().addWidget(self.frameList)

        self.setEnabled(False)

        Observer().add(self.debugger, 'pause', self.updateWidget)
        Observer().add(self.debugger, 'setup', self.enable)
        Observer().add(self.debugger, 'end', self.disable)

    def disable(self, *args, **kwargs):
        self.setEnabled(False)
        self.threadCombo.clear()
        self.frameList.clear()

    def enable(self, *args, **kwargs):
        self.setEnabled(True)

    def updateWidget(self, *args, **kwargs):
        self.updateThreadCombo()
        self.updateFrameList()

    @property
    def threadFrames(self):
        res = {}
        for thread in self.debugger.threads():
            res[thread.GetName()] = self.debugger.frames(thread)
        return res

    def updateThreadCombo(self):
        self.threadCombo.clear()
        for k, v in self.threadFrames.items():
            self.threadCombo.addItem(k)

    def changeThread(self, i):
        thread_name = self.threadCombo.itemText(i)
        self.updateFrameList(thread_name)

    def updateFrameList(self, thread_name=None):
        self.frameList.clear()
        if thread_name is None:
            cur_thread = self.debugger.process.GetSelectedThread()
            frames = self.threadFrames.get(cur_thread.GetName())
            cur_frame = cur_thread.GetSelectedFrame()
        else:
            frames = self.threadFrames.get(thread_name)
            cur_frame = frames[0]
        if frames is not None:
            for frame in frames:
                frame_name = frame.GetDisplayFunctionName()
                line_entry = frame.GetLineEntry()
                file_name = line_entry.GetFileSpec().GetFilename()
                line = line_entry.GetLine()
                if file_name is None:
                    self.frameList.addItem(str(frame_name))
                else:
                    self.frameList.addItem(str(frame_name) + ', ' + str(file_name) + ':' + str(line))
            self.frameList.currentItemChanged.connect(self.changeFrame)
            cur_item = self.frameList.findItems(cur_frame.GetDisplayFunctionName(), Qt.MatchStartsWith)[0]
            self.frameList.setCurrentItem(cur_item)

    def changeFrame(self, newItem, oldItem):
        pass
