

#Notepad.setWindowState(Qt.WindowMaximized)
#python HLPL_writer.py

from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtPrintSupport import *
from PyQt5 import QtCore, QtGui, QtWidgets

from matplotlib.backends.backend_qt4agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.backends.backend_qt4agg import NavigationToolbar2QT as NavigationToolbar
from matplotlib.figure import Figure

import os
import sys

rrm=int()
ar=list('أبجدهوزحطيكلمنسعفصقرشتثخذضظغءاةإآؤىئ')
en=list('abcdefghijklmnopqrstuvwxyz')
from hlpl_composer.hlpl_license_about import *
from hlpl_composer.hlpl_functions import *
from hlpl_composer.hlpl_conjugate import *
import hlpl_composer.static as sfd
import hlpl_composer.images as sfd2
import hlpl_composer as sfd3

import webbrowser


def hlpl_get_name(st):
    if '\\' in st:
       return st.split('\\')[len(st.split('\\'))-1]   
    if '/' in st:
       return st.split('/')[len(st.split('/'))-1]   
    if '\/' in st:
       return st.split('\/')[len(st.split('\/'))-1] 




class Ui_Notepad(object):
    def setupUi(self, Notepad):
        Notepad.setObjectName("Notepad")
        Notepad.setWindowModality(QtCore.Qt.ApplicationModal)
        #Notepad.setWindowState(Qt.WindowMaximized)
        Notepad.setCursor(QtGui.QCursor(QtCore.Qt.ArrowCursor))
       
        
        Notepad.setLayoutDirection(QtCore.Qt.RightToLeft)
        Notepad.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        Notepad.setIconSize(QtCore.QSize(24, 24))
        self.centralWidget = QtWidgets.QWidget(Notepad)
        self.centralWidget.setCursor(QtGui.QCursor(QtCore.Qt.PointingHandCursor))
        self.centralWidget.setObjectName("centralWidget")
        self.verticalLayout_12 = QtWidgets.QVBoxLayout(self.centralWidget)
        self.verticalLayout_12.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_12.setSpacing(6)
        self.verticalLayout_12.setObjectName("verticalLayout_12")
        self.frame = QtWidgets.QFrame(self.centralWidget)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout.setSpacing(1)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.splitter_3 = QtWidgets.QSplitter(self.frame)
        self.splitter_3.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_3.setObjectName("splitter_3")
        self.splitter_2 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_2.setOrientation(QtCore.Qt.Vertical)
        self.splitter_2.setObjectName("splitter_2")
        self.splitter = QtWidgets.QSplitter(self.splitter_2)
        self.splitter.setOrientation(QtCore.Qt.Horizontal)
        self.splitter.setObjectName("splitter")
        self.layoutWidget = QtWidgets.QWidget(self.splitter)
        self.layoutWidget.setObjectName("layoutWidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.layoutWidget)
        self.verticalLayout.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout.setSpacing(6)
        self.verticalLayout.setObjectName("verticalLayout")
        self.horizontalLayout_10 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_10.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_10.setSpacing(6)
        self.horizontalLayout_10.setObjectName("horizontalLayout_10")
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_10.addItem(spacerItem)
        self.pushButton_30 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_30.setMaximumSize(QtCore.QSize(21, 21))
        self.pushButton_30.setText("")
        icon1 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"new.png")
        icon1.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_30.setIcon(icon1)
        self.pushButton_30.setObjectName("pushButton_30")
        self.horizontalLayout_10.addWidget(self.pushButton_30)
        self.pushButton_32 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_32.setMaximumSize(QtCore.QSize(21, 21))
        self.pushButton_32.setText("")
        icon2 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"open.png")
        icon2.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_32.setIcon(icon2)
        self.pushButton_32.setObjectName("pushButton_32")
        self.horizontalLayout_10.addWidget(self.pushButton_32)
        self.pushButton_31 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_31.setMaximumSize(QtCore.QSize(21, 21))
        self.pushButton_31.setText("")
        icon3 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"save.png")
        icon3.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_31.setIcon(icon3)
        self.pushButton_31.setObjectName("pushButton_31")
        self.horizontalLayout_10.addWidget(self.pushButton_31)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        self.pushButton_2.setMaximumSize(QtCore.QSize(21, 21))
        self.pushButton_2.setText("")
        icon4 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"disk--pencil.png")
        icon4.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_2.setIcon(icon4)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout_10.addWidget(self.pushButton_2)
        self.comboBox_8 = QtWidgets.QComboBox(self.layoutWidget)
        self.comboBox_8.setMinimumSize(QtCore.QSize(35, 0))
        self.comboBox_8.setMaximumSize(QtCore.QSize(35, 19))
        self.comboBox_8.setStyleSheet("color: rgb(255, 0, 127)")
        self.comboBox_8.setObjectName("comboBox_8")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.comboBox_8.addItem("")
        self.horizontalLayout_10.addWidget(self.comboBox_8)
        self.fontComboBox = QtWidgets.QFontComboBox(self.layoutWidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fontComboBox.sizePolicy().hasHeightForWidth())
        self.fontComboBox.setSizePolicy(sizePolicy)
        self.fontComboBox.setMinimumSize(QtCore.QSize(101, 0))
        self.fontComboBox.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fontComboBox.setAutoFillBackground(False)
        self.fontComboBox.setStyleSheet("color: rgb(0, 0, 127);")
        self.fontComboBox.setSizeAdjustPolicy(QtWidgets.QComboBox.AdjustToContents)
        self.fontComboBox.setWritingSystem(QtGui.QFontDatabase.Any)
        self.fontComboBox.setObjectName("fontComboBox")
        self.horizontalLayout_10.addWidget(self.fontComboBox)
        self.verticalLayout.addLayout(self.horizontalLayout_10)
        self.textEdit = QtWidgets.QTextEdit(self.layoutWidget)
        self.textEdit.setObjectName("textEdit")
        self.verticalLayout.addWidget(self.textEdit)
        self.layoutWidget1 = QtWidgets.QWidget(self.splitter)
        self.layoutWidget1.setObjectName("layoutWidget1")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.layoutWidget1)
        self.verticalLayout_2.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_2.setSpacing(6)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.horizontalLayout_7 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_7.setSpacing(6)
        self.horizontalLayout_7.setObjectName("horizontalLayout_7")
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_7.addItem(spacerItem1)
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton.setMaximumSize(QtCore.QSize(21, 21))
        self.pushButton.setText("")
        self.pushButton.setIcon(icon4)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_7.addWidget(self.pushButton)
        self.comboBox_7 = QtWidgets.QComboBox(self.layoutWidget1)
        self.comboBox_7.setMinimumSize(QtCore.QSize(35, 0))
        self.comboBox_7.setMaximumSize(QtCore.QSize(40, 19))
        self.comboBox_7.setStyleSheet("color: rgb(170, 0, 0);")
        self.comboBox_7.setObjectName("comboBox_7")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.comboBox_7.addItem("")
        self.horizontalLayout_7.addWidget(self.comboBox_7)
        self.fontComboBox_2 = QtWidgets.QFontComboBox(self.layoutWidget1)
        self.fontComboBox_2.setMinimumSize(QtCore.QSize(101, 0))
        self.fontComboBox_2.setMaximumSize(QtCore.QSize(200, 16777215))
        self.fontComboBox_2.setStyleSheet("color: rgb(255, 85, 0);")
        self.fontComboBox_2.setWritingSystem(QtGui.QFontDatabase.Any)
        self.fontComboBox_2.setObjectName("fontComboBox_2")
        self.horizontalLayout_7.addWidget(self.fontComboBox_2)
        self.pushButton_18 = QtWidgets.QPushButton(self.layoutWidget1)
        self.pushButton_18.setMaximumSize(QtCore.QSize(55, 16777215))
        self.pushButton_18.setStyleSheet("color: rgb(0, 85, 0)")
        self.pushButton_18.setObjectName("pushButton_18")
        self.horizontalLayout_7.addWidget(self.pushButton_18)
        self.verticalLayout_2.addLayout(self.horizontalLayout_7)
        self.textEdit_2 = QtWidgets.QTextEdit(self.layoutWidget1)
        self.textEdit_2.setReadOnly(True)
        self.textEdit_2.setObjectName("textEdit_2")
        self.verticalLayout_2.addWidget(self.textEdit_2)
        self.textEdit_5 = QtWidgets.QTextEdit(self.splitter_2)
        self.textEdit_5.setMinimumSize(QtCore.QSize(0, 44))
        self.textEdit_5.setMaximumSize(QtCore.QSize(16777215, 88))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.textEdit_5.setFont(font)
        self.textEdit_5.setReadOnly(True)
        self.textEdit_5.setObjectName("textEdit_5")
        self.splitter_7 = QtWidgets.QSplitter(self.splitter_3)
        self.splitter_7.setOrientation(QtCore.Qt.Vertical)
        self.splitter_7.setObjectName("splitter_7")
        self.textEdit_9 = QtWidgets.QTextEdit(self.splitter_7)
        self.textEdit_9.setReadOnly(True)
        self.textEdit_9.setObjectName("textEdit_9")
        self.textEdit_11 = QtWidgets.QTextEdit(self.splitter_7)
        self.textEdit_11.setReadOnly(True)
        self.textEdit_11.setObjectName("textEdit_11")
        self.horizontalLayout.addWidget(self.splitter_3)
        self.verticalLayout_12.addWidget(self.frame)
        self.frame_2 = QtWidgets.QFrame(self.centralWidget)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_5 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_5.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_5.setSpacing(6)
        self.horizontalLayout_5.setObjectName("horizontalLayout_5")
        self.splitter_6 = QtWidgets.QSplitter(self.frame_2)
        self.splitter_6.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_6.setObjectName("splitter_6")
        self.layoutWidget2 = QtWidgets.QWidget(self.splitter_6)
        self.layoutWidget2.setObjectName("layoutWidget2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout(self.layoutWidget2)
        self.verticalLayout_7.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_7.setSpacing(6)
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.splitter_5 = QtWidgets.QSplitter(self.layoutWidget2)
        self.splitter_5.setOrientation(QtCore.Qt.Vertical)
        self.splitter_5.setObjectName("splitter_5")
        self.splitter_4 = QtWidgets.QSplitter(self.splitter_5)
        self.splitter_4.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_4.setObjectName("splitter_4")
        self.layoutWidget_3 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget_3.setObjectName("layoutWidget_3")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.layoutWidget_3)
        self.verticalLayout_4.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_4.setSpacing(6)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.horizontalLayout_8 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_8.setSpacing(6)
        self.horizontalLayout_8.setObjectName("horizontalLayout_8")
        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_8.addItem(spacerItem2)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget_3)
        self.pushButton_4.setMaximumSize(QtCore.QSize(21, 21))
        self.pushButton_4.setText("")
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout_8.addWidget(self.pushButton_4)
        self.comboBox = QtWidgets.QComboBox(self.layoutWidget_3)
        self.comboBox.setMinimumSize(QtCore.QSize(35, 0))
        self.comboBox.setMaximumSize(QtCore.QSize(35, 16777215))
        self.comboBox.setStyleSheet("color: rgb(255, 0, 127)")
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.horizontalLayout_8.addWidget(self.comboBox)
        self.fontComboBox_3 = QtWidgets.QFontComboBox(self.layoutWidget_3)
        self.fontComboBox_3.setMinimumSize(QtCore.QSize(101, 0))
        self.fontComboBox_3.setStyleSheet("color: rgb(0, 0, 127);")
        self.fontComboBox_3.setObjectName("fontComboBox_3")
        self.horizontalLayout_8.addWidget(self.fontComboBox_3)
        self.verticalLayout_4.addLayout(self.horizontalLayout_8)
        self.textEdit_4 = QtWidgets.QTextEdit(self.layoutWidget_3)
        self.textEdit_4.setReadOnly(True)
        self.textEdit_4.setObjectName("textEdit_4")
        self.verticalLayout_4.addWidget(self.textEdit_4)
        self.layoutWidget_2 = QtWidgets.QWidget(self.splitter_4)
        self.layoutWidget_2.setObjectName("layoutWidget_2")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.layoutWidget_2)
        self.verticalLayout_3.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_3.setSpacing(6)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.horizontalLayout_11 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_11.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_11.setSpacing(6)
        self.horizontalLayout_11.setObjectName("horizontalLayout_11")
        spacerItem3 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_11.addItem(spacerItem3)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_3.setMaximumSize(QtCore.QSize(21, 21))
        self.pushButton_3.setText("")
        self.pushButton_3.setIcon(icon4)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout_11.addWidget(self.pushButton_3)
        self.comboBox_2 = QtWidgets.QComboBox(self.layoutWidget_2)
        self.comboBox_2.setMinimumSize(QtCore.QSize(35, 0))
        self.comboBox_2.setMaximumSize(QtCore.QSize(35, 16777215))
        self.comboBox_2.setStyleSheet("color: rgb(170, 0, 0);")
        self.comboBox_2.setObjectName("comboBox_2")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.comboBox_2.addItem("")
        self.horizontalLayout_11.addWidget(self.comboBox_2)
        self.fontComboBox_4 = QtWidgets.QFontComboBox(self.layoutWidget_2)
        self.fontComboBox_4.setMinimumSize(QtCore.QSize(101, 0))
        self.fontComboBox_4.setStyleSheet("color: rgb(255, 85, 0);")
        self.fontComboBox_4.setObjectName("fontComboBox_4")
        self.horizontalLayout_11.addWidget(self.fontComboBox_4)
        self.pushButton_19 = QtWidgets.QPushButton(self.layoutWidget_2)
        self.pushButton_19.setMaximumSize(QtCore.QSize(55, 16777215))
        self.pushButton_19.setStyleSheet("color: rgb(0, 85, 0)")
        self.pushButton_19.setObjectName("pushButton_19")
        self.horizontalLayout_11.addWidget(self.pushButton_19)
        self.verticalLayout_3.addLayout(self.horizontalLayout_11)
        self.textEdit_3 = QtWidgets.QTextEdit(self.layoutWidget_2)
        self.textEdit_3.setReadOnly(True)
        self.textEdit_3.setObjectName("textEdit_3")
        self.verticalLayout_3.addWidget(self.textEdit_3)
        self.textEdit_7 = QtWidgets.QLineEdit(self.splitter_5)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_7.sizePolicy().hasHeightForWidth())
        self.textEdit_7.setSizePolicy(sizePolicy)
        self.textEdit_7.setMinimumSize(QtCore.QSize(0, 33))
        self.textEdit_7.setMaximumSize(QtCore.QSize(16777215, 33))
        self.textEdit_7.setReadOnly(True)
        self.textEdit_7.setObjectName("textEdit_7")
        self.textEdit_7.setStyleSheet("color: rgb(85, 0, 127)")
        self.textEdit_7.setAlignment(QtCore.Qt.AlignCenter)
        self.verticalLayout_7.addWidget(self.splitter_5)
        self.verticalLayout_5 = QtWidgets.QVBoxLayout()
        self.verticalLayout_5.setSpacing(6)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_3.setMinimumSize(QtCore.QSize(0, 33))
        self.lineEdit_3.setMaximumSize(QtCore.QSize(16777215, 111))
        self.lineEdit_3.setStyleSheet("color: rgb(85, 0, 0)")
        self.lineEdit_3.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_3.setReadOnly(True)
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.verticalLayout_5.addWidget(self.lineEdit_3)
        self.horizontalLayout_4 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_4.setSpacing(6)
        self.horizontalLayout_4.setObjectName("horizontalLayout_4")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_3.setSpacing(6)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.lineEdit = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit.setMaximumSize(QtCore.QSize(148, 33))
        self.lineEdit.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_3.addWidget(self.lineEdit)
        self.pushButton_5 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_5.setMaximumSize(QtCore.QSize(40, 27))
        self.pushButton_5.setText("")
        icon5 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"plus.png")
        icon5.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_5.setIcon(icon5)
        self.pushButton_5.setIconSize(QtCore.QSize(33, 17))
        self.pushButton_5.setObjectName("pushButton_5")
        self.horizontalLayout_3.addWidget(self.pushButton_5)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_3)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setSpacing(6)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.layoutWidget2)
        self.lineEdit_2.setMaximumSize(QtCore.QSize(148, 33))
        self.lineEdit_2.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton_6 = QtWidgets.QPushButton(self.layoutWidget2)
        self.pushButton_6.setMaximumSize(QtCore.QSize(40, 27))
        self.pushButton_6.setText("")
        icon6 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"minus.png")
        icon6.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.pushButton_6.setIcon(icon6)
        self.pushButton_6.setIconSize(QtCore.QSize(33, 17))
        self.pushButton_6.setObjectName("pushButton_6")
        self.horizontalLayout_2.addWidget(self.pushButton_6)
        self.horizontalLayout_4.addLayout(self.horizontalLayout_2)
        spacerItem4 = QtWidgets.QSpacerItem(22, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_4.addItem(spacerItem4)
        self.verticalLayout_5.addLayout(self.horizontalLayout_4)
        self.verticalLayout_7.addLayout(self.verticalLayout_5)
        self.splitter_8 = QtWidgets.QSplitter(self.splitter_6)
        self.splitter_8.setOrientation(QtCore.Qt.Vertical)
        self.splitter_8.setObjectName("splitter_8")
        self.textEdit_12 = QtWidgets.QTextEdit(self.splitter_8)
        self.textEdit_12.setReadOnly(True)
        self.textEdit_12.setObjectName("textEdit_12")
        self.textEdit_13 = QtWidgets.QTextEdit(self.splitter_8)
        self.textEdit_13.setReadOnly(True)
        self.textEdit_13.setObjectName("textEdit_13")
        self.textEdit_14 = QtWidgets.QTextEdit(self.splitter_8)
        self.textEdit_14.setReadOnly(True)
        self.textEdit_14.setObjectName("textEdit_14")
        self.horizontalLayout_5.addWidget(self.splitter_6)
        self.verticalLayout_12.addWidget(self.frame_2)
        self.frame_3 = QtWidgets.QFrame(self.centralWidget)
        self.frame_3.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_3.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_3.setObjectName("frame_3")
        self.horizontalLayout_6 = QtWidgets.QHBoxLayout(self.frame_3)
        self.horizontalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.horizontalLayout_6.setSpacing(1)
        self.horizontalLayout_6.setObjectName("horizontalLayout_6")
        self.splitter_9 = QtWidgets.QSplitter(self.frame_3)
        self.splitter_9.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_9.setObjectName("splitter_9")
        self.layoutWidget_4 = QtWidgets.QWidget(self.splitter_9)
        self.layoutWidget_4.setObjectName("layoutWidget_4")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.layoutWidget_4)
        self.verticalLayout_8.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_8.setSpacing(6)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.splitter_10 = QtWidgets.QSplitter(self.layoutWidget_4)
        self.splitter_10.setOrientation(QtCore.Qt.Vertical)
        self.splitter_10.setObjectName("splitter_10")
        self.splitter_11 = QtWidgets.QSplitter(self.splitter_10)
        self.splitter_11.setOrientation(QtCore.Qt.Horizontal)
        self.splitter_11.setObjectName("splitter_11")
        self.layoutWidget_5 = QtWidgets.QWidget(self.splitter_11)
        self.layoutWidget_5.setObjectName("layoutWidget_5")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.layoutWidget_5)
        self.verticalLayout_6.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_6.setSpacing(6)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.horizontalLayout_9 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_9.setSpacing(6)
        self.horizontalLayout_9.setObjectName("horizontalLayout_9")
        spacerItem5 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_9.addItem(spacerItem5)
        self.pushButton_7 = QtWidgets.QPushButton(self.layoutWidget_5)
        self.pushButton_7.setMaximumSize(QtCore.QSize(21, 21))
        self.pushButton_7.setText("")
        self.pushButton_7.setIcon(icon4)
        self.pushButton_7.setObjectName("pushButton_7")
        self.horizontalLayout_9.addWidget(self.pushButton_7)
        self.comboBox_3 = QtWidgets.QComboBox(self.layoutWidget_5)
        self.comboBox_3.setMinimumSize(QtCore.QSize(35, 0))
        self.comboBox_3.setMaximumSize(QtCore.QSize(35, 16777215))
        self.comboBox_3.setStyleSheet("color: rgb(255, 0, 127)")
        self.comboBox_3.setObjectName("comboBox_3")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.comboBox_3.addItem("")
        self.horizontalLayout_9.addWidget(self.comboBox_3)
        self.fontComboBox_5 = QtWidgets.QFontComboBox(self.layoutWidget_5)
        self.fontComboBox_5.setMinimumSize(QtCore.QSize(101, 0))
        self.fontComboBox_5.setStyleSheet("color: rgb(0, 0, 127);")
        self.fontComboBox_5.setObjectName("fontComboBox_5")
        self.horizontalLayout_9.addWidget(self.fontComboBox_5)
        self.verticalLayout_6.addLayout(self.horizontalLayout_9)
        self.textEdit_6 = QtWidgets.QTextEdit(self.layoutWidget_5)
        self.textEdit_6.setReadOnly(True)
        self.textEdit_6.setObjectName("textEdit_6")
        self.verticalLayout_6.addWidget(self.textEdit_6)
        self.layoutWidget_6 = QtWidgets.QWidget(self.splitter_11)
        self.layoutWidget_6.setObjectName("layoutWidget_6")
        self.verticalLayout_9 = QtWidgets.QVBoxLayout(self.layoutWidget_6)
        self.verticalLayout_9.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_9.setSpacing(6)
        self.verticalLayout_9.setObjectName("verticalLayout_9")
        self.horizontalLayout_12 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_12.setSizeConstraint(QtWidgets.QLayout.SetMinAndMaxSize)
        self.horizontalLayout_12.setSpacing(6)
        self.horizontalLayout_12.setObjectName("horizontalLayout_12")
        spacerItem6 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_12.addItem(spacerItem6)
        self.pushButton_8 = QtWidgets.QPushButton(self.layoutWidget_6)
        self.pushButton_8.setMaximumSize(QtCore.QSize(21, 21))
        self.pushButton_8.setText("")
        self.pushButton_8.setIcon(icon4)
        self.pushButton_8.setObjectName("pushButton_8")
        self.horizontalLayout_12.addWidget(self.pushButton_8)
        self.comboBox_4 = QtWidgets.QComboBox(self.layoutWidget_6)
        self.comboBox_4.setMinimumSize(QtCore.QSize(35, 0))
        self.comboBox_4.setMaximumSize(QtCore.QSize(35, 16777215))
        self.comboBox_4.setStyleSheet("color: rgb(170, 0, 0);")
        self.comboBox_4.setObjectName("comboBox_4")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.comboBox_4.addItem("")
        self.horizontalLayout_12.addWidget(self.comboBox_4)
        self.fontComboBox_6 = QtWidgets.QFontComboBox(self.layoutWidget_6)
        self.fontComboBox_6.setMinimumSize(QtCore.QSize(101, 0))
        self.fontComboBox_6.setStyleSheet("color: rgb(255, 85, 0);R")
        self.fontComboBox_6.setObjectName("fontComboBox_6")
        self.horizontalLayout_12.addWidget(self.fontComboBox_6)
        self.pushButton_20 = QtWidgets.QPushButton(self.layoutWidget_6)
        self.pushButton_20.setMaximumSize(QtCore.QSize(55, 16777215))
        self.pushButton_20.setStyleSheet("color: rgb(0, 85, 0)")
        self.pushButton_20.setObjectName("pushButton_20")
        self.horizontalLayout_12.addWidget(self.pushButton_20)
        self.verticalLayout_9.addLayout(self.horizontalLayout_12)
        self.textEdit_8 = QtWidgets.QTextEdit(self.layoutWidget_6)
        self.textEdit_8.setReadOnly(True)
        self.textEdit_8.setObjectName("textEdit_8")
        self.verticalLayout_9.addWidget(self.textEdit_8)
        self.textEdit_15 = QtWidgets.QLineEdit(self.splitter_10)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.textEdit_15.sizePolicy().hasHeightForWidth())
        self.textEdit_15.setSizePolicy(sizePolicy)
        self.textEdit_15.setMinimumSize(QtCore.QSize(0, 33))
        self.textEdit_15.setMaximumSize(QtCore.QSize(16777215, 33))
        self.textEdit_15.setReadOnly(True)
        self.textEdit_15.setObjectName("textEdit_15")
        self.textEdit_15.setStyleSheet("color: rgb(85, 0, 127)")
        self.textEdit_15.setAlignment(QtCore.Qt.AlignCenter)        
        self.verticalLayout_8.addWidget(self.splitter_10)
        self.verticalLayout_10 = QtWidgets.QVBoxLayout()
        self.verticalLayout_10.setSpacing(6)
        self.verticalLayout_10.setObjectName("verticalLayout_10")
        self.lineEdit_4 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_4.setMinimumSize(QtCore.QSize(0, 33))
        self.lineEdit_4.setMaximumSize(QtCore.QSize(16777215, 111))
        self.lineEdit_4.setStyleSheet("color: rgb(85, 0, 0)")
        self.lineEdit_4.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_4.setReadOnly(True)
        self.lineEdit_4.setObjectName("lineEdit_4")
        self.verticalLayout_10.addWidget(self.lineEdit_4)
        self.horizontalLayout_13 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_13.setSpacing(6)
        self.horizontalLayout_13.setObjectName("horizontalLayout_13")
        self.horizontalLayout_14 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_14.setSpacing(6)
        self.horizontalLayout_14.setObjectName("horizontalLayout_14")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_5.setMaximumSize(QtCore.QSize(148, 33))
        self.lineEdit_5.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.horizontalLayout_14.addWidget(self.lineEdit_5)
        self.pushButton_9 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_9.setMaximumSize(QtCore.QSize(40, 27))
        self.pushButton_9.setText("")
        self.pushButton_9.setIcon(icon5)
        self.pushButton_9.setIconSize(QtCore.QSize(33, 17))
        self.pushButton_9.setObjectName("pushButton_9")
        self.horizontalLayout_14.addWidget(self.pushButton_9)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_14)
        self.horizontalLayout_15 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_15.setSpacing(6)
        self.horizontalLayout_15.setObjectName("horizontalLayout_15")
        self.lineEdit_6 = QtWidgets.QLineEdit(self.layoutWidget_4)
        self.lineEdit_6.setMaximumSize(QtCore.QSize(148, 33))
        self.lineEdit_6.setAlignment(QtCore.Qt.AlignCenter)
        self.lineEdit_6.setObjectName("lineEdit_6")
        self.horizontalLayout_15.addWidget(self.lineEdit_6)
        self.pushButton_10 = QtWidgets.QPushButton(self.layoutWidget_4)
        self.pushButton_10.setMaximumSize(QtCore.QSize(40, 27))
        self.pushButton_10.setText("")
        self.pushButton_10.setIcon(icon6)
        self.pushButton_10.setIconSize(QtCore.QSize(33, 17))
        self.pushButton_10.setObjectName("pushButton_10")
        self.horizontalLayout_15.addWidget(self.pushButton_10)
        self.horizontalLayout_13.addLayout(self.horizontalLayout_15)
        spacerItem7 = QtWidgets.QSpacerItem(22, 24, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_13.addItem(spacerItem7)
        self.verticalLayout_10.addLayout(self.horizontalLayout_13)
        self.verticalLayout_8.addLayout(self.verticalLayout_10)
        self.splitter_12 = QtWidgets.QSplitter(self.splitter_9)
        self.splitter_12.setOrientation(QtCore.Qt.Vertical)
        self.splitter_12.setObjectName("splitter_12")
        self.textEdit_16 = QtWidgets.QTextEdit(self.splitter_12)
        self.textEdit_16.setReadOnly(True)
        self.textEdit_16.setObjectName("textEdit_16")
        self.textEdit_17 = QtWidgets.QTextEdit(self.splitter_12)
        self.textEdit_17.setReadOnly(True)
        self.textEdit_17.setOverwriteMode(True)
        self.textEdit_17.setObjectName("textEdit_17")
        self.textEdit_18 = QtWidgets.QTextEdit(self.splitter_12)
        self.textEdit_18.setReadOnly(True)
        self.textEdit_18.setOverwriteMode(True)
        self.textEdit_18.setObjectName("textEdit_18")
        self.horizontalLayout_6.addWidget(self.splitter_9)
        self.verticalLayout_12.addWidget(self.frame_3)
        self.frame_4 = QtWidgets.QFrame(self.centralWidget)
        self.frame_4.setMinimumSize(QtCore.QSize(0, 0))
        self.frame_4.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_4.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_4.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_4.setObjectName("frame_4")
        self.verticalLayout_11 = QtWidgets.QVBoxLayout(self.frame_4)
        self.verticalLayout_11.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_11.setSpacing(6)
        self.verticalLayout_11.setObjectName("verticalLayout_11")
        self.horizontalLayout_24 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_24.setSpacing(6)
        self.horizontalLayout_24.setObjectName("horizontalLayout_24")
        self.pushButton_16 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_16.setFont(font)
        self.pushButton_16.setStyleSheet("color: rgb(0, 85, 0)")
        self.pushButton_16.setObjectName("pushButton_16")
        self.horizontalLayout_24.addWidget(self.pushButton_16)
        spacerItem8 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_24.addItem(spacerItem8)
        self.verticalLayout_11.addLayout(self.horizontalLayout_24)
        self.horizontalLayout_16 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_16.setSpacing(6)
        self.horizontalLayout_16.setObjectName("horizontalLayout_16")
        self.pushButton_11 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_11.setFont(font)
        self.pushButton_11.setStyleSheet("color: rgb(0, 0, 127);")
        self.pushButton_11.setObjectName("pushButton_11")
        self.horizontalLayout_16.addWidget(self.pushButton_11)
        self.lineEdit_7 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_7.setObjectName("lineEdit_7")
        self.horizontalLayout_16.addWidget(self.lineEdit_7)
        self.label = QtWidgets.QLabel(self.frame_4)
        self.label.setObjectName("label")
        self.horizontalLayout_16.addWidget(self.label)
        self.verticalLayout_11.addLayout(self.horizontalLayout_16)
        self.horizontalLayout_17 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_17.setSpacing(6)
        self.horizontalLayout_17.setObjectName("horizontalLayout_17")
        self.pushButton_12 = QtWidgets.QPushButton(self.frame_4)
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet("color: rgb(0, 0, 127);")
        self.pushButton_12.setObjectName("pushButton_12")
        self.horizontalLayout_17.addWidget(self.pushButton_12)
        self.lineEdit_8 = QtWidgets.QLineEdit(self.frame_4)
        self.lineEdit_8.setObjectName("lineEdit_8")
        self.horizontalLayout_17.addWidget(self.lineEdit_8)
        self.label_2 = QtWidgets.QLabel(self.frame_4)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_17.addWidget(self.label_2)
        self.verticalLayout_11.addLayout(self.horizontalLayout_17)
        self.line = QtWidgets.QFrame(self.frame_4)
        self.line.setFrameShape(QtWidgets.QFrame.HLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.verticalLayout_11.addWidget(self.line)
        self.horizontalLayout_18 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_18.setSpacing(6)
        self.horizontalLayout_18.setObjectName("horizontalLayout_18")
        spacerItem9 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_18.addItem(spacerItem9)
        self.checkBox = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox.setChecked(True)
        self.checkBox.setAutoExclusive(True)
        self.checkBox.setObjectName("checkBox")
        self.horizontalLayout_18.addWidget(self.checkBox)
        self.checkBox_2 = QtWidgets.QCheckBox(self.frame_4)
        self.checkBox_2.setChecked(False)
        self.checkBox_2.setAutoExclusive(True)
        self.checkBox_2.setObjectName("checkBox_2")
        self.horizontalLayout_18.addWidget(self.checkBox_2)
        self.label_3 = QtWidgets.QLabel(self.frame_4)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_18.addWidget(self.label_3)
        self.verticalLayout_11.addLayout(self.horizontalLayout_18)
        spacerItem10 = QtWidgets.QSpacerItem(20, 40, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Expanding)
        self.verticalLayout_11.addItem(spacerItem10)
        self.verticalLayout_12.addWidget(self.frame_4)
        self.frame_5 = QtWidgets.QFrame(self.centralWidget)
        self.frame_5.setMinimumSize(QtCore.QSize(0, 333))
        self.frame_5.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_5.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_5.setObjectName("frame_5")
        self.verticalLayout_14 = QtWidgets.QVBoxLayout(self.frame_5)
        self.verticalLayout_14.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_14.setSpacing(6)
        self.verticalLayout_14.setObjectName("verticalLayout_14")
        self.horizontalLayout_21 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_21.setSpacing(6)
        self.horizontalLayout_21.setObjectName("horizontalLayout_21")
        self.pushButton_13 = QtWidgets.QPushButton(self.frame_5)
        self.pushButton_13.setMaximumSize(QtCore.QSize(66, 16777215))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet("color: rgb(0, 85, 0);")
        self.pushButton_13.setObjectName("pushButton_13")
        self.horizontalLayout_21.addWidget(self.pushButton_13)
        spacerItem11 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_21.addItem(spacerItem11)
        self.verticalLayout_14.addLayout(self.horizontalLayout_21)
        self.tabWidget = QtWidgets.QTabWidget(self.frame_5)
        self.tabWidget.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_15 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_15.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_15.setSpacing(6)
        self.verticalLayout_15.setObjectName("verticalLayout_15")
        self.textEdit_10 = QtWidgets.QTextBrowser(self.tab)
        self.textEdit_10.setObjectName("textEdit_10")
        self.textEdit_10.setProperty("openExternalLinks", True)
        self.verticalLayout_15.addWidget(self.textEdit_10)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.verticalLayout_16 = QtWidgets.QVBoxLayout(self.tab_2)
        self.verticalLayout_16.setContentsMargins(1, 1, 1, 1)
        self.verticalLayout_16.setSpacing(6)
        self.verticalLayout_16.setObjectName("verticalLayout_16")
        self.horizontalLayout_20 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_20.setSpacing(6)
        self.horizontalLayout_20.setObjectName("horizontalLayout_20")
        spacerItem12 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_20.addItem(spacerItem12)
        self.pushButton_14 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_14.setObjectName("pushButton_14")
        self.horizontalLayout_20.addWidget(self.pushButton_14)
        self.verticalLayout_16.addLayout(self.horizontalLayout_20)
        self.textEdit_19 = QtWidgets.QTextBrowser(self.tab_2)
        self.textEdit_19.setObjectName("textEdit_19")
        self.textEdit_19.setProperty("openExternalLinks", True)
        self.verticalLayout_16.addWidget(self.textEdit_19)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout_14.addWidget(self.tabWidget)
        self.verticalLayout_12.addWidget(self.frame_5)
        Notepad.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(Notepad)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 814, 21))
        self.menuBar.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuBar.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.menuBar.setObjectName("menuBar")
        self.menuEdit = QtWidgets.QMenu(self.menuBar)
        self.menuEdit.setGeometry(QtCore.QRect(272, 132, 165, 178))
        self.menuEdit.setBaseSize(QtCore.QSize(0, 0))
        self.menuEdit.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuEdit.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.menuEdit.setObjectName("menuEdit")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menuBar)
        self.menu_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menu_2.setObjectName("menu_2")
        self.menuFormat = QtWidgets.QMenu(self.menu_2)
        self.menuFormat.setObjectName("menuFormat")
        self.menu_4 = QtWidgets.QMenu(self.menuBar)
        self.menu_4.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.menu_4.setObjectName("menu_4")
        self.menu_5 = QtWidgets.QMenu(self.menuBar)
        self.menu_5.setLocale(QtCore.QLocale(QtCore.QLocale.Arabic, QtCore.QLocale.Egypt))
        self.menu_5.setObjectName("menu_5")
        self.menuRescources = QtWidgets.QMenu(self.menuBar)
        self.menuRescources.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.menuRescources.setObjectName("menuRescources")
        self.menuMessages = QtWidgets.QMenu(self.menuBar)
        self.menuMessages.setObjectName("menuMessages")
        Notepad.setMenuBar(self.menuBar)
        self.toolBar_3 = QtWidgets.QToolBar(Notepad)
        self.toolBar_3.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar_3.setObjectName("toolBar_3")
        Notepad.addToolBar(QtCore.Qt.RightToolBarArea, self.toolBar_3)
        self.toolBar_2 = QtWidgets.QToolBar(Notepad)
        self.toolBar_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.toolBar_2.setIconSize(QtCore.QSize(38, 27))
        self.toolBar_2.setObjectName("toolBar_2")
        Notepad.addToolBar(QtCore.Qt.TopToolBarArea, self.toolBar_2)
        self.action_8 = QtWidgets.QAction(Notepad)
        icon7 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"print.png")
        icon7.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_8.setIcon(icon7)
        self.action_8.setObjectName("action_8")
        self.action_11 = QtWidgets.QAction(Notepad)
        self.action_11.setIcon(icon2)
        self.action_11.setObjectName("action_11")
        self.action_12 = QtWidgets.QAction(Notepad)
        self.action_12.setIcon(icon2)
        self.action_12.setObjectName("action_12")
        self.action_10 = QtWidgets.QAction(Notepad)
        icon8 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"document-copy.png")
        icon8.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_10.setIcon(icon8)
        self.action_10.setObjectName("action_10")
        self.action_14 = QtWidgets.QAction(Notepad)
        icon9 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"clipboard-paste-document-text.png")
        icon9.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_14.setIcon(icon9)
        self.action_14.setObjectName("action_14")
        self.action_17 = QtWidgets.QAction(Notepad)
        icon10 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"arrow-curve-180-left.png")
        icon10.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_17.setIcon(icon10)
        self.action_17.setObjectName("action_17")
        self.action_18 = QtWidgets.QAction(Notepad)
        icon11 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"arrow-curve.png")
        icon11.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_18.setIcon(icon11)
        self.action_18.setObjectName("action_18")
        self.action_26 = QtWidgets.QAction(Notepad)
        icon12 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"edit-alignment-justify.png")
        icon12.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_26.setIcon(icon12)
        self.action_26.setObjectName("action_26")
        self.action_25 = QtWidgets.QAction(Notepad)
        icon13 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"edit-alignment-center.png")
        icon13.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_25.setIcon(icon13)
        self.action_25.setObjectName("action_25")
        self.action_23 = QtWidgets.QAction(Notepad)
        icon14 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"edit-alignment-right.png")
        icon14.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_23.setIcon(icon14)
        self.action_23.setObjectName("action_23")
        self.action_24 = QtWidgets.QAction(Notepad)
        icon15 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"edit-italic.png")
        icon15.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_24.setIcon(icon15)
        self.action_24.setObjectName("action_24")
        self.action_27 = QtWidgets.QAction(Notepad)
        icon16 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"edit-bold.png")
        icon16.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_27.setIcon(icon16)
        self.action_27.setObjectName("action_27")
        self.action = QtWidgets.QAction(Notepad)
        self.action.setIcon(icon3)
        self.action.setObjectName("action")
        self.action_2 = QtWidgets.QAction(Notepad)
        self.action_2.setIcon(icon3)
        self.action_2.setObjectName("action_2")
        self.action_3 = QtWidgets.QAction(Notepad)
        self.action_3.setIcon(icon7)
        self.action_3.setObjectName("action_3")
        self.action_7 = QtWidgets.QAction(Notepad)
        icon17 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"scissors.png")
        icon17.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_7.setIcon(icon17)
        self.action_7.setObjectName("action_7")
        self.action_13 = QtWidgets.QAction(Notepad)
        icon18 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"edit_redo.png")
        icon18.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_13.setIcon(icon18)
        self.action_13.setObjectName("action_13")
        self.action_15 = QtWidgets.QAction(Notepad)
        icon19 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"edit_undo.png")
        icon19.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_15.setIcon(icon19)
        self.action_15.setObjectName("action_15")
        self.action_16 = QtWidgets.QAction(Notepad)
        icon20 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"paste.png")
        icon20.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_16.setIcon(icon20)
        self.action_16.setObjectName("action_16")
        self.action_19 = QtWidgets.QAction(Notepad)
        icon21 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"copy.png")
        icon21.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_19.setIcon(icon21)
        self.action_19.setObjectName("action_19")
        self.action_20 = QtWidgets.QAction(Notepad)
        self.action_20.setIcon(icon14)
        self.action_20.setObjectName("action_20")
        self.action_21 = QtWidgets.QAction(Notepad)
        self.action_21.setIcon(icon13)
        self.action_21.setObjectName("action_21")
        self.action_22 = QtWidgets.QAction(Notepad)
        self.action_22.setIcon(icon12)
        self.action_22.setObjectName("action_22")
        self.action_29 = QtWidgets.QAction(Notepad)
        icon22 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"italic.png")
        icon22.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_29.setIcon(icon22)
        self.action_29.setObjectName("action_29")
        self.action_31 = QtWidgets.QAction(Notepad)
        icon23 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"selection-input.png")
        icon23.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_31.setIcon(icon23)
        self.action_31.setObjectName("action_31")
        self.action_32 = QtWidgets.QAction(Notepad)
        icon24 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"arrow-continue.png")
        icon24.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_32.setIcon(icon24)
        self.action_32.setObjectName("action_32")
        self.action_33 = QtWidgets.QAction(Notepad)
        icon25 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"edit-underline.png")
        icon25.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_33.setIcon(icon25)
        self.action_33.setObjectName("action_33")
        self.action_36 = QtWidgets.QAction(Notepad)
        self.action_36.setIcon(icon23)
        self.action_36.setObjectName("action_36")
        self.action_37 = QtWidgets.QAction(Notepad)
        self.action_37.setIcon(icon24)
        self.action_37.setObjectName("action_37")
        self.action_38 = QtWidgets.QAction(Notepad)
        self.action_38.setIcon(icon25)
        self.action_38.setObjectName("action_38")
        self.action_9 = QtWidgets.QAction(Notepad)
        icon26 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"bold.png")
        icon26.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_9.setIcon(icon26)
        self.action_9.setObjectName("action_9")
        self.action_1 = QtWidgets.QAction(Notepad)
        self.action_1.setIcon(icon4)
        self.action_1.setObjectName("action_1")
        self.action_34 = QtWidgets.QAction(Notepad)
        self.action_34.setIcon(icon4)
        self.action_34.setObjectName("action_34")
        self.action_30 = QtWidgets.QAction(Notepad)
        self.action_30.setCheckable(True)
        icon27 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-write-100 (3).png")
        icon27.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_30.setIcon(icon27)
        self.action_30.setObjectName("action_30")
        self.action_35 = QtWidgets.QAction(Notepad)
        self.action_35.setCheckable(True)
        self.action_35.setChecked(False)
        icon28 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-write-100 (3) - Copie.png")
        icon28.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_35.setIcon(icon28)
        self.action_35.setObjectName("action_35")
        self.action_5 = QtWidgets.QAction(Notepad)
        icon29 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"guide.png")
        icon29.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_5.setIcon(icon29)
        self.action_5.setObjectName("action_5")
        self.action_6 = QtWidgets.QAction(Notepad)
        icon30 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-about-100.png")
        icon30.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_6.setIcon(icon30)
        self.action_6.setObjectName("action_6")
        self.action_28 = QtWidgets.QAction(Notepad)
        icon31 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-license-100.png")
        icon31.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_28.setIcon(icon31)
        self.action_28.setObjectName("action_28")
        self.action_4 = QtWidgets.QAction(Notepad)
        icon32 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-logout-100.png")
        icon32.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_4.setIcon(icon32)
        self.action_4.setObjectName("action_4")
        self.action_39 = QtWidgets.QAction(Notepad)
        self.action_39.setCheckable(False)
        icon33 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-settings-100 (2).png")
        icon33.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.action_39.setIcon(icon33)
        self.action_39.setObjectName("action_39")
        self.actionWords_templates_database = QtWidgets.QAction(Notepad)
        icon34 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-database-server-with-cloud-storage-online-layout-100 (1).png")
        icon34.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionWords_templates_database.setIcon(icon34)
        self.actionWords_templates_database.setObjectName("actionWords_templates_database")
        self.actionWords_synonyme_antonyme_database = QtWidgets.QAction(Notepad)
        icon35 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-database-server-with-cloud-storage-online-layout-100 (1) - Copie.png")
        icon35.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionWords_synonyme_antonyme_database.setIcon(icon35)
        self.actionWords_synonyme_antonyme_database.setObjectName("actionWords_synonyme_antonyme_database")
        self.actionMessages = QtWidgets.QAction(Notepad)
        icon36 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-new-message-100.png")
        icon36.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionMessages.setIcon(icon36)
        self.actionMessages.setObjectName("actionMessages")
        self.actionForum = QtWidgets.QAction(Notepad)
        icon37 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"forum2.png")
        icon37.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionForum.setIcon(icon37)
        self.actionForum.setObjectName("actionForum")
        self.actionAcount = QtWidgets.QAction(Notepad)
        icon38 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-user-100.png")
        icon38.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionAcount.setIcon(icon38)
        self.actionAcount.setObjectName("actionAcount")
        self.actionAdjust_left = QtWidgets.QAction(Notepad)
        icon39 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"edit-alignment.png")
        icon39.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionAdjust_left.setIcon(icon39)
        self.actionAdjust_left.setObjectName("actionAdjust_left")
        self.actionRestart = QtWidgets.QAction(Notepad)
        icon40 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-restart-100.png")
        icon40.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionRestart.setIcon(icon40)
        self.actionRestart.setObjectName("actionRestart")
        self.actionRestart_2 = QtWidgets.QAction(Notepad)
        self.actionRestart_2.setIcon(icon40)
        self.actionRestart_2.setObjectName("actionRestart_2")
        self.actionExit = QtWidgets.QAction(Notepad)
        self.actionExit.setIcon(icon32)
        self.actionExit.setObjectName("actionExit")
        self.actionMessages_2 = QtWidgets.QAction(Notepad)
        icon41 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"ni0.png")
        icon41.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionMessages_2.setIcon(icon41)
        self.actionMessages_2.setObjectName("actionMessages_2")
        self.actionAccount_setting = QtWidgets.QAction(Notepad)
        icon42 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"icons8-account-100.png")
        icon42.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionAccount_setting.setIcon(icon42)
        self.actionAccount_setting.setObjectName("actionAccount_setting")
        self.actionWords_templates_database_2 = QtWidgets.QAction(Notepad)
        self.actionWords_templates_database_2.setIcon(icon34)
        self.actionWords_templates_database_2.setObjectName("actionWords_templates_database_2")
        self.actionWords_synonyme_antonyme_database_2 = QtWidgets.QAction(Notepad)
        self.actionWords_synonyme_antonyme_database_2.setIcon(icon35)
        self.actionWords_synonyme_antonyme_database_2.setObjectName("actionWords_synonyme_antonyme_database_2")
        self.actionGuide = QtWidgets.QAction(Notepad)
        icon43 = QtGui.QIcon()
        dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"guide.png")
        icon43.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)

        self.actionGuide.setIcon(icon43)
        self.actionGuide.setObjectName("actionGuide")
        self.actionForum_2 = QtWidgets.QAction(Notepad)
        self.actionForum_2.setIcon(icon37)
        self.actionForum_2.setObjectName("actionForum_2")
        self.actionAbout = QtWidgets.QAction(Notepad)
        self.actionAbout.setIcon(icon30)
        self.actionAbout.setObjectName("actionAbout")
        self.actionnnn = QtWidgets.QAction(Notepad)
        self.actionnnn.setObjectName("actionnnn")
        self.actionAlign_left = QtWidgets.QAction(Notepad)
        self.actionAlign_left.setIcon(icon39)
        self.actionAlign_left.setObjectName("actionAlign_left")
        self.menuEdit.addAction(self.actionAbout)
        self.menuEdit.addAction(self.action_28)
        self.menuEdit.addAction(self.action_5)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.actionForum)
        self.menuEdit.addSeparator()
        self.menuEdit.addAction(self.action_4)
        self.menu.addAction(self.action_11)
        self.menu.addSeparator()
        self.menu.addAction(self.action)
        self.menu.addAction(self.action_2)
        self.menu.addSeparator()
        self.menu.addAction(self.action_8)
        self.menu.addAction(self.action_3)
        self.menuFormat.addAction(self.action_25)
        self.menuFormat.addAction(self.action_26)
        self.menuFormat.addAction(self.actionAdjust_left)
        self.menuFormat.addAction(self.action_23)
        self.menuFormat.addAction(self.action_33)
        self.menuFormat.addAction(self.action_27)
        self.menuFormat.addAction(self.action_24)
        self.menu_2.addAction(self.action_18)
        self.menu_2.addAction(self.action_17)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_14)
        self.menu_2.addAction(self.action_10)
        self.menu_2.addAction(self.action_31)
        self.menu_2.addAction(self.action_7)
        self.menu_2.addSeparator()
        self.menu_2.addAction(self.action_32)
        self.menu_2.addAction(self.menuFormat.menuAction())
        self.menu_4.addAction(self.action_30)
        self.menu_4.addAction(self.action_35)
        self.menu_5.addAction(self.action_39)
        self.menuRescources.addAction(self.actionWords_templates_database)
        self.menuRescources.addAction(self.actionWords_synonyme_antonyme_database)
        self.menuMessages.addAction(self.actionMessages)
        self.menuBar.addAction(self.menuEdit.menuAction())
        self.menuBar.addAction(self.menu_2.menuAction())
        self.menuBar.addAction(self.menu.menuAction())
        self.menuBar.addAction(self.menuRescources.menuAction())
        self.menuBar.addAction(self.menu_4.menuAction())
        self.menuBar.addAction(self.menuMessages.menuAction())
        self.menuBar.addAction(self.menu_5.menuAction())
        self.toolBar_3.addAction(self.action_7)
        self.toolBar_3.addAction(self.action_10)
        self.toolBar_3.addAction(self.action_14)
        self.toolBar_3.addAction(self.action_17)
        self.toolBar_3.addAction(self.action_18)
        self.toolBar_3.addAction(self.actionAlign_left)
        self.toolBar_3.addAction(self.action_26)
        self.toolBar_3.addAction(self.action_25)
        self.toolBar_3.addAction(self.action_23)
        self.toolBar_3.addAction(self.action_24)
        self.toolBar_3.addAction(self.action_31)
        self.toolBar_3.addAction(self.action_32)
        self.toolBar_3.addAction(self.action_33)
        self.toolBar_3.addAction(self.action_27)
        self.toolBar_2.addAction(self.action_39)
        self.toolBar_2.addAction(self.actionGuide)
        self.toolBar_2.addAction(self.actionMessages_2)
        self.toolBar_2.addAction(self.actionForum_2)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.action_35)
        self.toolBar_2.addAction(self.action_30)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionWords_templates_database_2)
        self.toolBar_2.addAction(self.actionWords_synonyme_antonyme_database_2)
        self.toolBar_2.addSeparator()
        self.toolBar_2.addAction(self.actionExit)

        self.retranslateUi(Notepad)
        self.tabWidget.setCurrentIndex(0)
        self.pushButton_31.pressed.connect(self.action.trigger) # type: ignore
        self.pushButton_32.pressed.connect(self.action_11.trigger) # type: ignore
        self.action_18.triggered.connect(self.textEdit.redo) # type: ignore
        self.action_17.triggered.connect(self.textEdit.undo) # type: ignore
        self.action_14.triggered.connect(self.textEdit.paste) # type: ignore
        self.action_10.triggered.connect(self.textEdit.copy) # type: ignore
        self.action_7.triggered.connect(self.textEdit.cut) # type: ignore
        self.pushButton_2.pressed.connect(self.action_1.trigger) # type: ignore
        self.pushButton.pressed.connect(self.action_34.trigger) # type: ignore
        self.action_13.triggered.connect(self.textEdit_2.redo) # type: ignore
        self.action_15.triggered.connect(self.textEdit_2.undo) # type: ignore
        self.action_16.triggered.connect(self.textEdit_2.paste) # type: ignore
        self.action_19.triggered.connect(self.textEdit_2.copy) # type: ignore
        self.fontComboBox.currentFontChanged['QFont'].connect(self.textEdit.setCurrentFont) # type: ignore
        self.fontComboBox_2.currentFontChanged['QFont'].connect(self.textEdit_2.setCurrentFont) # type: ignore
        self.action_4.triggered.connect(Notepad.close) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Notepad)








        # start      ---------------------------------------
        
        # Setup the QTextEdit textEdit configuration
        self.textEdit.setAutoFormatting(QTextEdit.AutoAll)
        self.textEdit.selectionChanged.connect(self.update_format)


        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None
 
        self.action_11.triggered.connect(lambda: self.file_open(self.textEdit,'save as'))
        self.action.setCheckable(True)
        self.action.triggered.connect(lambda: self.file_save(self.textEdit,self.textEdit_path))
        self.action_8.triggered.connect(lambda: self.hlpl_file_print(self.textEdit.toPlainText()))
        self.textEdit_path=None
        self.action_1.triggered.connect(lambda: self.file_saveas(self.textEdit,'save as'))
        self.action_34.triggered.connect(lambda: self.file_saveas(self.textEdit_2,'save as'))
        self.pushButton_30.pressed.connect(self.my_clear1)           


        self.action_23.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignLeft)) 
        self.actionAdjust_left.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignRight))
        self.actionAlign_left.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignRight))
        self.action_25.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignCenter))
        self.action_26.triggered.connect(lambda: self.textEdit.setAlignment(Qt.AlignJustify))
        self.action_24.setCheckable(True)
        self.action_24.toggled.connect(self.textEdit.setFontItalic)
        self.action_27.setCheckable(True)
        self.action_27.toggled.connect(lambda x: self.textEdit.setFontWeight(QFont.Bold if x else QFont.Normal))
        
        
        self.action_31.triggered.connect(self.textEdit.selectAll)       
        self.action_31.setChecked(True)
        
        self.action_32.triggered.connect(lambda: self.edit_toggle_wrap(self.textEdit))       
        self.action_32.setCheckable(True)
        
        self.action_33.toggled.connect(self.textEdit.setFontUnderline)
        self.action_33.setCheckable(True)

        self.comboBox_8.currentIndexChanged[str].connect(lambda s: self.textEdit.setFontPointSize(float(s)) )
        

        # A list of all format-related widgets/actions, so we can disable/enable signals when updating.
        self._format_actions = [
            self.action_23, 
            self.action_25,
            self.action_26,
            self.action_24, 
            self.action_27,
            self.action_32,
            self.action_33,            
            # We don't need to disable signals for alignment, as they are paragraph-wide.
        ]


        # Initialize.
        self.update_format()
        #self.update_title()

