import xlrd
from xlsxwriter.utility import xl_rowcol_to_cell

workbook = xlrd.open_workbook(r"선번장_테스트.xlsx")
print("sheet 개수:", workbook.nsheets)

sheets = workbook.sheets()

sheet = sheets[0]
print("sheet name:", sheet.name)

cell = sheet.cell(0, 0)

print("cell:", cell)
print("cell_value:", cell.value)

print("row size:", sheet.nrows)
print("col size:", sheet.ncols)

print("cell_name(0,0):", xl_rowcol_to_cell(0, 0))

search_text = "02018878-0009"
print("문자열 찾기: ", search_text)
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        cell = sheet.cell(row, col)
        if search_text in str(cell.value):
            sheet_name = sheet.name
            cell_name = xl_rowcol_to_cell(row, col)
            cell_value = cell.value
            print(sheet_name, cell_name, cell_value)
