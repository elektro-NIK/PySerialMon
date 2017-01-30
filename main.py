#!/usr/bin/env python3

import sys
import serial.tools.list_ports
import serial
import mainwindow_ui
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *


class MainWin(QMainWindow):
    # noinspection PyArgumentList
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        # Lineending
        self.lineend = ['', '\n', '\r', '\r\n']
        # Connects:
        self.ui.pushButton_update.clicked.connect(self.updatedevices)
        self.ui.pushButton_send.clicked.connect(self.writedata)
        self.ui.comboBox_device.currentTextChanged.connect(self.updatedescription)
        self.ui.comboBox_baud.currentTextChanged.connect(self.updatebaud)
        # Timer:
        self.autoupdate = None
        # Connection:
        self.coms = None
        self.com = None
        self.baud = None
        self.con = None
        # Start
        self.updatedevices()
        self.updatebaud(self.ui.comboBox_baud.currentText())

    def updatedevices(self):
        try:
            self.closeconnection()
        except AttributeError:
            pass
        self.ui.pushButton_send.setDisabled(True)
        self.ui.comboBox_device.clear()
        coms = serial.tools.list_ports.comports()
        if not len(coms):
            self.ui.statusBar.showMessage('No serial adapter found!', msecs=3000)
        self.coms = {i.device: i.description for i in coms[::-1]}
        for i in self.coms.keys():
            self.ui.comboBox_device.addItem(i)

    def updatedescription(self, dev):
        if dev:
            self.ui.label_description.setText(self.coms[dev])
            self.com = dev
            self.con = self.createconnection() if self.baud else None
        else:
            self.com = None

    def updatebaud(self, baud):
        try:
            self.closeconnection()
        except AttributeError:
            pass
        self.ui.pushButton_send.setDisabled(True)
        try:
            self.baud = int(baud)
            self.ui.comboBox_baud.setStyleSheet(None)
            self.con = self.createconnection() if self.com else None
        except ValueError:
            self.baud = None
            self.ui.comboBox_baud.setStyleSheet('background:#ff0000')
            self.ui.statusBar.showMessage('Bad baud value!', msecs=3000)

    def createconnection(self):
        self.ui.plainTextEdit_output.clear()
        self.ui.statusBar.showMessage('Connect to {0} with baud = {1}'.format(self.com, self.baud), msecs=5000)
        self.autoupdate = QTimer(self)
        # noinspection PyUnresolvedReferences
        self.autoupdate.timeout.connect(self.readdata)
        self.autoupdate.start(10)
        self.ui.pushButton_send.setEnabled(True)
        return serial.Serial(self.com, self.baud, timeout=1)

    def closeconnection(self):
        self.con.close()
        self.autoupdate.timeout.disconnect(self.readdata)
        self.con = None

    def writedata(self):
        end = self.lineend[self.ui.comboBox_lineend.currentIndex()]
        msg = self.ui.lineEdit_input.text() + end
        self.ui.lineEdit_input.clear()
        self.con.write(msg.encode())

    def readdata(self):
        if self.con.inWaiting():
            self.ui.plainTextEdit_output.insertPlainText(self.con.readline().decode('utf-8'))
            sb = self.ui.plainTextEdit_output.verticalScrollBar()
            if self.ui.checkBox_autoscroll.isChecked():
                sb.setValue(sb.maximum())

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())