#---------------------------------------------------------------------------------------------
        
        # Setup the QTextEdit textEdit_2 configuration
        self.textEdit_2.setAutoFormatting(QTextEdit.AutoAll)
        self.textEdit_2.selectionChanged.connect(self.update_format2)

        # self.path holds the path of the currently open file.
        # If none, we haven't got a file open yet (or creating new).
        self.path = None

 
        self.action.setCheckable(True)
        self.action_2.triggered.connect(lambda: self.file_saveas(self.textEdit_2,'save as'))
        self.action_3.triggered.connect(self.hlpl_file_print)
   
   
        self.action_20.triggered.connect(lambda: self.textEdit_2.setAlignment(Qt.AlignLeft))
        self.action_21.triggered.connect(lambda: self.textEdit_2.setAlignment(Qt.AlignCenter))
        self.action_22.triggered.connect(lambda: self.textEdit_2.setAlignment(Qt.AlignJustify))
        self.action_29.setCheckable(True)
        self.action_29.toggled.connect(self.textEdit_2.setFontItalic)
        self.action_9.setCheckable(True)
        self.action_9.toggled.connect(lambda x: self.textEdit_2.setFontWeight(QFont.Bold if x else QFont.Normal))
        
        
        self.action_36.triggered.connect(self.textEdit_2.selectAll)       
        self.action_36.setChecked(True)
        
        self.action_37.triggered.connect(lambda: self.edit_toggle_wrap(self.textEdit))        
        self.action_37.setCheckable(True)
        
        self.action_38.toggled.connect(self.textEdit_2.setFontUnderline)
        self.action_38.setCheckable(True)

        self.comboBox_7.currentIndexChanged[str].connect(lambda s: self.textEdit_2.setFontPointSize(float(s)) )
        

        # A list of all format-related widgets/actions, so we can disable/enable signals when updating.
        self._format_actions = [
            self.action_20,            
            self.action_21,
            self.action_22,
            self.action_29, 
            self.action_9,
            self.action_37, 
            self.action_38,
            # We don't need to disable signals for alignment, as they are paragraph-wide.
        ]

        #Initialize. 
        self.frame_2.hide()
        self.frame_3.hide()  


        self.flowLayout1 = FlowLayout(self.textEdit_4)
        self.flowLayout2 = FlowLayout(self.textEdit_6)
        self.flowLayout3 = FlowLayout(self.textEdit_3)
        self.flowLayout4 = FlowLayout(self.textEdit_8)

        
        
        self.action_30.toggled.connect(self.activate_alike)
        self.action_35.toggled.connect(self.activate_oposit)
        self.text_length=100           
        self.action_30.toggled.connect(self.my_f1)        
        self.action_35.toggled.connect(self.my_f2) 
        
        
        for i in range(self.text_length):
              exec('self.pushButton81_'+str(i)+' = QPushButton()\nself.pushButton81_'+str(i)+'.setObjectName(u"pushButton81_'+str(i)+'")')          
        for i in range(self.text_length):
              exec('self.pushButton82_'+str(i)+' = QPushButton()\nself.pushButton82_'+str(i)+'.setObjectName(u"pushButton82_'+str(i)+'")')
        
        for n in range(self.text_length):
            getattr(self, 'pushButton81_%s' % n).pressed.connect(lambda v=n: self.input_number(v))
        for n in range(self.text_length):
            getattr(self, 'pushButton82_%s' % n).pressed.connect(lambda v=n: self.input_numberr(v))


        for i in range(self.text_length):
              exec('self.pushButton83_'+str(i)+' = QPushButton()\nself.pushButton83_'+str(i)+'.setObjectName(u"pushButton83_'+str(i)+'")')          
        for i in range(self.text_length):
              exec('self.pushButton84_'+str(i)+' = QPushButton()\nself.pushButton84_'+str(i)+'.setObjectName(u"pushButton84_'+str(i)+'")')
        
        for n in range(self.text_length):
            getattr(self, 'pushButton83_%s' % n).pressed.connect(lambda v=n: self.hlpl_input_number_2(v))
        for n in range(self.text_length):
            getattr(self, 'pushButton84_%s' % n).pressed.connect(lambda v=n: self.input_numberr2(v))
            
        self.frame_4.hide()

 

        self.frame_4.hide()


        # CREATE WIZARD, WATERMARK, LOGO, BANNER ----------------------------------------------------
        wizard = QtWidgets.QWizard()
        wizard.setWizardStyle(QtWidgets.QWizard.ModernStyle)

        try: # PYSIDE
           wizard.setPixmap(QtWidgets.QWizard.WatermarkPixmap,
                    'Watermark.png')
           wizard.setPixmap(QtWidgets.QWizard.LogoPixmap,
                    'Logo.png')
           wizard.setPixmap(QtWidgets.QWizard.BannerPixmap,
                    'Banner.png')
        except TypeError: # PYQT5
           wizard.setPixmap(QtWidgets.QWizard.WatermarkPixmap,
            QtGui.QPixmap('Watermark.png'))
           wizard.setPixmap(QtWidgets.QWizard.LogoPixmap,
            QtGui.QPixmap('Logo.png'))
           wizard.setPixmap(QtWidgets.QWizard.BannerPixmap,
            QtGui.QPixmap('Banner.png'))


        # CREATE PAGE 1, LINE EDIT, TITLES
        page1 = QtWidgets.QWizardPage()
        page1.setTitle('Page 1 is best!')
        page1.setSubTitle('1111111111')
        lineEdit_w = QtWidgets.QLineEdit()
        hLayout1 = QtWidgets.QHBoxLayout(page1)
        hLayout1.addWidget(lineEdit_w)

        try: # PYSIDE
            page1.registerField('myField*', 
                lineEdit_w,
                lineEdit_w.text(),
               'textChanged')
        except TypeError: # PYQT5
           page1.registerField('myField*', 
                lineEdit_w,
                lineEdit_w.text(),
                lineEdit_w.textChanged)

        # CREATE PAGE 2, LABEL, TITLES
        page2 = QtWidgets.QWizardPage()
        page2.setFinalPage(True)
        page2.setTitle('Page 2 is better!')
        page2.setSubTitle('Lies!')
        label = QtWidgets.QLabel()
        hLayout2 = QtWidgets.QHBoxLayout(page2)
        hLayout2.addWidget(label)

        # CONNECT SIGNALS AND PAGES
        nxt = wizard.button(QtWidgets.QWizard.NextButton)
        func = lambda:label.setText(page1.field('myField'))
        nxt.clicked.connect(func)
        wizard.addPage(page1)
        wizard.addPage(page2)
        page2 = QtWidgets.QWizardPage()
        page2.setFinalPage(True)
        page2.setTitle('Page 2 is better!')
        page2.setSubTitle('Lies!')
        label = QtWidgets.QLabel()
        hLayout2 = QtWidgets.QHBoxLayout(page2)
        hLayout2.addWidget(label)

        # CONNECT SIGNALS AND PAGES
        nxt = wizard.button(QtWidgets.QWizard.NextButton)
        func = lambda:label.setText(page1.field('myField'))
        nxt.clicked.connect(func)
        wizard.addPage(page1)
        wizard.addPage(page2)

        wizard.hide()
        
        
        # new ------------------
        self.hlpl_sa_loop=-1;self.hlpl_sa_loop_pb=-1;self.hlpl_sa_st='';self.hlpl_sa_lst=[]
        self.hlpl_sa2_loop=-1;self.hlpl_sa2_loop_pb=-1;self.hlpl_sa2_st='';self.hlpl_sa2_lst=[]
        
        self.hlpl_as_loop=-1;self.hlpl_as_loop_pb=-1;self.hlpl_as_st='';self.hlpl_as_lst=[]
        self.hlpl_as2_loop=-1;self.hlpl_as2_loop_pb=-1;self.hlpl_as2_st='';self.hlpl_as2_lst=[]
        
        #self.pushButton_37.pressed.connect(lambda: self.hlpl_save_activated_sa(self.flowLayout1))
        self.pushButton_7.pressed.connect(lambda: self.hlpl_save_activated_sa(self.flowLayout2,'save'))
        
        self.pushButton_8.pressed.connect(lambda: self.hlpl_save_activated_sa(self.flowLayout4,'save'))
        
        
        self.pushButton_4.pressed.connect(lambda: self.hlpl_save_activated_sa(self.flowLayout1,'save'))

        self.pushButton_3.pressed.connect(lambda: self.hlpl_save_activated_sa(self.flowLayout3,'save'))
        
        
        
        

        # canvas 9 
        self.layout9 = FlowLayout(self.textEdit_9)
        self.layout12 = FlowLayout(self.textEdit_12)
        self.layout13 = FlowLayout(self.textEdit_13)
        self.layout14 = FlowLayout(self.textEdit_14)
        self.layout16 = FlowLayout(self.textEdit_16)
        self.layout17 = FlowLayout(self.textEdit_17)
        self.layout18 = FlowLayout(self.textEdit_18)
        self.layout11 = FlowLayout(self.textEdit_11)
        
        

        self.retranslateUi(Notepad)    
        self.textEdit.setText(' ')

        if self.checkBox.isChecked()==True:
           self.hlpl_letters_status('ar')  
        else:
           self.hlpl_letters_status('en') 
           
           
        
        self.action_28.triggered.connect(self.hlpl_license)
        self.action_5.triggered.connect(self.hlpl_guide) 
        self.actionGuide.triggered.connect(self.hlpl_guide)
        self.action_4.triggered.connect(self.hlpl_close)
        self.actionExit.triggered.connect(self.hlpl_close)
        self.actionForum.triggered.connect(self.hlpl_Forum)
        self.actionForum_2.triggered.connect(self.hlpl_Forum)          
               
        self.actionAcount.triggered.connect(lambda: self.hlpl_hide_show_2('hlpl_account'))
        self.action_39.triggered.connect(lambda: self.hlpl_hide_show_2('hlpl_setting'))
        self.actionMessages.triggered.connect(lambda: self.hlpl_hide_show_2('hlpl_message'))
        self.actionMessages_2.triggered.connect(lambda: self.hlpl_hide_show_2('hlpl_message'))

        self.pushButton_16.pressed.connect(lambda: self.hlpl_hide_show_2('home'))
        self.pushButton_13.pressed.connect(lambda: self.hlpl_hide_show_2('home')) 
        self.hlpl_settings() 
        
        
        self.checkBox.stateChanged.connect(lambda: self.hlpl_checkbox('1')) 
        self.checkBox_2.stateChanged.connect(lambda: self.hlpl_checkbox('2'))  


        self.pushButton_11.pressed.connect(lambda: self.hlpl_dirs('pushButton_11'))
        self.actionWords_templates_database.triggered.connect(lambda: self.hlpl_dirs('pushButton_11')) 
        self.actionWords_templates_database_2.triggered.connect(lambda: self.hlpl_dirs('pushButton_11'))  
        
        self.pushButton_12.pressed.connect(lambda: self.hlpl_dirs('pushButton_12'))
        self.actionWords_synonyme_antonyme_database.triggered.connect(lambda: self.hlpl_dirs('pushButton_12'))
        self.actionWords_synonyme_antonyme_database_2.triggered.connect(lambda: self.hlpl_dirs('pushButton_12'))
        
        
        self.pushButton_14.pressed.connect(lambda: self.hlpl_dirs('delete_messages')) 

        
        self.templates_dct={} 
        self.TXT=QTextEdit()   
        self.lt1=8; self.lt2=8;self.lt3=8;self.lt4=8 
        self.lt11=QTextEdit(); self.lt22=QTextEdit();self.lt33=QTextEdit();self.lt44=QTextEdit()
        self.comboBox.currentIndexChanged[str].connect(lambda s: self.hlpl_lt_font_size(1,s))
        self.comboBox_2.currentIndexChanged[str].connect(lambda s: self.hlpl_lt_font_size(3,s))
        self.comboBox_3.currentIndexChanged[str].connect(lambda s: self.hlpl_lt_font_size(2,s))
        self.comboBox_4.currentIndexChanged[str].connect(lambda s: self.hlpl_lt_font_size(4,s))
        
        self.fonttext=QTextEdit() 
        self.fontComboBox.currentFontChanged.connect(self.lt11.setCurrentFont)
        
        self.pushButton_18.pressed.connect(lambda: self.hlpl_grapgs_signals('textedit'))
        self.pushButton_19.pressed.connect(lambda: self.hlpl_grapgs_signals('else'))
        self.pushButton_20.pressed.connect(lambda: self.hlpl_grapgs_signals('else'))
        self.actionAbout.triggered.connect(self.hlpl_about)
        self.dct_x_y={}
        self.iii=0
        
        
        
        self.frame_5.hide()
        self.hlpl_check_messages()
        self.old_message=""
        
        self.templates_dict={}
        self.templates_dict2={}
        
        
        
        

        self.hlpl_language_layout_2()
        
        self.hlpl_grapgs_signals('textedit')
        self.hlpl_language()
        self.wdx=8
        
        self.pushButton_6.pressed.connect(lambda: self.hlpl_add_remove_sa('2',self.lineEdit_2))
        self.pushButton_5.pressed.connect(lambda: self.hlpl_add_remove_sa('0',self.lineEdit))
        self.pushButton_9.pressed.connect(lambda: self.hlpl_add_remove_sa('5',self.lineEdit_5))
        self.pushButton_10.pressed.connect(lambda: self.hlpl_add_remove_sa('6',self.lineEdit_6))
        self.current_word_a='' ; self.current_word_s=''        
        # end --------------------------------

    def hlpl_get_sa_get_st(self,cur,wd,wd2,taple,col,case,case2):
              st2='  ,  '
              if case=='s':
                 lst=cur.execute('SELECT * FROM '+taple+' WHERE '+col+'="'+wd+'"').fetchone()[1].split(st2)
              else:
                 lst=cur.execute('SELECT * FROM '+taple+' WHERE '+col+'="'+wd+'"').fetchone()[2].split(st2)                 
              st3=''
              if case2=='rem':
                 for x in lst:
                  if x!=wd2:
                     st3+=x+st2
              if case2=='add':
                 for x in lst:
                     st3+=x+st2
                 st3+=wd2+st2 
              st3=st3[0:len(st3)-len(st2)]
              return st3  
             
              
    def hlpl_add_remove_sa(self,c,le):
        wd2=le.text().split()[0] ; wd=self.current_word_s ; wd3=self.current_word_a ; dct={'0':'add','2':'rem','5':'add','6':'rem',}
        conn = sqlite3.connect(self.lineEdit_8.text()) ; cur = conn.cursor()
        if c in ['2','0']:
           if self.checkBox.isChecked() ==True:
              try:
                 st=self.hlpl_get_sa_get_st(cur,wd,wd2,'noun_sa','الاسم','s',dct[c])
                 cur.execute('UPDATE noun_sa SET مرادفات="'+st+'" WHERE الاسم="'+wd+'"')
                 conn.commit()
                 conn.close()
              except:
                 pass
                 
              try:
                 st=self.hlpl_get_sa_get_st(cur,wd,wd2,'verb_sa','الفعل','s',dct[c])
                 cur.execute('UPDATE verb_sa SET مرادفات="'+st+'" WHERE الفعل="'+wd+'"')
                 conn.commit()
                 conn.close()
              except:
                 pass              
           else:
              try:
                 st=self.hlpl_get_sa_get_st(cur,wd,wd2,'word_sa','word','s',dct[c])
                 cur.execute('UPDATE word_sa SET synonyme="'+st+'" WHERE word="'+wd+'"')
                 conn.commit()
                 conn.close()
              except:
                 pass 
              
        if c in ['5','6']:
           if self.checkBox.isChecked() ==True:
              try:
                 st=self.hlpl_get_sa_get_st(cur,wd3,wd2,'noun_sa','الاسم','a',dct[c])
                 cur.execute('UPDATE noun_sa SET أضداد="'+st+'" WHERE الاسم="'+wd3+'"')
                 conn.commit()
                 conn.close()
              except:
                 pass
                 
              try:
                 st=self.hlpl_get_sa_get_st(cur,wd3,wd2,'verb_sa','الفعل','a',dct[c])
                 cur.execute('UPDATE verb_sa SET أضداد="'+st+'" WHERE الفعل="'+wd3+'"')
                 conn.commit()
                 conn.close()
              except: 
                 pass              
           else:
              try:
                 st=self.hlpl_get_sa_get_st(cur,wd3,wd2,'word_sa','word','a',dct[c])
                 cur.execute('UPDATE word_sa SET antonyme="'+st+'" WHERE word="'+wd3+'"')
                 conn.commit()
                 conn.close()
              except:
                 pass       

    def hlpl_language_layout_2(self):
        if self.checkBox.isChecked()==True:
           self.hlpl_language_layout('ar',[self.textEdit,self.textEdit_2,self.textEdit_3,self.textEdit_4,self.textEdit_6,self.textEdit_8,])
        if self.checkBox_2.isChecked()==True:
           self.hlpl_language_layout('en',[self.textEdit,self.textEdit_2,self.textEdit_3,self.textEdit_4,self.textEdit_6,self.textEdit_8,])        

    
    language=True
    def hlpl_language(self):
        Ui_Notepad.language=self.checkBox.isChecked()      
        
    def hlpl_language_layout(self,case,lst):
        _translate = QtCore.QCoreApplication.translate
        st1='أدخل نصوص هنا واستخرج نصوص مشابهة ومعاكسة'
        st2='Write texts here and extract alike and opposit texts'
        if case in ['ar',]:
           for x in lst:
              if x==self.textEdit:
               x.setHtml(_translate("Notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; qt-block-indent:0; text-indent:0px; font-size:8.07477pt;\"><br />"+st1+"</p></body></html>"))
              else:
               pass
                
        if case in ['en',]:
           for x in lst:
              if x==self.textEdit:
               x.setHtml(_translate("Notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"left\" dir=\'ltr\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; qt-block-indent:0; text-indent:0px; font-size:8.07477pt;\"><br />"+st2+"</p></body></html>"))
              else:
               pass
 

    def hlpl_checkbox(self,case):
        if case=='1':
          if self.checkBox.isChecked()==True:
           self.checkBox_2.setChecked(False)
           self.hlpl_dirs('ar')
           self.hlpl_language_layout_2()
           self.hlpl_grapgs_signals('textedit')
           self.hlpl_language() 
           self.dialog_warning('Please review databases by replacing them with other English ones if they are already Arabic')          
        if case=='2':
          if self.checkBox_2.isChecked()==True:
           self.checkBox.setChecked(False)
           self.hlpl_dirs('en')
           self.hlpl_language_layout_2()
           self.hlpl_grapgs_signals('textedit')
           self.hlpl_language()
           self.dialog_warning('Please review databases by replacing them with other English ones if they are already Arabic')           
           
        if case=='3':
          if self.checkBox_3.isChecked()==True:
           self.checkBox_4.setChecked(False)
           self.hlpl_dirs('no')
        if case=='4':
          if self.checkBox_4.isChecked()==True:
           self.checkBox_3.setChecked(False)
           self.hlpl_dirs('yes')                    
               
 
    def hlpl_direct_link(self,url):
        webbrowser.open(str(url.toString()))
        
        
    def hlpl_table_format(self):
        header = self.tableWidget_2.horizontalHeader()
        header.setSectionResizeMode(QHeaderView.ResizeToContents)


    def hlpl_check_messages(self):
        import requests
        try:
           r = requests.get("https://hlpl.net/message/message.html")
           html=r.text
           dirx=os.path.dirname(sfd.__file__);st1=os.path.join(dirx,'new.html');st2=os.path.join(dirx,'old.html');st3=os.path.join(dirx,'static.html')
           f=open(st1,'r')
           f2=open(st2,'r')
           f3=open(st3,'r')
           html_old=f.read()
           html_old2=f2.read()
           html_old3=f3.read()
           f.close();f2.close()
           if len(html)!=len(html_old) and len(html)!=0:
              _translate = QtCore.QCoreApplication.translate
              self.textEdit_10.setHtml(_translate("Notepad",html))
              f=open(st1,'w')
              f2=open(st2,'w')
              x0='<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:"MS Shell Dlg 2"; font-size:8.25pt; font-weight:400; font-style:normal;"><p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p><p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:12pt; font-weight:600;">------------------------- End Message ------------------------------</span></p></body></html>'  
              html2=html+x0+html_old2
              f.write(html)
              f2.write(html2)
              f.close()
              f2.close()

              icon41 = QtGui.QIcon()
              dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"ni2.png")
              icon41.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)
              self.actionMessages_2.setIcon(icon41)

           if len(self.textEdit_10.toPlainText())==0:
              _translate = QtCore.QCoreApplication.translate
              self.textEdit_10.setHtml(_translate("Notepad",html_old3))   
              
        except:  
              pass         
              
              
           
        
        

    def hlpl_internet_con(self,case):
        import requests
        url = "https://hlpl.net/"
        timeout = 1
        try:
            request = requests.get(url, timeout=timeout)
            return True
            
        except:
            return False
            

    #---------------------------------------------------------------
    def hlpl_txt_to_lst(self,txt):
        lst=[]
        for x in txt:
            lst.append(x)
        return lst
    
    def hlpl_elements(self,lst,lst1):
        lst2=[]
        for x in lst:
            if x not in lst2 and x in lst1:
               lst2.append(x)
        return lst2
 

    def hlpl_all_elements_2(self,lst):
        lst2=[]
        for x in lst:
            for x2 in x.split(' - '):
                lst2.append(x2)
        return lst2
        
        
        
 
    def hlpl_all_elements(self,case): 
        conn = sqlite3.connect(self.lineEdit_7.text())
        conn.row_factory = lambda cursor, row: row[1]
        cur = conn.cursor();dct={'en':{'ns':[],'np':[],'adj':[],'adv':[],'art':[]},'ar':{'ns':[],'np':[],'adj':[],'adv':[]}}
        if case=='ar':
           dct['ar']['art']=cur.execute("SELECT * FROM ar_articles_lst").fetchall()
           dct['ar']['n']=cur.execute("SELECT * FROM ar_nouns_lst").fetchall()
           dct['ar']['v']=cur.execute("SELECT * FROM ar_verbs_lst").fetchall()

           dct['ar']['art']=self.hlpl_all_elements_2(dct['ar']['art'])
           dct['ar']['n']=self.hlpl_all_elements_2(dct['ar']['n'])
           dct['ar']['v']=self.hlpl_all_elements_2(dct['ar']['v'])
           
           return dct           
        
        if case=='en':
           dct['en']['art']=cur.execute("SELECT * FROM en_articles_lst").fetchall()
           dct['en']['adj']=cur.execute("SELECT * FROM en_adj_lst").fetchall()
           dct['en']['adv']=cur.execute("SELECT * FROM en_adv_lst").fetchall()
           dct['en']['ns']=cur.execute("SELECT * FROM en_nouns_s_lst").fetchall()
           dct['en']['sp']=cur.execute("SELECT * FROM en_nouns_p_lst").fetchall()  
           dct['en']['v']=cur.execute("SELECT * FROM en_verbs_lst").fetchall()

           dct['en']['art']=self.hlpl_all_elements_2(dct['en']['art'])
           dct['en']['adj']=self.hlpl_all_elements_2(dct['en']['adj'])
           dct['en']['adv']=self.hlpl_all_elements_2(dct['en']['adv'])
           dct['en']['ns']=self.hlpl_all_elements_2(dct['en']['ns'])
           dct['en']['sp']=self.hlpl_all_elements_2(dct['en']['sp'])
           dct['en']['v']=self.hlpl_all_elements_2(dct['en']['v'])
           
           return dct             
                  
 
 
    def hlpl_distance_order(self,case0,h,case,txt,txtedit):
        try:
          for i in reversed(range(getattr(self, 'layout'+'%s' % h).count())): 
            getattr(self, 'layout'+'%s' % h).itemAt(i).widget().setParent(None)
        except:
            pass
         
        exec('self.hlpl_figure'+str(h)+' = Figure()\nself.hlpl_canvas'+str(h)+' = FigureCanvas(self.hlpl_figure'+str(h)+')\nself.hlpl_toolbar'+str(h)+' = NavigationToolbar(self.hlpl_canvas'+str(h)+', None)\nself.layout'+str(h)+'.addWidget(self.hlpl_toolbar'+str(h)+')\nself.layout'+str(h)+'.addWidget(self.hlpl_canvas'+str(h)+')')
            
        dct={};lst=[];lst0=[]
        if self.checkBox.isChecked()==True:
         if case=='letters':
           lst=self.hlpl_txt_to_lst(txt)
           lst0=ar
         else:
           txt=hlpl_remover(txt,['[',']'])
           lst=txt.split()
           if case in ['12','16']:
              lst_art=self.hlpl_all_elements('ar')['ar']['art']
              lst0=self.hlpl_elements(lst,lst_art)
           if case in ['13','17']:
              lst_n=self.hlpl_all_elements('ar')['ar']['n']
              lst0=self.hlpl_elements(lst,lst_n)      
           if case in ['14','18']:
              lst_v=self.hlpl_all_elements('ar')['ar']['v']
              lst0=self.hlpl_elements(lst,lst_v)
 
        else:  
         if case=='letters':
           lst=self.hlpl_txt_to_lst(txt)
           lst0=en 
         else:
           txt=hlpl_remover(txt,['[',']'])
           lst=txt.split()
           if case in ['12','16']:
              lst_art=self.hlpl_all_elements('en')['en']['art']
              lst0=self.hlpl_elements(lst,lst_art)
           if case in ['13','17']:
              lst_n=self.hlpl_all_elements('en')['en']['ns']+self.hlpl_all_elements('en')['en']['np']+self.hlpl_all_elements('en')['en']['adj']+self.hlpl_all_elements('en')['en']['adv']
              lst0=self.hlpl_elements(lst,lst_n)      
           if case in ['14','18']:
              lst_v=self.hlpl_all_elements('en')['en']['v']
              lst0=self.hlpl_elements(lst,lst_v)             


        for r in range(len(lst0)):
            x=lst0[r]
            rd=[];o=[];cd=[];k=1
            for i in range(len(lst)):
                if x==lst[i]:
                   o.append(i+1)
                   rd.append(k);k+=1
            for m in range(1,len(rd)):
                cd.append(rd[m]-rd[m-1])
            dct[x]=[o,rd,cd]
            self.dct_x_y[str(h)+str(r)]=[o,rd,cd]
            
        
        lst2=list(dct.keys())
        for i in range(len(lst2)):
            wd=QFontMetrics(QFont("Arial",self.lt4)).width(lst2[i])
            exec('self.plot_'+str(h)+str(i)+' = QPushButton("'+lst2[i]+'")\nself.plot_'+str(h)+str(i)+'.setMinimumSize(QSize('+str(wd+16)+', 21))\nself.plot_'+str(h)+str(i)+'.setMaximumSize(QSize('+str(wd+16)+', 21))')

        for i in range(len(lst2)):  
            exec('self.layout'+str(h)+'.addWidget(self.plot_'+str(h)+str(i)+')')
        
        for n in range(len(lst2)):
            getattr(self, 'plot_'+str(h)+'%s' % n).pressed.connect(lambda v=str(h)+str(n): self.hlpl_plot(v,getattr(self, 'hlpl_canvas'+'%s' % h),getattr(self, 'hlpl_figure'+'%s' % h)))
        

    

    def hlpl_lt_font_size(self,n,s):
        if n==1:
           self.lt1=s
        if n==2:
           self.lt2=s
        if n==3:
           self.lt3=s
        if n==4:
           self.lt4=s     
    def hlpl_lt_font_type(self,n,s):
        if n==1:
           self.lt1=s
        if n==2:
           self.lt2=s
        if n==3:
           self.lt3=s
        if n==4:
           self.lt4=s 
           
    
    def hlpl_file_print(self,txt):
        self.TXT.setText(txt)
        self.file_print()
    
    def file_print(self):
        dlg = QPrintDialog()
        if dlg.exec_():
            self.TXT.print_(dlg.printer())
            
    def hlpl_inject_template(self,txt0,target):
        db=self.lineEdit_7.text();conn=sqlite3.connect(db);cur = conn.cursor() 
        if self.checkBox.isChecked()==True:
           dct,txt1=hlpl_arabic_phrase_template(txt0,cur)
           target.setText(txt1)
           self.hlpl_fill_templates_dct(dct)
        else:
           dct,txt1=hlpl_english_phrase_template(txt0,cur)
           target.setText(txt1)
           self.hlpl_fill_templates_dct(dct)
    
    def hlpl_fill_templates_dct(self,dct):
        for x in dct.keys():
            self.templates_dct[x]=dct[x]     
      
    def hlpl_info_saved(self,msg2):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Information)
        msg.setText(msg2)
        msg.setWindowTitle("HLPL message")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
                      
            

    def hlpl_dirs(self,case,html=""):
          if case=='delete_messages':
              x0='<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd"><html><head><meta name="qrichtext" content="1" /><style type="text/css">p, li { white-space: pre-wrap; }</style></head><body style=" font-family:"MS Shell Dlg 2"; font-size:8.25pt; font-weight:400; font-style:normal;"><p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p><p align="center" style="-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><br /></p><p align="center" style=" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-size:16pt; font-weight:600;">No messages found!</span></p></body></html>'            
              _translate = QtCore.QCoreApplication.translate
              dirx=os.path.dirname(sfd.__file__);st1=os.path.join(dirx,'new.html');st2=os.path.join(dirx,'old.html')
              f2=open(st2,'w')
              self.textEdit_19.setHtml(_translate("Notepad",x0))
              f2.write(x0)
              f2.close()
            
            
            
          if case=='pushButton_11':
            txt1 = QFileDialog.getOpenFileName(None, 'Open a file', '','Database files (*.db)')[0]
            if '.db' in txt1:           
               self.lineEdit_7.setText(txt1)
               txt1='"'+txt1+'"'
               hlpl_settings_insert('hlpl_1',txt1) 
               
          if case=='pushButton_12':
            txt2 = QFileDialog.getOpenFileName(None, 'Open a file', '','Database files (*.db)')[0]  
            if '.db' in txt2:                    
               self.lineEdit_8.setText(txt2)
               txt2='"'+txt2+'"'
               hlpl_settings_insert('hlpl_2',txt2)
            
                     
          
          """ 
          if case=='spinBox':
            txt3 = self.spinBox.value()
            txt3='"'+str(txt3)+'"'
            hlpl_settings_insert('spinBox',txt3) """             
                
          if case=='en':
            hlpl_settings_insert('hlpl_3','"en"')
          if case=='ar':
            hlpl_settings_insert('hlpl_3','"ar"')

          if case=='yes':
            hlpl_settings_insert('hlpl_4','"yes"')
          if case=='no':
            hlpl_settings_insert('hlpl_4','"no"') 


    def hlpl_settings(self): 
        _translate = QtCore.QCoreApplication.translate
        dirx=os.path.dirname(sfd.__file__);st1=os.path.join(dirx,'new.html');st2=os.path.join(dirx,'old.html')
        diry=os.path.dirname(sfd3.__file__);st3=os.path.join(diry,'hlpl_arabic_words_synonym_antonym.db');st4=os.path.join(diry,'hlpl_arabic_words_templates.db')
        f=open(st1,'r')
        f2=open(st2,'r')
        html_old=f.read()
        html_old2=f2.read()
        f.close();f2.close()
        self.textEdit_10.setHtml(_translate("Notepad",html_old))
        self.textEdit_19.setHtml(_translate("Notepad",html_old2)) 

        
        try:
           txt1=hlpl_settings_import('hlpl_1')[0] 
        except:
           txt1=st4
        self.lineEdit_7.setText(txt1)

        try:
           txt2=hlpl_settings_import('hlpl_2')[0] 
        except:
           txt2=st3
        self.lineEdit_8.setText(txt2)
        
        try:
           st=hlpl_settings_import('hlpl_3')[0] 
        except:
           st='ar'
        if st=='en':
           self.checkBox_2.setChecked(True)
           self.checkBox.setChecked(False)
           
        else:
           self.checkBox.setChecked(True)
           self.checkBox_2.setChecked(False)
         

        """         
        try:
           st8=hlpl_settings_import('hlpl_4')[0] 
        except:
           st8='no'
        if st8=='no':
           self.checkBox_3.setChecked(True)
           self.checkBox_4.setChecked(False)
        else:
           self.checkBox_4.setChecked(True)
           self.checkBox_3.setChecked(False)           
      
        
        try:
           spinBox=hlpl_settings_import('spinBox')[0] 
        except:
           spinBox='8'  
           
        self.lineEdit_2.setText( my_dir1)

        self.spinBox.setValue(int(spinBox))"""

        
    def hlpl_hide_show_2(self,case): 
        if case=='hlpl_account':
           hlpl_hide_show([self.frame_6],[self.frame,self.frame_2,self.frame_3,self.frame_4,self.frame_5])    
        if case=='hlpl_setting':
           self.action_30.setChecked(False)
           self.action_35.setChecked(False) 
           hlpl_hide_show([self.frame_4],[self.frame,self.frame_2,self.frame_3,self.frame_5])           
        if case=='hlpl_message':
           self.action_30.setChecked(False)
           self.action_35.setChecked(False)
           hlpl_hide_show([self.frame_5],[self.frame,self.frame_2,self.frame_3,self.frame_4])

        if case=='home':
           self.action_30.setChecked(False)
           self.action_35.setChecked(False)
           hlpl_hide_show([self.frame],[self.frame_5,self.frame_2,self.frame_3,self.frame_4])
                      
        if case=='actionStart_conversation_2':
           hlpl_hide_show([self.frame],[self.frame_3,self.frame_4,self.frame_20])
           
           
    def hlpl_about(self):
        dlg = AboutDialog()
        dlg.exec_()
    def hlpl_license(self):
        dlg = LicenseDialog()
        dlg.exec_()
    def hlpl_guide(self):
         webbrowser.open('https://docs.hlpl.net') 
    def hlpl_close(self):
        sys.exit(app.exec_())
    def hlpl_Forum(self):
         webbrowser.open('https://hlpl.net/forums/hlpl-composer/')     
    def hlpl_restart(self):
        QtCore.QCoreApplication.quit()
        status = QtCore.QProcess.startDetached(sys.executable, sys.argv)    

                
    
    import datetime
    def hlpl_grapgs_signals(self,case):
          if case=='textedit':
           if self.checkBox.isChecked()==True:
              self.hlpl_letters_status('ar')
              self.hlpl_distance_order('ar',9,'letters',self.textEdit.toPlainText(),self.textEdit_9)
              try:
                 self.hlpl_inject_template(self.textEdit.toPlainText(),self.textEdit_2)
              except:
                 self.textEdit_2.setText('Tamplates have not been generated due to an error in databases!... please verify it in settings.')
           else:
              self.hlpl_letters_status('en')
              self.hlpl_distance_order('en',9,'letters',self.textEdit.toPlainText(),self.textEdit_9) 
              try:
                 self.hlpl_inject_template(self.textEdit.toPlainText(),self.textEdit_2) 
              except:
                 self.textEdit_2.setText('Tamplates have not been generated due to an eroor in databases!... please verify it in settings.')              
              
          if case=='else':
             self.hlpl_distance_order('ar',12,'12',self.hlpl_pbs_txt('1'),self.textEdit_12)
             self.hlpl_distance_order('ar',13,'13',self.hlpl_pbs_txt('1'),self.textEdit_13)
             self.hlpl_distance_order('ar',14,'14',self.hlpl_pbs_txt('1'),self.textEdit_14)

             self.hlpl_distance_order('ar',16,'16',self.hlpl_pbs_txt('2'),self.textEdit_16)
             self.hlpl_distance_order('ar',17,'17',self.hlpl_pbs_txt('2'),self.textEdit_17)
             self.hlpl_distance_order('ar',18,'18',self.hlpl_pbs_txt('2'),self.textEdit_18)
 
 
    def hlpl_pbs_txt(self,c):
       if c=='1':
        txt=''
        for i in range(self.flowLayout3.count()): 
               txt+=self.flowLayout3.itemAt(i).widget().text()+' ' 
        return txt    
        
       if c=='2':
        txt=''
        for i in range(self.flowLayout4.count()): 
               txt+=self.flowLayout4.itemAt(i).widget().text()+' ' 
        return txt  
 
    def hlpl_letters_status(self,case):
        st1=self.textEdit.toPlainText()
        st2='';lst=[];st1_len=len(st1);lst_pie=[];lst_ae=[]
        if case=='ar':
           lst_ae=ar
           for x in ar:
               w1='(';w2=')';w3=(st1.count(x)/st1_len)*100;w3="%.2f" % round(w3, 2)
               lst.append(w1+x+': '+str(w3)+w2)
               lst_pie.append(st1.count(x))
        else:
           lst_ae=en
           for x in en:
               w1='(';w2=')';w3=((st1.count(x.lower())+st1.count(x.upper()))/st1_len)*100;w3="%.2f" % round(w3, 2)
               lst.append(w1+x+': '+str(w3)+w2)
               lst_pie.append(st1.count(x.lower())+st1.count(x.upper()))               
               
        for x in lst:
               st2+=x+'  -  '
        st2=st2[0:len(st2)-len('  -  ')]
        self.textEdit_5.setText(st2)
        h=11
        try:
          for i in reversed(range(self.layout11.count())): 
            getattr(self, 'layout'+'%s' % h).itemAt(i).widget().setParent(None)
        except:
            pass
        exec('self.hlpl_figure'+str(h)+' = Figure()\nself.hlpl_canvas'+str(h)+' = FigureCanvas(self.hlpl_figure'+str(h)+')\nself.hlpl_toolbar'+str(h)+' = NavigationToolbar(self.hlpl_canvas'+str(h)+', None)\nself.layout'+str(h)+'.addWidget(self.hlpl_toolbar'+str(h)+')\nself.layout'+str(h)+'.addWidget(self.hlpl_canvas'+str(h)+')')
        self.hlpl_pie(lst_pie,lst_ae,self.hlpl_canvas11,self.hlpl_figure11)
 
 
    def hlpl_plot(self,v,canvass,fig):
        x,y=self.dct_x_y[v][0],self.dct_x_y[v][1]
        ax=fig.add_subplot(1,1,1)
        ax.clear()
        xx=ax.plot(x,y, '*-')
        fig.tight_layout()
        canvass.draw() 

    def hlpl_pie(self,x,y,canvass,fig,case='pie'):
        lst1,lst2=[],[]
        for i in range(len(x)):
            if x[i]!=0:
               lst1.append(x[i]);lst2.append(y[i])
        ax = fig.subplots()
        ax.clear()
        if case=='hist':
         ax.hist(x)
         rects = ax.patches
         labels = ['ت' for i in range(len(rects))]
         for rect, label in zip(rects, labels):
            height = rect.get_height()
            ax.text(rect.get_x() + rect.get_width() / 2, height+0.01, label,
            ha='center', va='bottom')
        else:
         xx=ax.pie(lst1, labels = lst2)
         #ax.set_title('Survery responses')
        fig.tight_layout()
        canvass.show() 
        
        

