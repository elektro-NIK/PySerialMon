#!/usr/bin/env python3

import sys
import serial.tools.list_ports
import serial
import mainwindow_ui
from PyQt5.QtWidgets import *


class MainWin(QMainWindow):
    # noinspection PyArgumentList
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)
        # Connects:
        self.ui.pushButton_update.clicked.connect(self.updatedevices)
        self.ui.pushButton_send.clicked.connect(self.senddata)
        self.ui.comboBox_device.currentTextChanged.connect(self.updatedescription)
        self.ui.comboBox_baud.currentTextChanged.connect(self.updatebaud)
        # Devices:
        self.coms = None
        self.com = None
        self.baud = None
        self.con = None
        self.updatedevices()
        self.updatebaud(self.ui.comboBox_baud.currentText())

    def updatedevices(self):
        try:
            self.con.close()
        except AttributeError:
            pass
        self.ui.pushButton_send.setDisabled(True)
        self.ui.comboBox_device.clear()
        coms = serial.tools.list_ports.comports()
        if len(coms) == 0:
            self.ui.statusBar.showMessage('No serial adapter found!', msecs=3000)
        self.coms = {i.device: i.description for i in coms[::-1]}
        for i in self.coms.keys():
            self.ui.comboBox_device.addItem(i)

    def updatedescription(self, dev):
        if dev:
            self.ui.label_description.setText(self.coms[dev])
            self.com = dev
            if self.baud:
                self.con = serial.Serial(self.com, self.baud, timeout=0.1)
                self.ui.statusBar.showMessage('Connect to {0} with baud = {1}'.format(self.com,  self.baud), msecs=5000)
                self.ui.pushButton_send.setEnabled(True)
        else:
            self.com = None

    def updatebaud(self, baud):
        try:
            self.con.close()
        except AttributeError:
            pass
        self.ui.pushButton_send.setDisabled(True)
        try:
            self.baud = int(baud)
            self.ui.comboBox_baud.setStyleSheet(None)
            if self.com:
                self.con = serial.Serial(self.com, self.baud, timeout=0.1)
                self.ui.statusBar.showMessage('Connect to {0} with baud = {1}'.format(self.com,  self.baud), msecs=5000)
                self.ui.pushButton_send.setEnabled(True)
        except ValueError:
            self.baud = None
            self.ui.comboBox_baud.setStyleSheet('background:#ff0000')
            self.ui.statusBar.showMessage('Bad baud value!', msecs=3000)

    def senddata(self):
        print('1')

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())
