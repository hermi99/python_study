import sys

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication

from day07.dialog_buttonbox import DialogButtonBox

uifile = r'.\qt\window_name.ui'
form, base = uic.loadUiType(uifile)


class WindowName(form, base):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_dialog.clicked.connect(self.btn_dialog_clicked)

    def btn_dialog_clicked(self):
        print("btn_dialog_clicked")
        dialog = DialogButtonBox()
        dialog.show()
        dialog.exec()

        print(dialog.result())

        if dialog.result():
            name = dialog.text_name.text()
            print(name)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindowName()
    window.show()
    app.exec_()