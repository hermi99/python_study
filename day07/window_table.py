import sys

from PyQt5 import uic
from PyQt5.QtCore import Qt, QVariant, QAbstractTableModel, QModelIndex
from PyQt5.QtGui import QBrush
from PyQt5.QtWidgets import QApplication

from day07.dialog_buttonbox import DialogButtonBox

uifile = r'.\qt\window_table.ui'
form, base = uic.loadUiType(uifile)


class WindowTable(form, base):
    def __init__(self):
        super().__init__()
        self.setupUi(self)

        self.headers = ["번호", "고객명", "전용회선번호", "연락처"]
        self.datas = []
        self.datas.append(["1", "고객1", "02190111-1111", "010-1111-1111"])
        self.datas.append(["2", "고객2", "02190111-1112", "010-1111-1112"])
        self.datas.append(["3", "고객3", "02190111-1113", "010-1111-1113"])
        self.datas.append(["4", "고객4", "02190111-1114", "010-1111-1114"])
        self.datas.append(["5", "고객5", "02190111-1115", "010-1111-1115"])

        self.model = TableModel(self.datas, self.headers)
        self.table_test.setModel(self.model)

        self.btn_update.clicked.connect(self.btn_update_clicked)
        self.table_test.doubleClicked[QModelIndex].connect(self.table_double_clicked)

        self.resize_headers()

    def btn_update_clicked(self):
        print("btn_update_clicked")
        self.datas.append(["6", "고객6", "02190111-1116", "010-1111-1116"])
        model = TableModel(self.datas, self.headers)
        self.table_test.setModel(model)

    def table_double_clicked(self, signal):
        print("table_double_clicked")
        row = signal.row()  # RETRIEVES ROW OF CELL THAT WAS DOUBLE CLICKED

        selected_data = self.datas[row]
        print(selected_data)

    def resize_headers(self):
        # column 크기조절 옵션
        header = self.table_test.horizontalHeader()

        widths = {1: 150, 2: 150, 3: 150}
        for index in range(len(header)):
            if widths.get(index):
                header.resizeSection(index, widths[index])
            else:
                header.resizeSection(index, 80)
        # self.table_test.resizeRowsToContents()

        header.setStyleSheet("QHeaderView { font-size: 10pt; }")
        header.setStyleSheet("color: rgb(255, 170, 0)")



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

        number = self.datas[row][0]

        if role == Qt.DisplayRole:
            return QVariant(self.datas[row][col])
        elif role == Qt.TextAlignmentRole:
            if col in [1, 2, 3]:
                return Qt.AlignLeft + Qt.AlignVCenter
            else:
                return Qt.AlignHCenter + Qt.AlignVCenter
        elif role == Qt.BackgroundRole:
            if number == '2':
                return QBrush(Qt.yellow)

        return QVariant()

    def headerData(self, col, orientation, role=None):
        if orientation == Qt.Horizontal and role == Qt.DisplayRole:
            return QVariant(self.headers[col])
        return QVariant()




if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = WindowTable()
    window.show()
    app.exec_()