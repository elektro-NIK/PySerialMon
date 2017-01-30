#!/usr/bin/env python3

import sys
import mainwindow_ui
from PyQt5.QtWidgets import *


class MainWin(QMainWindow):
    # noinspection PyArgumentList
    def __init__(self, parent=None):
        super().__init__(parent)
        self.ui = mainwindow_ui.Ui_MainWindow()
        self.ui.setupUi(self)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    myapp = MainWin()
    myapp.show()
    sys.exit(app.exec_())
