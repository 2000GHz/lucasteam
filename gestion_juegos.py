import csv

# Esta función abre el archivo CSV, lo vuelca en una lista y la devuelve.


def get_CSV():
    with open("juegos.csv", newline="", encoding="utf-8") as csvfile:
        lista_csv = list(csv.reader(csvfile))
    return lista_csv

# Esta funcion genera una lista y dentro de ellas un diccionario


def get_diccionario():
    lista = get_CSV()
    columnas = lista[0]
    diccionario_aux = {}
    lista_dict = []
    for i in range(1, len(lista)):
        datos = zip(columnas, lista[i])
        diccionario_aux = (dict(datos))
        lista_dict.append(diccionario_aux)
    return lista_dict

# Esta funcion tiene que permitir añadir juegos nuevos


def add_games():
    columnas = ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher',
                'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales',
                'Global_Sales']
    lista_asubir = []
    # Bucle para solicitar datos a añadir
    for i in range(len(columnas)):
        lista_asubir.append(input("Introduce el {}: ".format(columnas[i])))
        # Permite escribir nuevas lineas en el csv


"""    with open("juegos.csv", "w", newline="", encoding="utf-8") as csvfile:
        writer = csv.DictWriter(csvfile, columnas=columnas)
        writer.writeheader()
        for fila in lista_asubir:
            writer.writerow(fila)
"""


def filtrado_nombre(nombre):
    lista_aux = get_diccionario()
    for i in range(lista_aux):
        if lista_aux[i]["Name"] == nombre:
            print(lista_aux[i])
