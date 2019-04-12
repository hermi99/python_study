import os
import re

import xlrd
from xlsxwriter.utility import xl_rowcol_to_cell


class ExcelFinder:
    def __init__(self, dir_names):
        self.excel_files = self.find_excel_files(dir_names)

    def find_excel_files(self, dir_names):
        excel_files = []
        for dir_name in dir_names:
            files = os.listdir(dir_name)
            for file in files:
                full_name = os.path.join(dir_name, file)
                ext = os.path.splitext(full_name)[1]
                if ext in ['.xls', '.xlsx', '.xlsm'] \
                        and not re.search(r"^\~\$", file):
                    excel_files.append(full_name)

        return excel_files

    def text_search(self, search_text):
        find_results = []
        for excel_file in self.excel_files:
            workbook = xlrd.open_workbook(excel_file)
            sheets = workbook.sheets()

            for sheet in sheets:
                for row in range(sheet.nrows):
                    for col in range(sheet.ncols):
                        cell = sheet.cell(row, col)
                        if search_text in cell.value:
                            cell_name = xl_rowcol_to_cell(row, col)
                            find_results.append((excel_file, sheet.name, cell.value, cell_name))

        return find_results


if __name__ == '__main__':
    excel_finder = ExcelFinder([r"D:\excel_test", r"D:\excel_test\sub"])
    find_results = excel_finder.text_search("02018878-0005")

    print(find_results)