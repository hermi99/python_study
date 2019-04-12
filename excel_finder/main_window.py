import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt, QVariant
from PyQt5.QtCore.QAbstractTableModel import QAbstractTableModel
from PyQt5.QtWidgets import QApplication

from excel_finder.excel_finder_app import ExcelFinder

uifile = r'.\resources\qt\main_window.ui'
form, base = uic.loadUiType(uifile)


class MainWindow(form, base):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_search.clicked.connect(self.btn_search_clicked)

    def btn_search_clicked(self):
        search_text = self.text_search.text()
        excel_finder = ExcelFinder([r"D:\excel_test", r"D:\excel_test\sub"])
        find_results = excel_finder.text_search(search_text)
        print(find_results)


class PortModel(QAbstractTableModel):
    def __init__(self, datas, headers):
        super().__init__()
        self.datas = datas
        self.headers = headers

    def rowCount(self, parent=None, *args, **kwargs):
        return len(self.datas)

    def columnCount(self, parent=None, *args, **kwargs):
        return len(self.headers)

    def data(self, index, role=None):
        row = index.row()
        col = index.column()

        if role == Qt.DisplayRole:
            return QVariant(self.datas[row][col])

        return QVariant()

    def headerData(self, col, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headers[col])
        return QVariant()



if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    app.exec_()