#--------------------------------------------    
    
    def hlpl_save_activated_sa(self,layout,case):
        txt=''
        for i in range(layout.count()): 
               txt+=layout.itemAt(i).widget().text()+' ' 
        if case=='save':  
           TXT=QTextEdit();TXT.setText(txt)        
           self.file_saveas(TXT,'save as')
        if case=='print':
           self.hlpl_file_print(txt)
           
    
    def hlpl_change_string(self,lst,n,txtedit):
        st=''
        for x in range(n,len(lst)):
            st+=lst[x]+'   '
        for x in range(0,n):
            st+=lst[x]+'   '
        txtedit.setText(st)           
 
    def hlpl_tuplet(self,tp):
        lsts,lsta,wd=[],[],''
        for x in tp:
            lst1=x[1].split(',');lst2=x[2].split(',');wd=x[0]
            for y in lst1:    
                if y not in lsts:
                   lsts.append(y)
            for y in lst2:    
                if y not in lsta:
                   lsta.append(y)            
        return wd,lsts,lsta
        
        
    def hlpl_remove_repited(self,lst,lst2):
        for x in lst:
            if x not in lst2:
               lst2.append(x)
        return lst2


    def hlpl_enlarge_dct(self,dct,wd):
        for i in range(len(dct[wd]['s'])):
            lstx=dct[wd]['s']
            w1=dct[wd]['s'][i]
            lsts=dct[wd]['s']
            lsta=[wd]
            
            if w1 in dct.keys():
               for x in lstx:
                   if x not in dct[w1]['s']:
                      dct[w1]['s'].append(x)
               for x in lsta:
                   if x not in dct[w1]['a']:
                      dct[w1]['a'].append(x)
            else:
               dct[w1]={'wd':w1,'s':lstx,'a':lsta}
 
        for i in range(len(dct[wd]['a'])):
            lstx=dct[wd]['a']
            w1=dct[wd]['a'][i]
            lsts=dct[wd]['a']
            lsta=[wd]
            
            if w1 in dct.keys():
               for x in lstx:
                   if x not in dct[w1]['s']:
                      dct[w1]['s'].append(x)
               for x in lsta:
                   if x not in dct[w1]['a']:
                      dct[w1]['a'].append(x)
            else:
               dct[w1]={'wd':w1,'s':lstx,'a':lsta}
        
        return dct
 
    def hlpl_enlarge_dct2(self,dct,wd):
       if self.checkBox.isChecked()==True: 
        for i in range(len(dct[wd]['n'])):
            lstx=dct[wd]['n']
            w1=dct[wd]['n'][i]
            if w1 in dct.keys():
               for x in lstx:
                   if x not in dct[w1]['n']:
                      dct[w1]['n'].append(x)
            else:
               dct[w1]={'a':dct[wd]['a'],'n':lstx,'v':[]} 

        for i in range(len(dct[wd]['v'])):
            lstx=dct[wd]['v']
            w1=dct[wd]['v'][i]
            if w1 in dct.keys():
               for x in lstx:
                   if x not in dct[w1]['v']:
                      dct[w1]['v'].append(x)
            else:
               dct[w1]={'a':dct[wd]['a'],'v':lstx,'n':[]}              
               
        return dct 
 
       else: 
        for i in range(len(dct[wd]['v'])):
            lstx=dct[wd]['v']
            w1=dct[wd]['v'][i]
            if w1 in dct.keys():
               for x in lstx:
                   if x not in dct[w1]['v']:
                      dct[w1]['v'].append(x)
            else:
               dct[w1]={'a':dct[wd]['a'],'v':lstx,'adv':[],'adj':[],'ns':[],'np':[]} 

        for i in range(len(dct[wd]['ns'])):
            lstx=dct[wd]['ns']
            w1=dct[wd]['ns'][i]
            if w1 in dct.keys():
               for x in lstx:
                   if x not in dct[w1]['ns']:
                      dct[w1]['ns'].append(x)
            else:
               dct[w1]={'a':dct[wd]['a'],'v':[],'adv':[],'adj':[],'ns':lstx,'np':[]} 

        for i in range(len(dct[wd]['np'])):
            lstx=dct[wd]['np']
            w1=dct[wd]['np'][i]
            if w1 in dct.keys():
               for x in lstx:
                   if x not in dct[w1]['np']:
                      dct[w1]['np'].append(x)
            else:
               dct[w1]={'a':dct[wd]['a'],'v':[],'adv':[],'adj':[],'ns':[],'np':lstx} 

        for i in range(len(dct[wd]['adv'])):
            lstx=dct[wd]['adv']
            w1=dct[wd]['adv'][i]
            if w1 in dct.keys():
               for x in lstx:
                   if x not in dct[w1]['adv']:
                      dct[w1]['adv'].append(x)
            else:
               dct[w1]={'a':dct[wd]['a'],'v':[],'adv':lstx,'adj':[],'ns':[],'np':[]} 

        for i in range(len(dct[wd]['adj'])):
            lstx=dct[wd]['adj']
            w1=dct[wd]['adj'][i]
            if w1 in dct.keys():
               for x in lstx:
                   if x not in dct[w1]['adj']:
                      dct[w1]['adj'].append(x)
            else:
               dct[w1]={'a':dct[wd]['a'],'v':[],'adv':[],'adj':lstx,'ns':[],'np':[]} 
        return dct 

    def hlpl_get_sa_dct(self,wd):
      if self.checkBox.isChecked()==True:
       if wd not in self.templates_dict.keys():
        conn = sqlite3.connect(self.lineEdit_8.text())
        cur = conn.cursor();dct={'s':[],'a':[]}
        wd='"'+wd+'"'
        row1=cur.execute("SELECT * FROM verb_sa WHERE الفعل="+wd).fetchall()
        row2=cur.execute("SELECT * FROM noun_sa WHERE الاسم="+wd).fetchall()
        wd,lsts1,lsta1=self.hlpl_tuplet(row1);wd,lsts2,lsta2=self.hlpl_tuplet(row2)
        lsts=self.hlpl_remove_repited(lsts1,lsts2);lsta=self.hlpl_remove_repited(lsta1,lsta2)
        dct={'wd':wd,'s':lsts2,'a':lsta2}
        self.templates_dict[wd]=dct
        self.templates_dict=self.hlpl_enlarge_dct(self.templates_dict,wd)
        return dct
       else:
        return self.templates_dict[wd]
      else:
       if wd not in self.templates_dict.keys():
        conn = sqlite3.connect(self.lineEdit_8.text())
        cur = conn.cursor();dct={'s':[],'a':[]}
        wd='"'+wd+'"'
        row=cur.execute("SELECT * FROM word_sa WHERE word="+wd).fetchall()
        wd,lsts,lsta=self.hlpl_tuplet(row)
        dct={'wd':wd,'s':lsts,'a':lsta}
        self.templates_dict[wd]=dct
        self.templates_dict=self.hlpl_enlarge_dct(self.templates_dict,wd)
        return dct
       else:
        return self.templates_dict[wd]       
        
    def hlpl_get_sat_dct(self,wd):
      if self.checkBox.isChecked()==True: 
       if wd not in self.templates_dict2.keys():
        conn = sqlite3.connect(self.lineEdit_7.text())
        cur = conn.cursor();dct={'a':[],'n':[],'v':[]}
        wd='"'+wd+'"'
        row1=cur.execute("SELECT * FROM ar_articles_lst WHERE word="+wd).fetchone()
        row2=cur.execute("SELECT * FROM ar_nouns_lst WHERE word="+wd).fetchone()
        row3=cur.execute("SELECT * FROM ar_verbs_lst WHERE word="+wd).fetchone()
        if row1!=None:
           dct['a']=row1[1].split('-')
        if row2!=None:
           dct['n']=row2[1].split('-')                 
        if row3!=None:
           dct['v']=row3[1].split('-')
        self.templates_dict2[wd]=dct
        self.templates_dict2=self.hlpl_enlarge_dct2(self.templates_dict2,wd)
        return dct
       else:
        return self.templates_dict2[wd]
        
      else:
       if wd not in self.templates_dict2.keys():
        conn = sqlite3.connect(self.lineEdit_7.text())
        cur = conn.cursor();dct={'a':[],'ns':[],'np':[],'adv':[],'adj':[],'v':[]}
        wd='"'+wd+'"'
        row1=cur.execute("SELECT * FROM en_articles_lst WHERE word="+wd).fetchone()
        row2=cur.execute("SELECT * FROM en_nouns_s_lst WHERE word="+wd).fetchone()
        row3=cur.execute("SELECT * FROM en_verbs_lst WHERE word="+wd).fetchone()
        row4=cur.execute("SELECT * FROM en_adj_lst WHERE word="+wd).fetchone()
        row5=cur.execute("SELECT * FROM en_nouns_p_lst WHERE word="+wd).fetchone()
        row6=cur.execute("SELECT * FROM en_adv_lst WHERE word="+wd).fetchone()
        
        if row1!=None:
           dct['a']=row1[1].split('-')
        if row2!=None:
           dct['ns']=row2[1].split('-')                 
        if row3!=None:
           dct['v']=row3[1].split('-')
        if row4!=None:
           dct['adj']=row4[1].split('-')
        if row5!=None:
           dct['np']=row5[1].split('-')                 
        if row6!=None:
           dct['adv']=row6[1].split('-')  
        
        self.templates_dict2[wd]=dct
        self.templates_dict2=self.hlpl_enlarge_dct2(self.templates_dict2,wd)
        
        return dct
       else:
        return self.templates_dict2[wd]       
        
        
    def hlpl_pb_layout(self,pb):
        if self.checkBox_2.isChecked()==False:
           pb.setStyleSheet("QPushButton { text-align: left; }")
        else:
           pb.setStyleSheet("QPushButton { text-align: right; }")        
        
    def hlpl_change_synonyme(self,pb):
        txt=self.hlpl_sa_lst[self.hlpl_sa_loop]
        pb.setText(txt)
        self.hlpl_pb_layout(pb)
        fontt=str(self.fontComboBox_3.currentText()) 
        fsize=int(str(self.comboBox.currentText()))     
        pb.setMinimumSize(QSize(QFontMetrics(QFont(fontt,fsize)).width(txt), 27))
        self.hlpl_change_string(self.hlpl_sa_lst,self.hlpl_sa_loop,self.lineEdit_3)
        if self.hlpl_sa_loop==len(self.hlpl_sa_lst)-1:
           self.hlpl_sa_loop=-1 
    def input_number(self, v):
      x0=getattr(self, 'pushButton81_%s' % v); x=x0.text()
      if self.hlpl_sa_loop_pb==v:
        self.hlpl_sa_loop+=1
        self.hlpl_change_synonyme(x0)
        self.hlpl_inject_template_data('1')
        txtt=self.hlpl_inject_template_data2('1')
        
      else:
        lst=[x];x2=''; self.current_word_s=x
        www=self.hlpl_get_sa_dct(x)
        if www!=None:
           x1=www['s']
           for y in x1:
               x2+=y+'   ';lst.append(y)
        
        self.lineEdit_3.setText(x2)
        self.hlpl_inject_template_data('1')         
           
        self.hlpl_sa_loop_pb=v      
        self.hlpl_sa_loop=-1
        self.hlpl_sa_lst=lst
        self.hlpl_sa_st=x2
        self.input_number(v)


    def hlpl_change_synonyme2(self,pb):
        txt=self.hlpl_sa2_lst[self.hlpl_sa2_loop]
        pb.setText(txt)
        self.hlpl_pb_layout(pb)
        fontt=str(self.fontComboBox_4.currentText())
        fsize=int(str(self.comboBox_2.currentText()))        
        pb.setMaximumSize(QSize(QFontMetrics(QFont('"'+fontt+'"',fsize)).width(txt), 27))
        self.hlpl_change_string(self.hlpl_sa2_lst,self.hlpl_sa2_loop,self.textEdit_7)
        if self.hlpl_sa2_loop==len(self.hlpl_sa2_lst)-1:
           self.hlpl_sa2_loop=-1    
    def hlpl_input_number_2(self, v):
      x0=getattr(self, 'pushButton83_%s' % v); x=x0.text()
      if self.hlpl_sa2_loop_pb==v:
        self.hlpl_sa2_loop+=1
        self.hlpl_change_synonyme2(x0)
        
      else:
        lst=[x];x2=''
        dct=self.hlpl_get_sat_dct(x)
        if dct['a']!=[]:
           x2=x
        else:
          if self.checkBox.isChecked()==True: 
           if dct['n']!=[]:
              for y in dct['n']:
                  x2+=y+'   ';lst.append(y)
           if dct['v']!=[]:
              for y in dct['v']:
                  x2+=y+'   ';lst.append(y)

          else:
           if dct['ns']!=[]:
              for y in dct['ns']:
                  x2+=y+'   ';lst.append(y)
           if dct['np']!=[]:
              for y in dct['np']:
                  x2+=y+'   ';lst.append(y)              
           if dct['adj']!=[]:
              for y in dct['adj']:
                  x2+=y+'   ';lst.append(y)
           if dct['adv']!=[]:
              for y in dct['adv']:
                  x2+=y+'   ';lst.append(y)   
           if dct['v']!=[]:
              for y in dct['v']:
                  x2+=y+'   ';lst.append(y)   
       
        self.textEdit_7.setText(x2) 
           
        self.hlpl_sa2_loop_pb=v      
        self.hlpl_sa2_loop=-1
        self.hlpl_sa2_lst=lst
        self.hlpl_sa2_st=x2
        self.hlpl_input_number_2(v)
        

    def hlpl_change_antonyme(self,pb):
        txt=self.hlpl_as_lst[self.hlpl_as_loop]
        pb.setText(txt)
        self.hlpl_pb_layout(pb)
        fontt=str(self.fontComboBox_5.currentText())
        fsize=int(str(self.comboBox_3.currentText()))         
        pb.setMaximumSize(QSize(QFontMetrics(QFont('"'+fontt+'"',fsize)).width(txt), 27))
        self.hlpl_change_string(self.hlpl_as_lst,self.hlpl_as_loop,self.lineEdit_4)
        if self.hlpl_as_loop==len(self.hlpl_as_lst)-1:
           self.hlpl_as_loop=-1
    def input_numberr(self, v):
      x0=getattr(self, 'pushButton82_%s' % v); x=x0.text()
      if self.hlpl_as_loop_pb==v:  
        self.hlpl_as_loop+=1   
        self.hlpl_change_antonyme(x0)
        self.hlpl_inject_template_data('2')
        
      else: 
        lst=[x];x2='' ; self.current_word_a=x
        www=self.hlpl_get_sa_dct(x)
        if www!=None:
           x1=www['a']
           for y in x1:
               x2+=y+'   ';lst.append(y)
               
        
        self.lineEdit_4.setText(x2)
        self.hlpl_inject_template_data('2')         
           
        self.hlpl_as_loop_pb=v      
        self.hlpl_as_loop=-1
        self.hlpl_as_lst=lst
        self.hlpl_as_st=x2
        self.input_numberr(v)        
        
        

    def hlpl_change_antonyme2(self,pb):
        txt=self.hlpl_as2_lst[self.hlpl_as2_loop]
        pb.setText(txt)
        self.hlpl_pb_layout(pb)
        fontt=str(self.fontComboBox_6.currentText()) 
        fsize=int(str(self.comboBox_4.currentText()))  
        pb.setMaximumSize(QSize(QFontMetrics(QFont('"'+fontt+'"',fsize)).width(txt), 27))
        self.hlpl_change_string(self.hlpl_as2_lst,self.hlpl_as2_loop,self.textEdit_15)
        if self.hlpl_as2_loop==len(self.hlpl_as2_lst)-1:
           self.hlpl_as2_loop=-1
    def input_numberr2(self, v):
      x0=getattr(self, 'pushButton84_%s' % v); x=x0.text()
      if self.hlpl_as2_loop_pb==v:
        self.hlpl_as2_loop+=1
        self.hlpl_change_antonyme2(x0)
        
      else: 
        lst=[x];x2=''
        dct=self.hlpl_get_sat_dct(x)
        if dct['a']!=[]:
           x2=x
        else:
          if self.checkBox.isChecked()==True: 
           if dct['n']!=[]:
              for y in dct['n']:
                  x2+=y+'   ';lst.append(y)
           if dct['v']!=[]:
              for y in dct['v']:
                  x2+=y+'   ';lst.append(y)               

          else: 
           if dct['ns']!=[]:
              for y in dct['ns']:
                  x2+=y+'   ';lst.append(y)
           if dct['np']!=[]:
              for y in dct['np']:
                  x2+=y+'   ';lst.append(y)              
           if dct['adj']!=[]:
              for y in dct['adj']:
                  x2+=y+'   ';lst.append(y)
           if dct['adv']!=[]:
              for y in dct['adv']:
                  x2+=y+'   ';lst.append(y)   
           if dct['v']!=[]:
              for y in dct['v']:
                  x2+=y+'   ';lst.append(y) 
                  
        self.textEdit_15.setText(x2)
           
        self.hlpl_as2_loop_pb=v      
        self.hlpl_as2_loop=-1
        self.hlpl_as2_lst=lst
        self.hlpl_as2_st=x2
        self.input_numberr2(v)   
        
  
        
    #\nself.pushButton81_'+str(i)+'.setLocale(QLocale(QLocale.Arabic, QLocale.Egypt))
    def activate_alike(self):
      if self.action_30.isChecked()==True:
        for i in reversed(range(self.flowLayout1.count())): 
            self.flowLayout1.itemAt(i).widget().setParent(None)
        
        dd=[] 
        rr={}
        dd=self.textEdit.toPlainText().split()
        fontt=str(self.fontComboBox_3.currentText())
        fsize=str(self.comboBox.currentText())        
        ddd=len(dd) 
        for x in dd:
            exec('rr[x]=QFontMetrics(QFont("'+fontt+'",'+str(self.lt1)+')).width(x)')
        rrm=max(rr.values())
        for i in range(ddd):
              exec('self.pushButton81_'+str(i)+'.setMinimumSize(QSize('+str(rr[dd[i]]+2*self.wdx)+', 27))\nself.pushButton81_'+str(i)+'.setMaximumSize(QSize('+str(rr[dd[i]]+2*self.wdx)+', 27))\nfont = QFont("'+fontt+'",'+fsize+')\nself.pushButton81_'+str(i)+'.setFont(font)\nself.pushButton81_'+str(i)+'.setFont(font)\nself.pushButton81_'+str(i)+'.setFlat(True)\nself.pushButton81_'+str(i)+'.setText(QCoreApplication.translate("Notepad", u"'+dd[i]+'", None))\n')
        for j in range(ddd): 
              exec('self.flowLayout1.addWidget(self.pushButton81_'+str(j)+')\n')
              
        self.hlpl_grapgs_signals('else')
                      

    def hlpl_get_template_text(self,txt):
        lst=txt.split();st=''
        for x in lst:
            try:
               st+=self.templates_dct[x].split(' - ')[0]+' '
            except:
                st+=x+' '
        return st
    
    
    def activate_alike2(self,txt):
      if self.action_30.isChecked()==True:
        for i in reversed(range(self.flowLayout3.count())): 
            self.flowLayout3.itemAt(i).widget().setParent(None)
        textt=self.hlpl_get_template_text(txt)
        dd=textt.split()
        rr={}
        ddd=len(dd) 
        fontt=str(self.fontComboBox_4.currentText())
        fsize=str(self.comboBox_2.currentText())         
        for x in dd:
            exec('rr[x]=QFontMetrics(QFont("Arial",'+str(self.lt3)+')).width(x)')
        rrm=max(rr.values())
        for i in range(ddd):
              exec('self.pushButton83_'+str(i)+'.setMinimumSize(QSize('+str(rr[dd[i]]+2*self.wdx)+', 27))\nself.pushButton83_'+str(i)+'.setMaximumSize(QSize('+str(rr[dd[i]]+2*self.wdx)+', 27))\nfont = QFont("'+fontt+'",'+fsize+')\nself.pushButton83_'+str(i)+'.setFont(font)\nself.pushButton83_'+str(i)+'.setFont(font)\nself.pushButton83_'+str(i)+'.setFlat(True)\nself.pushButton83_'+str(i)+'.setText(QCoreApplication.translate("Notepad", u"'+dd[i]+'", None))\n')
        for j in reversed(range(ddd)): 
              exec('self.flowLayout3.addWidget(self.pushButton83_'+str(j)+')\n')
              
        
    def activate_oposit(self):
      if self.action_35.isChecked()==True:
        for i in reversed(range(self.flowLayout2.count())): 
            self.flowLayout2.itemAt(i).widget().setParent(None)
        textt=self.textEdit.toPlainText()
        dd=textt.split()
        rr={}
        ddd=len(dd)
        fontt=str(self.fontComboBox_5.currentText())
        fsize=str(self.comboBox_3.currentText())          
        for x in dd:
            exec('rr[x]=QFontMetrics(QFont("Arial",'+str(self.lt2)+')).width(x)')
        rrm=max(rr.values()) 
        for i in range(ddd):
              exec('self.pushButton82_'+str(i)+'.setMinimumSize(QSize('+str(rr[dd[i]]+2*self.wdx)+', 27))\nself.pushButton82_'+str(i)+'.setMaximumSize(QSize('+str(rr[dd[i]]+2*self.wdx)+', 27))\nfont = QFont("'+fontt+'" ,'+fsize+')\nself.pushButton82_'+str(i)+'.setFont(font)\nself.pushButton82_'+str(i)+'.setFont(font)\nself.pushButton82_'+str(i)+'.setFlat(True)\nself.pushButton82_'+str(i)+'.setText(QCoreApplication.translate("Notepad", u"'+dd[i]+'", None))\n')
        for j in range(ddd): 
              exec('self.flowLayout2.addWidget(self.pushButton82_'+str(j)+')\n') 
        
        self.hlpl_grapgs_signals('else')

    def activate_oposit2(self,txt):
      if self.action_35.isChecked()==True:
        for i in reversed(range(self.flowLayout4.count())): 
            self.flowLayout4.itemAt(i).widget().setParent(None)
        textt=self.hlpl_get_template_text(txt)
        fontt=str(self.fontComboBox_6.currentText()) 
        fsize=str(self.comboBox_4.currentText())           
        dd=textt.split()
        rr={}
        ddd=len(dd)
        for x in dd:
            exec('rr[x]=QFontMetrics(QFont("Arial",'+str(self.lt4)+')).width(x)')
        rrm=max(rr.values())
        for i in range(ddd):
              exec('self.pushButton84_'+str(i)+'.setMinimumSize(QSize('+str(rr[dd[i]]+2*self.wdx)+', 27))\nself.pushButton84_'+str(i)+'.setMaximumSize(QSize('+str(rr[dd[i]]+2*self.wdx)+', 27))\nfont = QFont("'+fontt+'" ,'+fsize+')\nself.pushButton84_'+str(i)+'.setFont(font)\nself.pushButton84_'+str(i)+'.setFont(font)\nself.pushButton84_'+str(i)+'.setFlat(True)\nself.pushButton84_'+str(i)+'.setText(QCoreApplication.translate("Notepad", u"'+dd[i]+'", None))\n')
        for j in reversed(range(ddd)): 
              exec('self.flowLayout4.addWidget(self.pushButton84_'+str(j)+')\n') 

        
