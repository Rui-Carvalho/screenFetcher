readme.md for *designer*
========================

The **screen_fetcher.ui** is the file generated by the **qt-designer**.

To see how it was generated, open screen_fetcher.ui with the qt-designer. 

It needs to be converted to a python readable file with the pyside tool: **pyside-uic**

We choose a name for the output file which indicates that it is

* a python file, so it has an extension py
* a user interface data file, so it has a prefix ui_

Thus, the command is:

> C:\Python33\Scripts\pyside-uic screen_fetcher.ui -o ui_screen_fetcher.py

NOTE: you will probably find pyside-uic in: C:\Python33\Scripts\pyside-uic.exe

The file resulting file **ui_screen_fetcher.py** should then be copied to the master directory.