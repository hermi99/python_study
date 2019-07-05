import xlrd
from xlsxwriter.utility import xl_rowcol_to_cell

workbook = xlrd.open_workbook(r"선번장_테스트.xlsx")

print("워크시트 개수:", workbook.nsheets)

sheets = workbook.sheets()
print("워크시트:", sheets)

sheet = sheets[0]
cell = sheet.cell(0, 0)
print("cell(0,0):", cell)
print("cell_value:", cell.value)

print("row size:", sheet.nrows)
print("col size:", sheet.ncols)

find_results = []
search_text = "02018878-000"
for row in range(sheet.nrows):
    for col in range(sheet.ncols):
        cell = sheet.cell(row, col)
        if search_text in cell.value:
            cell_name = xl_rowcol_to_cell(row, col)
            # print(sheet.name, cell.value, cell_name)
            find_results.append((sheet.name, cell.value, cell_name))

print("검색결과:", find_results)




