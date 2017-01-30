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
        self.ui.comboBox_device.currentIndexChanged.connect(self.updatedescription)
        self.coms = serial.tools.list_ports.comports()
        for i in self.coms[::-1]:
            self.ui.comboBox_device.addItem(i.device)

    def updatedescription(self, a):
        self.ui.label_description.setText(self.coms[a].description)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())
