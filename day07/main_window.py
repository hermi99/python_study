import sys

from PyQt5 import uic
from PyQt5.QtCore import pyqtSlot
from PyQt5.QtWidgets import QApplication

uifile = r'.\qt\main_window.ui'
form, base = uic.loadUiType(uifile)


class MainWindow(form, base):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_ok.clicked.connect(self.btn_ok_clicked)

    def btn_ok_clicked(self):
        name = self.text_name.text()
        address = self.text_address.text()

        print("이름은 {}, 주소는 {} 입니다."
              .format(name, address))

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    # app.exec()
    sys.exit(app.exec_())


