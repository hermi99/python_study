import csv

with open("myfile.csv", "w", newline='') as f:
    writer = csv.writer(f)
    writer.writerow(["번호", "port", "전용번호"])

    list = []
    list.append(["1", "port1", "02190111-1111"])
    list.append(["2", "port2", "02190111-1112"])
    list.append(["3", "port3", "02190111-1113"])

    for data in list:
        writer.writerow(data)
