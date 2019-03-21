import sys

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication, QMessageBox

uifile = r'.\qt\name_window.ui'
form, base = uic.loadUiType(uifile)


class NameWindow(form, base):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_add.clicked.connect(self.btn_add_clicked)
        self.btn_clear.clicked.connect(self.btn_clear_clicked)

    def btn_add_clicked(self):
        name = self.text_name.text()

        if not name:
            QMessageBox.warning(self, "입력 에러", "이름을 입력하세요")
            return

        self.list_name.addItem(name)
        self.text_name.clear()

    def btn_clear_clicked(self):
        self.list_name.clear()


if __name__ == '__main__':
    app = QApplication([])
    main_window = NameWindow()
    main_window.show()
    app.exec()
