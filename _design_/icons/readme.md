readme.md for **icons**
==========================

The **screen_fetcher.qrc** is a Resource Source File to be compiled and it is prepared with a plain text editor.
It's a XML file easily written following the extant pattern.

Inspection of the file reveals the replacement of the path to the icon (eg.: "images/32x32/actions/system-log-out.png")
by a much simpler token (eg.: alias="quit.png"). 
Applications refer to icons by that token. For the format, find the token name in the code.

In a similar way to the file in **qt-designer**, the XML file needs to be converted to a python readable file, 
with a pyside compiler **pyside-rcc**:

* **pyside-rcc [options] screen_fetcher.qrc -o <output file>**

NOTE: you will probably find pyside-rcc in: C:\Python33\Lib\site-packages\PySide\pyside-rcc.exe

NOTE: usually you will want something like: <output file> = "qrc_screen_fetcher.py"

One of the options is to produce the <output file> for python3; the default is python2.
The switch for python3  is **-py3**, so that the above command for python3 becomes:

* **C:\Python33\Lib\site-packages\PySide\pyside-rcc -py3 screen_fetcher.qrc -o qrc_screen_fetcher.py**

We choose a name for the output file which indicates that it is:
* a python file, so it has an extension py
* a user interface data file, so it has a prefix qrc_
* main part of the name is **screen_fetcher**, which identifies the project.
* indication of python version - 2 for python 2.x, 3 for python 3.x

**qrc_screen_fetcher.py** should then be copied to other directories as required.


