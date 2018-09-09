import csv

data = [
    ['Sachin',80],
    ['Virat',120],
    ['Yuvraj',50],
    ['Dhoni',65],
    ['Suresh',10]
]

with open('data.csv', 'w', newline='') as file:
    writer = csv.writer(file)

    for row in data:
        writer.writerow(row)