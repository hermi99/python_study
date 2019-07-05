import csv

with open('output.csv', 'w', newline='') as f:
    writer = csv.writer(f)
    writer.writerow([1, 'hi', '하이'], )
    writer.writerow([2, 'hello', '헬로우'])
    writer.writerow([3, 'morning', '모닝'])