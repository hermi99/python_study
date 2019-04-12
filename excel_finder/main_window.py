import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

uifile = r'.\resources\qt\main_window.ui'
form, base = uic.loadUiType(uifile)


class MainWindow(form, base):
    def __init__(self):
        super().__init__()
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
