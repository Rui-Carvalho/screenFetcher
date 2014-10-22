### To generate the exe file do the following:

From:
C:\Python33\Scripts>

Run:
cxfreeze C:\Users\RuiCarvalho\Desktop\PythonProjs\ScreenFetcher\__releases__\v1.0\source\screen_fetcher.py --base-name=Win32GUI --target-dir C:\Users\RuiCarvalho\Desktop\PythonProjs\ScreenFetcher\__releases__\v1.0\dist --icon=C:\Users\RuiCarvalho\Desktop\PythonProjs\ScreenFetcher\__releases__\v1.0\source\screenFetcher.ico

### Alternative (See: http://blog.notfaqs.com/2011/09/python-32-create-executable-with.html):

Create and run the file "setup.py":

from cx_Freeze import setup, Executable

executables = [
    Executable("screen_fetcher.py",
               icon="screenFetcher.ico",
               appendScriptToExe=True,
               appendScriptToLibrary=False,
               )
]

buildOptions = dict(create_shared_zip=False)

setup(name="ScreenFetcher",
      version="1.0",
      description="Screen Fetcher Program",
      options=dict(build_exe=buildOptions),
      executables=executables,
      )

### Notes on msi Generation => Full Installation on Windows

The msi should copy the following files as well to the destination folder of installation:
* README.md
* CCPL.txt
* create folder: snapshots
* create startup folder
* create desktop shortcut => shortcut for exe