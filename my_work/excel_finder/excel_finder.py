import os
import re

import xlrd
from xlsxwriter.utility import xl_rowcol_to_cell


class ExcelFinder:
    def __init__(self, dir_names):
        self.dir_names = dir_names
        self.excel_files = self.find_excel_files(self.dir_names)

    def find_excel_files(self, dir_names):
        excel_files = []

        for dir_name in dir_names:
            filelist = os.listdir(dir_name)
            for file in filelist:
                full_filename = os.path.join(dir_name, file)
                ext = os.path.splitext(full_filename)[1]

                # 엑셀파일만 돌려주기
                if ext in ['.xls', '.xlsx', '.xsm'] and not re.search("^~\$", file):
                    excel_files.append(full_filename)

        return excel_files

    def text_search(self, search_text):
        """
        모든 파일에서 검색 문자열을 찾아서 sheet명, cell명, cell주소를 돌려준다
        :parameter: sheets, search_text
        :return: find_results(turple : (sheet_name, cell_name, cell_value))
        """
        find_results = []
        for excel_file in self.excel_files:
            workbook = xlrd.open_workbook(excel_file)
            sheets = workbook.sheets()
            sheet_find_results = self.find_text_in_sheets(sheets, search_text)
            for sheet_name, cell_name, cell_value in sheet_find_results:
                find_results.append((excel_file, sheet_name, cell_name, cell_value))

        return find_results

    def find_text_in_sheets(self, sheets, search_text):
        """
        모든 시트에서 검색 문자열을 찾아서 sheet명, cell명, cell주소를 돌려준다
        :parameter: sheets, search_text
        :return: find_results(turple : (sheet_name, cell_name, cell_value))
        """
        find_results = []
        for sheet in sheets:
            for row in range(sheet.nrows):
                for col in range(sheet.ncols):
                    cell = sheet.cell(row, col)
                    if search_text in str(cell.value):
                        sheet_name = sheet.name
                        cell_name = xl_rowcol_to_cell(row, col)
                        cell_value = cell.value
                        find_results.append((sheet_name, cell_name, cell_value))
        return find_results

if __name__ == '__main__':
    # excel_finder = ExcelFinder(["선번장_테스트.xlsx", "선번장_테스트2.xlsx"])
    excel_finder = ExcelFinder([r"d:\excel_test", r"d:\excel_test\sub"])
    find_results = excel_finder.text_search("02018123-0005")
    print(find_results)