#--------------------------------------------------------------------------------------
                 
    #hlpl_hide_show([self.frame_4],[self.frame,self.frame_2,self.frame_3,self.frame_5])       
    def my_f1(self):

      text=self.textEdit.toPlainText()
      dd=text.split()
        
      if len(dd)>=1:
        x1=self.action_30.isChecked()
        x2=self.action_35.isChecked()      
      
        if x1==True:
           self.action_35.setChecked(False)        
           self.frame.hide()
           self.frame_3.hide()
           self.frame_4.hide()
           self.frame_5.hide()
           self.toolBar_3.hide()
           self.frame_2.show()
           
           
        if x1==False:
           self.frame.show()
           self.toolBar_3.show()
           self.frame_2.hide()
        
        if x1==True or x2==True:
           self.menu.setEnabled(False)
           self.menu_2.setEnabled(False)
        if x1==False and x2==False:
           self.menu.setEnabled(True)
           self.menu_2.setEnabled(True)
           
      else:
           self.action_30.setChecked(False)
      self.hlpl_inject_template_data('1')

   
    def hlpl_inject_template_data2(self,case):
        txt=''
        if case=='1':
           for i in reversed(range(self.flowLayout1.count())): 
               txt+=self.flowLayout1.itemAt(i).widget().text()+' '
           return txt         
        if case=='2':
           for i in reversed(range(self.flowLayout2.count())): 
               txt+=self.flowLayout2.itemAt(i).widget().text()+' '
           return txt     
           
      
    def hlpl_inject_template_data(self,case):
        txt=''
        if case=='1':
           for i in reversed(range(self.flowLayout1.count())): 
               txt+=self.flowLayout1.itemAt(i).widget().text()+' '
           self.activate_alike2(txt)            
        if case=='2':
           for i in reversed(range(self.flowLayout2.count())): 
               txt+=self.flowLayout2.itemAt(i).widget().text()+' '
           self.activate_oposit2(txt)              
    
           
    def my_f2(self):
      text=self.textEdit.toPlainText()
      dd=text.split()	
      
      if len(dd)>=1:
        x1=self.action_30.isChecked() 
        x2=self.action_35.isChecked()

        if x2==True:
           self.action_30.setChecked(False)        
           self.frame.hide()
           self.frame_2.hide()
           self.frame_4.hide()
           self.frame_5.hide()
           self.toolBar_3.hide()
           self.frame_3.show()
        if x2==False:
           self.frame.show()
           self.toolBar_3.show()
           self.frame_3.hide()           

        if x1==True or x2==True:
           self.menu.setEnabled(False)
           self.menu_2.setEnabled(False)
        if x1==False and x2==False:
           self.menu.setEnabled(True)
           self.menu_2.setEnabled(True)
                           

      else:
           self.action_35.setChecked(False) 
      self.hlpl_inject_template_data('2')     

    def my_f3(self,case):
        if case==True:          
           self.frame.hide()
           self.frame_3.hide()
           self.frame_2.hide()
           self.frame_4.show()
        if x1==False:
           self.frame.show()
           self.frame_4.hide()          



           
    def block_signals(self, objects, b):
        for o in objects:
            o.blockSignals(b)

    def update_format(self):
    
        self.block_signals(self._format_actions, True)

        self.action_24.setChecked(self.textEdit.fontItalic())
        self.action_27.setChecked(self.textEdit.fontWeight() == QFont.Bold)

        self.action_25.setChecked(self.textEdit.alignment() == Qt.AlignCenter)
        self.action_23.setChecked(self.textEdit.alignment() == Qt.AlignRight)
        self.action_26.setChecked(self.textEdit.alignment() == Qt.AlignJustify)

        self.block_signals(self._format_actions, False)

    def update_format2(self):

        self.block_signals(self._format_actions, True)

        self.action_29.setChecked(self.textEdit_2.fontItalic())
        self.action_38.setChecked(self.textEdit_2.fontUnderline())
        self.action_9.setChecked(self.textEdit_2.fontWeight() == QFont.Bold)

        self.action_21.setChecked(self.textEdit_2.alignment() == Qt.AlignCenter)
        self.action_20.setChecked(self.textEdit_2.alignment() == Qt.AlignRight)
        self.action_22.setChecked(self.textEdit_2.alignment() == Qt.AlignJustify)

        self.block_signals(self._format_actions, False)
       
     

    #-------------------------------------------
    def dialog_critical(self, s):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Critical)
        msg.setText(s)
        msg.setWindowTitle("HLPL message")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()

    def dialog_warning(self, s):
        msg = QMessageBox()
        msg.setIcon(QMessageBox.Warning)
        msg.setText(s)
        msg.setWindowTitle("HLPL message")
        msg.setStandardButtons(QMessageBox.Ok | QMessageBox.Cancel)
        retval = msg.exec_()
        
    def file_open(self,textarea,pathx):
        path, _ = QFileDialog.getOpenFileName(None, "Open file", "", "Text docs (*.txt)")
        with open(path, 'rU', encoding="utf8") as f:
                text = f.read()
                textarea.setText(text)


    def file_save(self,textarea,pathx):
        if pathx =='save as':
            return self.file_saveas(textarea,pathx)
        elif pathx ==self.textEdit_path and self.textEdit_path==None:
            return self.file_saveas(textarea,pathx)
        else:
            try:
               with open(pathx, 'w', encoding="utf8") as f:
                text = textarea.toPlainText()
                f.write(text)
            except Exception as e:
                self.dialog_critical(str(e))


    def file_saveas(self,textarea,pathx):
        path, _ = QFileDialog.getSaveFileName(None, "Save file", "", "Text (*.txt)")
        text=textarea.toPlainText()
        if not path:
            return
        with open(path, 'w', encoding="utf8") as f:
                f.write(text)
                if pathx ==self.textEdit_path and self.textEdit_path==None:
                   self.textEdit_path=path



    def update_title(self,pathx):
        self.setWindowTitle("%s - Megasolid Idiom" % (os.path.basename(pathx) if pathx else "Untitled"))

    def edit_toggle_wrap(self,txtarea):
        txtarea.setLineWrapMode( 1 if txtarea.lineWrapMode() == 0 else 0 )
    #---------------------------------------------    
        
        
        
        
        
        
        
        
        
    def my_clear1(self):
        self.textEdit.setHtml(QCoreApplication.translate("Notepad", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.07477pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.07477pt;\"><br /></p></body></html>", None))

    def my_clear2(self):
        self.textEdit_2.setHtml(QCoreApplication.translate("Notepad", u"<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:'MS Shell Dlg 2'; font-size:8.07477pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" dir='rtl' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.07477pt;\"><br /></p></body></html>", None))

    
   
   
   
    def retranslateUi(self, Notepad):
        _translate = QtCore.QCoreApplication.translate
        Notepad.setWindowTitle(_translate("Notepad", "HLPL Composer"))
        self.comboBox_8.setItemText(0, _translate("Notepad", "8"))
        self.comboBox_8.setItemText(1, _translate("Notepad", "9"))
        self.comboBox_8.setItemText(2, _translate("Notepad", "10"))
        self.comboBox_8.setItemText(3, _translate("Notepad", "11"))
        self.comboBox_8.setItemText(4, _translate("Notepad", "12"))
        self.comboBox_8.setItemText(5, _translate("Notepad", "14"))
        self.comboBox_8.setItemText(6, _translate("Notepad", "16"))
        self.comboBox_8.setItemText(7, _translate("Notepad", "18"))
        self.comboBox_8.setItemText(8, _translate("Notepad", "20"))
        self.comboBox_8.setItemText(9, _translate("Notepad", "22"))
        self.textEdit.setHtml(_translate("Notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.07477pt;\"><br /></p></body></html>"))
        self.comboBox_7.setItemText(0, _translate("Notepad", "8"))
        self.comboBox_7.setItemText(1, _translate("Notepad", "9"))
        self.comboBox_7.setItemText(2, _translate("Notepad", "10"))
        self.comboBox_7.setItemText(3, _translate("Notepad", "11"))
        self.comboBox_7.setItemText(4, _translate("Notepad", "12"))
        self.comboBox_7.setItemText(5, _translate("Notepad", "14"))
        self.comboBox_7.setItemText(6, _translate("Notepad", "16"))
        self.comboBox_7.setItemText(7, _translate("Notepad", "18"))
        self.comboBox_7.setItemText(8, _translate("Notepad", "20"))
        self.comboBox_7.setItemText(9, _translate("Notepad", "22"))
        self.pushButton_18.setText(_translate("Notepad", "Refresh"))
        self.textEdit_2.setHtml(_translate("Notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.07477pt;\"><br /></p></body></html>"))
        self.textEdit_5.setHtml(_translate("Notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.07477pt;\"><br /></p></body></html>"))
        self.comboBox.setItemText(0, _translate("Notepad", "8"))
        self.comboBox.setItemText(1, _translate("Notepad", "9"))
        self.comboBox.setItemText(2, _translate("Notepad", "10"))
        self.comboBox.setItemText(3, _translate("Notepad", "11"))
        self.comboBox.setItemText(4, _translate("Notepad", "12"))
        self.comboBox.setItemText(5, _translate("Notepad", "14"))
        self.comboBox.setItemText(6, _translate("Notepad", "16"))
        self.comboBox.setItemText(7, _translate("Notepad", "18"))
        self.comboBox.setItemText(8, _translate("Notepad", "20"))
        self.comboBox.setItemText(9, _translate("Notepad", "22"))
        self.textEdit_4.setHtml(_translate("Notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.07477pt;\"><br /></p></body></html>"))
        self.comboBox_2.setItemText(0, _translate("Notepad", "8"))
        self.comboBox_2.setItemText(1, _translate("Notepad", "9"))
        self.comboBox_2.setItemText(2, _translate("Notepad", "10"))
        self.comboBox_2.setItemText(3, _translate("Notepad", "11"))
        self.comboBox_2.setItemText(4, _translate("Notepad", "12"))
        self.comboBox_2.setItemText(5, _translate("Notepad", "14"))
        self.comboBox_2.setItemText(6, _translate("Notepad", "16"))
        self.comboBox_2.setItemText(7, _translate("Notepad", "18"))
        self.comboBox_2.setItemText(8, _translate("Notepad", "20"))
        self.comboBox_2.setItemText(9, _translate("Notepad", "22"))
        self.pushButton_19.setText(_translate("Notepad", "Refresh"))
        self.textEdit_3.setHtml(_translate("Notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.07477pt;\"><br /></p></body></html>"))
        self.comboBox_3.setItemText(0, _translate("Notepad", "8"))
        self.comboBox_3.setItemText(1, _translate("Notepad", "9"))
        self.comboBox_3.setItemText(2, _translate("Notepad", "10"))
        self.comboBox_3.setItemText(3, _translate("Notepad", "11"))
        self.comboBox_3.setItemText(4, _translate("Notepad", "12"))
        self.comboBox_3.setItemText(5, _translate("Notepad", "14"))
        self.comboBox_3.setItemText(6, _translate("Notepad", "16"))
        self.comboBox_3.setItemText(7, _translate("Notepad", "18"))
        self.comboBox_3.setItemText(8, _translate("Notepad", "20"))
        self.comboBox_3.setItemText(9, _translate("Notepad", "22"))
        self.textEdit_6.setHtml(_translate("Notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.07477pt;\"><br /></p></body></html>"))
        self.comboBox_4.setItemText(0, _translate("Notepad", "8"))
        self.comboBox_4.setItemText(1, _translate("Notepad", "9"))
        self.comboBox_4.setItemText(2, _translate("Notepad", "10"))
        self.comboBox_4.setItemText(3, _translate("Notepad", "11"))
        self.comboBox_4.setItemText(4, _translate("Notepad", "12"))
        self.comboBox_4.setItemText(5, _translate("Notepad", "14"))
        self.comboBox_4.setItemText(6, _translate("Notepad", "16"))
        self.comboBox_4.setItemText(7, _translate("Notepad", "18"))
        self.comboBox_4.setItemText(8, _translate("Notepad", "20"))
        self.comboBox_4.setItemText(9, _translate("Notepad", "22"))
        self.pushButton_20.setText(_translate("Notepad", "Refresh"))
        self.textEdit_8.setHtml(_translate("Notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"right\" dir=\'rtl\' style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:8.07477pt;\"><br /></p></body></html>"))

        self.pushButton_16.setText(_translate("Notepad", "Finish"))
        self.pushButton_11.setText(_translate("Notepad", "Change"))
        self.label.setText(_translate("Notepad", "Words templates database"))
        self.pushButton_12.setText(_translate("Notepad", "Change"))
        self.label_2.setText(_translate("Notepad", "Words synonyme antonyme database"))
        self.checkBox.setText(_translate("Notepad", "Arabic"))
        self.checkBox_2.setText(_translate("Notepad", "English"))
        self.label_3.setText(_translate("Notepad", "Language:"))
        self.pushButton_13.setText(_translate("Notepad", "Finish"))
        self.textEdit_10.setHtml(_translate("Notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; color:#00aa00;\">Welcome to HLPL-Composer</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:16pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt;\">We have assembled some links to get you started:</span></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:14pt; text-decoration: underline;\">read docs for quick guide on using software at: </span><a href=\"https://docs.hlpl.net/\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">HLPL-Composer Guide</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; text-decoration: underline; color:#0000ff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://docs.hlpl.net/\"><span style=\" font-size:14pt; text-decoration: underline; color:#000000;\">Visit HLPL-Composer forum for opening and discussing issues about software at:  </span></a><a href=\"https://forum.hlpl.net\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">HLPL-Composer Forum</span></a></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; font-size:14pt; color:#0000ff;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><a href=\"https://forum.hlpl.net\"><span style=\" font-size:14pt; text-decoration: underline; color:#000000;\">Visit Official website of the organization HLPL (Human Life Programing Language) for completing sofwtares and further developements at: </span></a><a href=\"https://hlpl.net\"><span style=\" font-size:14pt; text-decoration: underline; color:#0000ff;\">HLPL Organization</span></a></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("Notepad", "New Message"))
        self.pushButton_14.setText(_translate("Notepad", "Delete all messages"))
        self.textEdit_19.setHtml(_translate("Notepad", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:8.25pt; font-weight:400; font-style:normal;\">\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
"<p align=\"center\" style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><span style=\" font-size:16pt; font-weight:600;\">No messages found!</span></p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("Notepad", "Old Messages"))
        self.menuEdit.setTitle(_translate("Notepad", "Composer"))
        self.menu.setTitle(_translate("Notepad", "File"))
        self.menu_2.setTitle(_translate("Notepad", "Edit"))
        self.menuFormat.setTitle(_translate("Notepad", "Format"))
        self.menu_4.setTitle(_translate("Notepad", "Compose"))
        self.menu_5.setTitle(_translate("Notepad", "Setting"))
        self.menuRescources.setTitle(_translate("Notepad", "Rescource"))
        self.menuMessages.setTitle(_translate("Notepad", "Message"))
        self.toolBar_3.setWindowTitle(_translate("Notepad", "toolBar_3"))
        self.toolBar_2.setWindowTitle(_translate("Notepad", "toolBar_2"))
        self.action_8.setText(_translate("Notepad", "Print text"))
        self.action_11.setText(_translate("Notepad", "Open text"))
        self.action_12.setText(_translate("Notepad", "فتح 2"))
        self.action_10.setText(_translate("Notepad", "Copy"))
        self.action_14.setText(_translate("Notepad", "Paste"))
        self.action_17.setText(_translate("Notepad", "Undo"))
        self.action_18.setText(_translate("Notepad", "Redo"))
        self.action_26.setText(_translate("Notepad", "Justify"))
        self.action_25.setText(_translate("Notepad", "Align center"))
        self.action_23.setText(_translate("Notepad", "Align right"))
        self.action_24.setText(_translate("Notepad", "Italic"))
        self.action_27.setText(_translate("Notepad", "Bold"))
        self.action.setText(_translate("Notepad", "Save text"))
        self.action_2.setText(_translate("Notepad", "Save template"))
        self.action_3.setText(_translate("Notepad", "Print template"))
        self.action_7.setText(_translate("Notepad", "Cut"))
        self.action_13.setText(_translate("Notepad", "إعادة آخر فعل 2"))
        self.action_15.setText(_translate("Notepad", "إلغاء آخر فعل 2"))
        self.action_16.setText(_translate("Notepad", "لسق 2"))
        self.action_19.setText(_translate("Notepad", "نسخ 2"))
        self.action_20.setText(_translate("Notepad", "إتجاه الخط \"يمين\" 2"))
        self.action_21.setText(_translate("Notepad", "إتجاه الخط \"متمركز\" 2"))
        self.action_22.setText(_translate("Notepad", "ضبط النص 2"))
        self.action_29.setText(_translate("Notepad", "إطالي 2"))
        self.action_31.setText(_translate("Notepad", "Select all"))
        self.action_32.setText(_translate("Notepad", "Wrap text to window"))
        self.action_33.setText(_translate("Notepad", "Underline"))
        self.action_36.setText(_translate("Notepad", "تحديد الكل 2"))
        self.action_37.setText(_translate("Notepad", "لف إلى الشاشة المرئية 2"))
        self.action_38.setText(_translate("Notepad", "تحت السطر 2"))
        self.action_9.setText(_translate("Notepad", "عريض 2"))
        self.action_1.setText(_translate("Notepad", "حفظ+ 1"))
        self.action_34.setText(_translate("Notepad", "حفظ+ 2"))
        self.action_30.setText(_translate("Notepad", "Compose  texts alike"))
        self.action_35.setText(_translate("Notepad", "Compose texts opposit"))
        self.action_5.setText(_translate("Notepad", "Guide"))
        self.action_6.setText(_translate("Notepad", "About"))
        self.action_28.setText(_translate("Notepad", "License"))
        self.action_4.setText(_translate("Notepad", "Exit"))
        self.action_39.setText(_translate("Notepad", "Settings"))
        self.actionWords_templates_database.setText(_translate("Notepad", "Words templates database"))
        self.actionWords_synonyme_antonyme_database.setText(_translate("Notepad", "Words synonyme antonyme database"))
        self.actionMessages.setText(_translate("Notepad", "Messages"))
        self.actionForum.setText(_translate("Notepad", "Forum"))
        self.actionAcount.setText(_translate("Notepad", "Account setting"))
        self.actionAdjust_left.setText(_translate("Notepad", "Align left"))
        self.actionRestart.setText(_translate("Notepad", "Restart"))
        self.actionRestart_2.setText(_translate("Notepad", "Restart"))
        self.actionExit.setText(_translate("Notepad", "Exit"))
        self.actionMessages_2.setText(_translate("Notepad", "Messages"))
        self.actionAccount_setting.setText(_translate("Notepad", "Account setting"))
        self.actionWords_templates_database_2.setText(_translate("Notepad", "Words templates database"))
        self.actionWords_synonyme_antonyme_database_2.setText(_translate("Notepad", "Words synonyme antonyme database"))
        self.actionGuide.setText(_translate("Notepad", "Guide"))
        self.actionForum_2.setText(_translate("Notepad", "Forum"))
        self.actionAbout.setText(_translate("Notepad", "About"))
        self.actionnnn.setText(_translate("Notepad", "nnn"))
        self.actionAlign_left.setText(_translate("Notepad", "Align left"))










class FlowLayout(QtWidgets.QLayout):
    def __init__(self, parent=None, margin=0, spacing=-1):
        super(FlowLayout, self).__init__(parent)
               
        self.speak = pyqtSignal(str)
        
        self.setSpacing(spacing)

        self.itemList = []
                                         
           
    def __del__(self):
        item = self.takeAt(0)
        while item:
            item = self.takeAt(0)

    def addItem(self, item):
        self.itemList.append(item)

    def count(self):
        return len(self.itemList)

    def itemAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList[index]

        return None

    def takeAt(self, index):
        if index >= 0 and index < len(self.itemList):
            return self.itemList.pop(index)

        return None

    def expandingDirections(self):
        return QtCore.Qt.Orientations(QtCore.Qt.RightToLeft)

    def hasHeightForWidth(self):
        return True

    def heightForWidth(self, width):
        height = self.doLayout(QtCore.QRect(0, 0, width, 0), True)
        return 27

    def setGeometry(self, rect):
        super(FlowLayout, self).setGeometry(rect)
        self.doLayout(rect, False)

    def sizeHint(self):
        return self.minimumSize()

    def minimumSize(self):
        size = QtCore.QSize()

        for item in self.itemList:
            size = size.expandedTo(item.minimumSize())

        size += QtCore.QSize(2 * self.contentsMargins().top(), 2 * self.contentsMargins().top())
        return size


    def doLayout(self, rect, testOnly):
        x = rect.x()
        y = rect.y()
        x1=rect.width()
        lineHeight = 0

        for item in self.itemList:
            yy=rrm-item.sizeHint().width()
            wid = item.widget()
            spaceX = self.spacing() + wid.style().layoutSpacing(QtWidgets.QSizePolicy.PushButton, QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Horizontal)
            spaceY = self.spacing() + wid.style().layoutSpacing(QtWidgets.QSizePolicy.PushButton, QtWidgets.QSizePolicy.PushButton, QtCore.Qt.Vertical)
            nextX = x + item.sizeHint().width() + spaceX
            if nextX - spaceX > rect.right() and lineHeight > 0:
                x = rect.x()
                y = y + lineHeight + spaceY
                nextX = x + item.sizeHint().width() + spaceX
                lineHeight = 0

            if not testOnly:
               if Ui_Notepad.language==True:
                  item.setGeometry(QtCore.QRect(QtCore.QPoint(x1-x+yy-11, y), item.sizeHint()))
               else:
                  item.setGeometry(QtCore.QRect(QtCore.QPoint(x, y), item.sizeHint()))                 
            
            
            x = nextX+1
            lineHeight = max(lineHeight, item.sizeHint().height())


 




import configparser
import sys
import os
def get_hlpl_composer__version(case):
    config = configparser.ConfigParser()
    current_directory = os.path.dirname(os.path.abspath(__file__))
    config_file_path = os.path.join(current_directory, 'setup.cfg')
    config.read(config_file_path)
    if case=='version':
       return config['hlpl_composer']['version']
    if case=='else':
       return config['hlpl_composer']['version']+'\n'+config['hlpl_composer']['author']+'\n'+config['hlpl_composer']['email']+'\n'+config['hlpl_composer']['url']+'\n'
 

       
      
        
def main():
    st=hlpl_get_name(sys.argv[0])
    if st=='hlpl_composer':
       app = QtWidgets.QApplication(sys.argv)

       icon = QtGui.QIcon()
       dirx=os.path.dirname(sfd2.__file__);st=os.path.join(dirx,"composer.png")
       icon.addPixmap(QtGui.QPixmap(st), QtGui.QIcon.Normal, QtGui.QIcon.Off)
       app.setWindowIcon(icon)
        
       ex = Ui_Notepad()
       w = QtWidgets.QMainWindow()
       ex.setupUi(w)
       w.show()
       sys.exit(app.exec_())
    if st=='version':
        print('\n'+get_hlpl_composer__version('version'))    
    
    else:
        print('\n'+get_hlpl_composer__version('else')+'\n'+'hlpl_composer under developement, it will be released next versions of HLPL')    
    
    