import os
import re

dir_name = "."
files = os.listdir(dir_name)
excel_files = []
for file in files:
    full_name = os.path.join(dir_name, file)
    print("파일명:", full_name)

    ext = os.path.splitext(full_name)[1]
    print("확장자:", ext)

    if ext in ['.xls', '.xlsx', '.xlsm'] \
            and not re.search(r"^\~\$", file):
        print("엑셀파일:", full_name)
        excel_files.append(full_name)

print("엑셀파일리스트:", excel_files)
