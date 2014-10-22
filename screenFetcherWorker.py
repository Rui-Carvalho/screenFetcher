import win32gui
import win32con
from PIL import ImageGrab
import time

class screenFetcherWorker():
    def __init__(self):
        self.imageCounter             = 0
        self.titleOfWindowToFetch     = ""
        self.iniForegroundWindowTitle = win32gui.GetWindowText(win32gui.GetForegroundWindow())

    def setTitleOfWindowToFetch(self, title):
        self.titleOfWindowToFetch = title
        
    def PrintTopWindow(self, hwnd):
        # ----- Prints the title of the top window -----
        print(hwnd)

    def MinimizeTopWindow(self):
        # ----- Minimizes the top windows -----
        win32gui.ShowWindow(win32gui.GetForegroundWindow(), win32con.SW_MINIMIZE)

    def RestoreWin(self, hwnd):
        # ----- Restores (or Maximizes) the previously minimized top windows -----
        ClassName = None
        WindowName = self.iniForegroundWindowTitle
        win32gui.ShowWindow(win32gui.FindWindow(ClassName, WindowName ), win32con.SW_RESTORE)

    def MaximizeFGWin(self, WindowName):
        # ----- Restores (or Maximizes) the previously minimized top windows -----
        ClassName = None
        win32gui.ShowWindow(win32gui.FindWindow(ClassName, WindowName ), win32con.SW_MAXIMIZE)

    def CloseFGWin(self):
        window_handle = win32gui.GetWindowText(win32gui.GetForegroundWindow())
        win32gui.PostMessage(window_handle, WM_CLOSE,0,0)

    def snapshotFGWin(self, img_name="", window_title=""):
        ClassName=None
        if window_title=="":
            window_title = self.titleOfWindowToFetch
        hwnd = win32gui.FindWindow(ClassName, window_title)
        if hwnd==0:
            print("\n  ERROR: Window for the program not found!")
            self.RestoreWin(self.iniForegroundWindowTitle)
            exit()
        self.RestoreWin(hwnd)
        win32gui.SetForegroundWindow(hwnd)
        time.sleep(1)
        #win32gui.ShowWindow(hwnd, win32con.SW_RESTORE)
        bbox = win32gui.GetWindowRect(hwnd)
        img = ImageGrab.grab(bbox)
        if img_name=="":
            img_name = "snapshots/screen_" + str(self.imageCounter) + ".jpg"
            self.imageCounter += 1
        img.save(img_name, quality="web_high")

    def sendKeysToActiveWin(self, keys):
        # Example: %{TAB} ==> ALT + TAB
        import win32com.client
        shell = win32com.client.Dispatch("WScript.Shell")
        shell.SendKeys(keys)

''' ----- Example of Usage -----
sfw = screenFetcherWorker()
sfw.setTitleOfWindowToFetch("Skillsoft Course Player - Google Chrome")
sfw.MinimizeTopWindow()
sfw.snapshotFGWin()
'''