import os
import re

if __name__ == '__main__':
    dir_name = r"d:\excel_test"
    filelist = os.listdir(dir_name)

    for file in filelist:
        print("파일명:", file)
        full_filename =  os.path.join(dir_name, file)
        print("full 파일명:", full_filename)

        ext = os.path.splitext(full_filename)[1]
        print("확장자:", ext)

        # 엑셀파일만 출력
        if ext in ['.xls', '.xlsx', '.xsm'] and not re.search("^~\$", file):
            print("엑셀파일:", full_filename)
