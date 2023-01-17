import csv
# Esta funcion abre el archivo CSV, lo vuelca en una lista y devuelve esa lista.
def get_CSV():
    with open('juegos.csv', newline='') as csvfile:
        lista_csv = list(csv.reader(csvfile))
    return lista_csv
lista = get_CSV()
columnas = lista[0]
diccionario = {}
lista2 = []
for i in range(len(lista)):
    datos = zip(columnas,lista[i])
    diccionario = (dict(datos))
    lista2.append(diccionario)

print(lista2[1])


"""with open('example.csv', 'w', newline='') as csvfile:
    fieldnames = ['name', 'age']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)

    writer.writeheader()
    for fila in lista_csv:
        writer.writerow(fila)"""
        