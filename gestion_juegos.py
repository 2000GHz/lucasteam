import csv
# Esta funcion abre el archivo CSV, lo vuelca en una lista y devuelve esa lista.
def get_CSV():
    with open('juegos.csv', newline='') as csvfile:
        data = list(csv.reader(csvfile))
    return data
print(get_CSV())

with open('example.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for row in data:
        writer.writerow(row)