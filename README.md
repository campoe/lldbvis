# lldbvis

Lldbvis is a debug visualizer. It is made for lldb, but can be extended in the future to also be used with gdb or other debuggers. It has only be tested on C++ programs, but should support any language that is supported by lldb.

## Installation

Because lldb is only supported for Python 2, lldbvis has also be built on Python 2. Therefore you require Python 2 (can be installed [here](https://www.python.org/download/releases/2.7/)) before you can install lldbvis.

To be able to run lldbvis you are required to install lldb. There is an instruction manual on how to build the sources over [here](https://lldb.llvm.org/source.html). You can also install lldb directly from the command line using:

* On Ubuntu:
`
sudo apt-get install lldb
`

* On Arch (requires e.g. yaourt):
`
yaourt -S lldb
`
Next, you need to install all the requirements of lldbvis. This is as easy as running:

```bash
pip install -r requirements.txt
```

There is one requirement that can't be installed using pip though. Lldbvis uses Qt4, as PyQt5 is not supported for Python 2, hence PyQt4 needs to be installed. PyQt4 can only be downloaded from the [PyQt4 download page](http://www.riverbankcomputing.com/software/pyqt/download). Note that in order to build PyQt4, you also need to install SIP from the [SIP download page](http://www.riverbankcomputing.com/software/sip/download).

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install lldbvis in the following way:

```bash
pip install lldbvis
```

When using multiple Python versions, make sure you can differentiate the pip installments. Usually the following command makes use of Python 2's pip:

```bash
pip2 install lldbvis
```

## Usage

You can now easily run lldbvis as a GUI desktop program by running the following from a shell:

```bash
lldbvis
```
## License
[MIT](https://github.com/campoe/lldbvis/blob/master/LICENSE)
