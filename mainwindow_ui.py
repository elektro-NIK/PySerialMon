# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(480, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.frame_ctrl = QtWidgets.QFrame(self.centralwidget)
        self.frame_ctrl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_ctrl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_ctrl.setObjectName("frame_ctrl")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.frame_ctrl)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.comboBox = QtWidgets.QComboBox(self.frame_ctrl)
        self.comboBox.setMaximumSize(QtCore.QSize(135, 16777215))
        self.comboBox.setObjectName("comboBox")
        self.horizontalLayout_3.addWidget(self.comboBox)
        self.label_2 = QtWidgets.QLabel(self.frame_ctrl)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout_3.addWidget(self.label_2)
        self.newLine = QtWidgets.QCheckBox(self.frame_ctrl)
        self.newLine.setChecked(True)
        self.newLine.setObjectName("newLine")
        self.horizontalLayout_3.addWidget(self.newLine)
        self.baud = QtWidgets.QComboBox(self.frame_ctrl)
        self.baud.setMinimumSize(QtCore.QSize(0, 0))
        self.baud.setEditable(True)
        self.baud.setObjectName("baud")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.baud.addItem("")
        self.horizontalLayout_3.addWidget(self.baud)
        self.label = QtWidgets.QLabel(self.frame_ctrl)
        self.label.setMaximumSize(QtCore.QSize(35, 16777215))
        self.label.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setWordWrap(False)
        self.label.setObjectName("label")
        self.horizontalLayout_3.addWidget(self.label)
        self.verticalLayout.addWidget(self.frame_ctrl)
        self.frame_send = QtWidgets.QFrame(self.centralwidget)
        self.frame_send.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_send.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_send.setObjectName("frame_send")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_send)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.input = QtWidgets.QLineEdit(self.frame_send)
        self.input.setObjectName("input")
        self.horizontalLayout_2.addWidget(self.input)
        self.send = QtWidgets.QPushButton(self.frame_send)
        self.send.setObjectName("send")
        self.horizontalLayout_2.addWidget(self.send)
        self.verticalLayout.addWidget(self.frame_send)
        self.output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.output.setReadOnly(True)
        self.output.setObjectName("output")
        self.verticalLayout.addWidget(self.output)
        self.frame_outctrl = QtWidgets.QFrame(self.centralwidget)
        self.frame_outctrl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_outctrl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_outctrl.setObjectName("frame_outctrl")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_outctrl)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.autoscroll = QtWidgets.QCheckBox(self.frame_outctrl)
        self.autoscroll.setChecked(True)
        self.autoscroll.setObjectName("autoscroll")
        self.horizontalLayout.addWidget(self.autoscroll)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.pageMode = QtWidgets.QCheckBox(self.frame_outctrl)
        self.pageMode.setChecked(True)
        self.pageMode.setObjectName("pageMode")
        self.horizontalLayout.addWidget(self.pageMode)
        self.verticalLayout.addWidget(self.frame_outctrl)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.baud.setCurrentIndex(3)
        self.input.returnPressed.connect(self.send.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PySerialMon"))
        self.label_2.setText(_translate("MainWindow", "None"))
        self.newLine.setText(_translate("MainWindow", "Newline"))
        self.baud.setItemText(0, _translate("MainWindow", "1200"))
        self.baud.setItemText(1, _translate("MainWindow", "2400"))
        self.baud.setItemText(2, _translate("MainWindow", "4800"))
        self.baud.setItemText(3, _translate("MainWindow", "9600"))
        self.baud.setItemText(4, _translate("MainWindow", "14400"))
        self.baud.setItemText(5, _translate("MainWindow", "19200"))
        self.baud.setItemText(6, _translate("MainWindow", "28800"))
        self.baud.setItemText(7, _translate("MainWindow", "57600"))
        self.baud.setItemText(8, _translate("MainWindow", "115200"))
        self.label.setText(_translate("MainWindow", "baud"))
        self.send.setText(_translate("MainWindow", "Send"))
        self.autoscroll.setText(_translate("MainWindow", "Autoscroll"))
        self.pageMode.setText(_translate("MainWindow", "Page mode"))
