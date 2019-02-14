

with open("myfile.txt", "r", newline='') as f:
    # print(f.read())

    # print(f.readline())
    # print(f.readline())
    # print(f.readline())

    # for line in f.readlines():
    for line in f.read().splitlines():
        print(line)
        data = line.split(",")
        port = data[0]
        ipadddr = data[1]
        line_number = data[2]

        # print(port, ipadddr, line_number)



