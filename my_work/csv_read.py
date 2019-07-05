import csv

with open('test.csv', 'r') as f:
    reader = csv.reader(f)
    for line in reader:
        print(line)

