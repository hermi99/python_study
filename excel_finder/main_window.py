import sys

from PyQt5.QtCore import QAbstractTableModel, Qt, QVariant, QThread

from PyQt5 import uic, QtCore
from PyQt5.QtWidgets import QApplication

from excel_finder.excel_finder_app import ExcelFinder

uifile = r'.\resources\qt\main_window.ui'
form, base = uic.loadUiType(uifile)


class MainWindow(form, base):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.btn_search.clicked.connect(self.btn_search_clicked)
        self.btn_stop.clicked.connect(self.btn_stop_clicked)

    def btn_search_clicked(self):
        search_text = self.text_search.text()

        self.thread = SearchThread(search_text)
        self.thread.searchEndEvent.connect(self.search_completed)
        self.thread.start()


    def btn_stop_clicked(self):
        print("stop")
        self.stop_search()


    def search_completed(self, find_results):
        headers = ["엑셀파일", "시트명", "셀", "셀 데이터"]
        datas = []

        for file_name, sheet_name, cell_value, cell_name in find_results:
            datas.append([file_name, sheet_name, cell_name, cell_value])

        model = TableModel(datas, headers)
        self.table_results.setModel(model)

    def stop_search(self):
        self.thread.stop()

class SearchThread(QThread):
    searchEndEvent = QtCore.pyqtSignal(list)

    def __init__(self, search_text):
        super().__init__()

        self.search_text = search_text
        self.is_running = True

    def run(self):
        excel_finder = ExcelFinder([r"D:\excel_test", r"D:\excel_test\sub"])
        find_results = excel_finder.text_search(self, str(self.search_text))
        self.searchEndEvent.emit(find_results)

    def stop(self):
        self.is_running = False

class TableModel(QAbstractTableModel):
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
