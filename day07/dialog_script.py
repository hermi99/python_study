from PyQt5 import uic

uifile = r'.\qt\dialog_script.ui'
form, base = uic.loadUiType(uifile)


class DialogScript(form, base):
    def __init__(self, script):
        super().__init__()
        self.setupUi(self)

        self.text_script.setPlainText(script)

