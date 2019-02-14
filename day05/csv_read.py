import csv

with open("myfile.csv", "r", newline='') as f:
    reader = csv.reader(f)
    for line in reader:
        number, port, line_number = line
        # number = line[0]
        # port = line[1]
        # line_number = line[2]
        print(number, port, line_number)

