#!/usr/bin/env python
# screen_fetcher.py - Fetches the screen as images taken as snapshots on click demand.

import sys
import platform
import PySide
from PySide.QtGui import QApplication, QMainWindow, QTextEdit, QPushButton, \
                         QMessageBox, QIcon
__version__ = '0.1'
from ui_screen_fetcher import Ui_MainWindow
import qrc_screen_fetcher
from screenFetcherWorker import screenFetcherWorker

#------------------------------------------------------------------------------
# We define the Main Window of the program as a specialization of 2 MainWindow objects already defined.
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        self.action_Show_CCPL.triggered.connect(self.showGPL)
        self.action_About.triggered.connect(self.about)
        self.action_Snapshot.triggered.connect(self.takeSnap)
        iconToolBar = self.addToolBar("iconBar.png")
        #------------------------------------------------------
        # Add icons to appear in tool bar - step 1 => Icon images are added to the actions.
        self.action_Show_CCPL.setIcon(QIcon(":/showlicense.png"))
        self.action_About.setIcon(QIcon(":/about.png"))
        self.action_Close.setIcon(QIcon(":/quit.png"))
        self.action_Snapshot.setIcon(QIcon(":/takeSnapshot.png"))
        #------------------------------------------------------
        # Show a tip on the Status Bar - step 2 => The hint texts are added to the program.
        self.action_Show_CCPL.setStatusTip("Show CCPL Licence")
        self.action_About.setStatusTip("Pop up the About dialog")
        self.action_Close.setStatusTip("Close the program")
        self.action_Snapshot.setStatusTip("Take new snapshot")
        #------------------------------------------------------        
        # Here We actually add the icons to the toolbar => establishes their order!
        iconToolBar.addAction(self.action_Snapshot)
        iconToolBar.addAction(self.action_Show_CCPL)
        iconToolBar.addAction(self.action_About)
        iconToolBar.addAction(self.action_Close)
        
        # Let's init the screen fetcher worker that will process the screen capture
        self.sfw = screenFetcherWorker()
        self.sfw.setTitleOfWindowToFetch("Skillsoft Course Player - Google Chrome")

    def showGPL(self):
        '''Read and display CCPL licence.'''
        self.textEdit.setText(open('CCPL.txt').read())

    def about(self):
        '''Popup a box with about message.'''
        QMessageBox.about(self, "About ScreenFetcher",
            """<b> About this program </b>
               <p>version %s
               <p>Copyright &copy; 2014 Rui Carvalho.
                  All rights reserved in accordance with CCPL - NO WARRANTIES!
               <p>ScreenFetcher allows you to save screen snapshots to 
                  files, on demand, by using a simple app interface.
               <p>Python %s -  PySide version %s - Qt version %s on %s
            """ %
               ( __version__, platform.python_version(), PySide.__version__,
                 PySide.QtCore.__version__, platform.system())
            )

    def takeSnap(self):
        self.sfw.MinimizeTopWindow()
        self.sfw.snapshotFGWin()
        #QMessageBox.about( self, "Take Snapshot", """<b>Take NEW Snapshot""" )


#------------------------------------------------------------------------------
if __name__ == '__main__':
    app = QApplication(sys.argv)
    frame = MainWindow()
    frame.show()
    app.exec_()