# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'screen_fetcher.ui'
#
# Created: Thu Mar  6 01:14:08 2014
#      by: pyside-uic 0.2.15 running on PySide 1.2.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(731, 475)
        self.centralwidget = QtGui.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout.setObjectName("gridLayout")
        self.textEdit = QtGui.QTextEdit(self.centralwidget)
        self.textEdit.setObjectName("textEdit")
        self.gridLayout.addWidget(self.textEdit, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 731, 21))
        self.menubar.setObjectName("menubar")
        self.menu_File = QtGui.QMenu(self.menubar)
        self.menu_File.setObjectName("menu_File")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.action_Show_CCPL = QtGui.QAction(MainWindow)
        self.action_Show_CCPL.setObjectName("action_Show_CCPL")
        self.action_About = QtGui.QAction(MainWindow)
        self.action_About.setObjectName("action_About")
        self.action_Close = QtGui.QAction(MainWindow)
        self.action_Close.setCheckable(False)
        self.action_Close.setObjectName("action_Close")
        self.action_Snapshot = QtGui.QAction(MainWindow)
        self.action_Snapshot.setObjectName("action_Snapshot")
        self.menu_File.addAction(self.action_Show_CCPL)
        self.menu_File.addAction(self.action_About)
        self.menu_File.addAction(self.action_Close)
        self.menubar.addAction(self.menu_File.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QObject.connect(self.action_Close, QtCore.SIGNAL("triggered()"), MainWindow.close)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "ScreenFetcher", None, QtGui.QApplication.UnicodeUTF8))
        self.menu_File.setTitle(QtGui.QApplication.translate("MainWindow", "&File", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Show_CCPL.setText(QtGui.QApplication.translate("MainWindow", "Show &CCPL", None, QtGui.QApplication.UnicodeUTF8))
        self.action_About.setText(QtGui.QApplication.translate("MainWindow", "&About", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Close.setText(QtGui.QApplication.translate("MainWindow", "Close   &X", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Snapshot.setText(QtGui.QApplication.translate("MainWindow", "&Snapshot", None, QtGui.QApplication.UnicodeUTF8))
        self.action_Snapshot.setToolTip(QtGui.QApplication.translate("MainWindow", "New Snapshot", None, QtGui.QApplication.UnicodeUTF8))

