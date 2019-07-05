from PyQt5 import uic

uifile = r'.\qt\dialog_buttonbox.ui'
form, base = uic.loadUiType(uifile)


class DialogButtonBox(form, base):
    def __init__(self):
        super().__init__()
        self.setupUi(self)