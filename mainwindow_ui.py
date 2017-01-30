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
        self.comboBox_device = QtWidgets.QComboBox(self.frame_ctrl)
        self.comboBox_device.setMaximumSize(QtCore.QSize(135, 16777215))
        self.comboBox_device.setObjectName("comboBox_device")
        self.horizontalLayout_3.addWidget(self.comboBox_device)
        self.pushButton_update = QtWidgets.QPushButton(self.frame_ctrl)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_update.sizePolicy().hasHeightForWidth())
        self.pushButton_update.setSizePolicy(sizePolicy)
        self.pushButton_update.setMaximumSize(QtCore.QSize(34, 16777215))
        self.pushButton_update.setText("")
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("icons/update.svg"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.pushButton_update.setIcon(icon)
        self.pushButton_update.setObjectName("pushButton_update")
        self.horizontalLayout_3.addWidget(self.pushButton_update)
        self.label_description = QtWidgets.QLabel(self.frame_ctrl)
        self.label_description.setObjectName("label_description")
        self.horizontalLayout_3.addWidget(self.label_description)
        self.comboBox_baud = QtWidgets.QComboBox(self.frame_ctrl)
        self.comboBox_baud.setMinimumSize(QtCore.QSize(0, 0))
        self.comboBox_baud.setMaximumSize(QtCore.QSize(99, 16777215))
        self.comboBox_baud.setEditable(True)
        self.comboBox_baud.setObjectName("comboBox_baud")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.comboBox_baud.addItem("")
        self.horizontalLayout_3.addWidget(self.comboBox_baud)
        self.label_baud = QtWidgets.QLabel(self.frame_ctrl)
        self.label_baud.setMaximumSize(QtCore.QSize(35, 16777215))
        self.label_baud.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.label_baud.setAlignment(QtCore.Qt.AlignCenter)
        self.label_baud.setWordWrap(False)
        self.label_baud.setObjectName("label_baud")
        self.horizontalLayout_3.addWidget(self.label_baud)
        self.verticalLayout.addWidget(self.frame_ctrl)
        self.frame_send = QtWidgets.QFrame(self.centralwidget)
        self.frame_send.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_send.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_send.setObjectName("frame_send")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_send)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit_input = QtWidgets.QLineEdit(self.frame_send)
        self.lineEdit_input.setObjectName("lineEdit_input")
        self.horizontalLayout_2.addWidget(self.lineEdit_input)
        self.comboBox_lineend = QtWidgets.QComboBox(self.frame_send)
        self.comboBox_lineend.setObjectName("comboBox_lineend")
        self.comboBox_lineend.addItem("")
        self.comboBox_lineend.addItem("")
        self.comboBox_lineend.addItem("")
        self.comboBox_lineend.addItem("")
        self.horizontalLayout_2.addWidget(self.comboBox_lineend)
        self.pushButton_send = QtWidgets.QPushButton(self.frame_send)
        self.pushButton_send.setEnabled(False)
        self.pushButton_send.setCheckable(False)
        self.pushButton_send.setChecked(False)
        self.pushButton_send.setObjectName("pushButton_send")
        self.horizontalLayout_2.addWidget(self.pushButton_send)
        self.verticalLayout.addWidget(self.frame_send)
        self.plainTextEdit_output = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.plainTextEdit_output.setReadOnly(True)
        self.plainTextEdit_output.setCenterOnScroll(False)
        self.plainTextEdit_output.setObjectName("plainTextEdit_output")
        self.verticalLayout.addWidget(self.plainTextEdit_output)
        self.frame_outctrl = QtWidgets.QFrame(self.centralwidget)
        self.frame_outctrl.setLayoutDirection(QtCore.Qt.RightToLeft)
        self.frame_outctrl.setFrameShape(QtWidgets.QFrame.NoFrame)
        self.frame_outctrl.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_outctrl.setObjectName("frame_outctrl")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame_outctrl)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.checkBox_autoscroll = QtWidgets.QCheckBox(self.frame_outctrl)
        self.checkBox_autoscroll.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.checkBox_autoscroll.setChecked(True)
        self.checkBox_autoscroll.setObjectName("checkBox_autoscroll")
        self.horizontalLayout.addWidget(self.checkBox_autoscroll)
        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)
        self.verticalLayout.addWidget(self.frame_outctrl)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QtWidgets.QStatusBar(MainWindow)
        self.statusBar.setObjectName("statusBar")
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)
        self.comboBox_baud.setCurrentIndex(3)
        self.comboBox_lineend.setCurrentIndex(1)
        self.lineEdit_input.returnPressed.connect(self.pushButton_send.click)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        MainWindow.setTabOrder(self.comboBox_device, self.pushButton_update)
        MainWindow.setTabOrder(self.pushButton_update, self.comboBox_baud)
        MainWindow.setTabOrder(self.comboBox_baud, self.lineEdit_input)
        MainWindow.setTabOrder(self.lineEdit_input, self.comboBox_lineend)
        MainWindow.setTabOrder(self.comboBox_lineend, self.pushButton_send)
        MainWindow.setTabOrder(self.pushButton_send, self.plainTextEdit_output)
        MainWindow.setTabOrder(self.plainTextEdit_output, self.checkBox_autoscroll)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "PySerialMon"))
        self.label_description.setText(_translate("MainWindow", "None"))
        self.comboBox_baud.setItemText(0, _translate("MainWindow", "1200"))
        self.comboBox_baud.setItemText(1, _translate("MainWindow", "2400"))
        self.comboBox_baud.setItemText(2, _translate("MainWindow", "4800"))
        self.comboBox_baud.setItemText(3, _translate("MainWindow", "9600"))
        self.comboBox_baud.setItemText(4, _translate("MainWindow", "14400"))
        self.comboBox_baud.setItemText(5, _translate("MainWindow", "19200"))
        self.comboBox_baud.setItemText(6, _translate("MainWindow", "28800"))
        self.comboBox_baud.setItemText(7, _translate("MainWindow", "57600"))
        self.comboBox_baud.setItemText(8, _translate("MainWindow", "115200"))
        self.label_baud.setText(_translate("MainWindow", "&baud"))
        self.comboBox_lineend.setItemText(0, _translate("MainWindow", "No ()"))
        self.comboBox_lineend.setItemText(1, _translate("MainWindow", "NL (\\n)"))
        self.comboBox_lineend.setItemText(2, _translate("MainWindow", "CR (\\r)"))
        self.comboBox_lineend.setItemText(3, _translate("MainWindow", "CR+NL (\\r\\n)"))
        self.pushButton_send.setText(_translate("MainWindow", "Send"))
        self.checkBox_autoscroll.setText(_translate("MainWindow", "Autoscroll"))

