# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'tool.ui'
#
# Created by: PyQt5 UI code generator 5.6
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1366, 768)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.Remaining = QtWidgets.QLabel(self.centralwidget)
        self.Remaining.setMaximumSize(QtCore.QSize(500, 50))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(12)
        self.Remaining.setFont(font)
        self.Remaining.setText("")
        self.Remaining.setAlignment(QtCore.Qt.AlignCenter)
        self.Remaining.setObjectName("Remaining")
        self.verticalLayout.addWidget(self.Remaining)
        self.verticalLayout.setAlignment(self.Remaining, QtCore.Qt.AlignCenter)
        self.image = QtWidgets.QLabel(self.centralwidget)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.image.sizePolicy().hasHeightForWidth())
        self.image.setSizePolicy(sizePolicy)
        self.image.setFocusPolicy(QtCore.Qt.NoFocus)
        self.image.setText("")
        self.image.setScaledContents(True)
        self.image.setAlignment(QtCore.Qt.AlignCenter)
        self.image.setObjectName("image")
        self.verticalLayout.addWidget(self.image)
        self.verticalLayout.setAlignment(self.image, QtCore.Qt.AlignHCenter)
        self.notice = QtWidgets.QLabel(self.centralwidget)
        self.notice.setMaximumSize(QtCore.QSize(700, 50))
        font = QtGui.QFont()
        font.setFamily("等线 Light")
        font.setPointSize(12)
        self.notice.setFont(font)
        self.notice.setAlignment(QtCore.Qt.AlignCenter)
        self.notice.setObjectName("notice")
        self.verticalLayout.addWidget(self.notice)
        self.verticalLayout.setAlignment(self.notice, QtCore.Qt.AlignCenter)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "QuickLabeTool"))
        self.notice.setText(_translate("MainWindow", "红色锥桶按数字键1，蓝色按2，黄色按3，回车确认"))

