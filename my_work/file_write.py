f = open("new_file.txt", "w")

data = "텍스트 데이터\n"
f.write(data)

data = "두번째 텍스트 데이터\n"
f.write(data)

f.close()