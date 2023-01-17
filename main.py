import csv

with open('juegos.csv', newline='') as csvfile:
    data = list(csv.reader(csvfile))

print(data[1][1])