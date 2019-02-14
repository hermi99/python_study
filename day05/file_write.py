
# f = open("myfile.txt", "w")
# f.write("hello again\n")
# f.write("hello again2")
# f.close()

# file write with
with open("myfile.txt", "w") as f:
    # f.write("hello again\n")
    # f.write("hello again2")

    datas = []
    datas.append("line1")
    datas.append("line2")
    datas.append("line3")

    f.write("\n".join(datas))





