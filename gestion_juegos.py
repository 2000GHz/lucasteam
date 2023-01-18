import csv
import heapq


# Esta función abre el archivo CSV, lo vuelca en una lista y la devuelve.


def get_CSV():
    with open("juegos.csv", newline="", encoding="utf-8") as csvfile:
        lista_csv = list(csv.reader(csvfile))
    return lista_csv

# Esta funcion genera una lista y dentro de ellas un diccionario


def get_dict():
    lista = get_CSV()
    columnas = lista[0]
    diccionario_aux = {}
    lista_dict = []
    for i in range(1, len(lista)):
        datos = zip(columnas, lista[i])
        diccionario_aux = (dict(datos))
        lista_dict.append(diccionario_aux)
    return lista_dict

# Esta funcion permite añadir juegos nuevos


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


# La función devuelve el diccionario del juego solicitado


# La función devuelve los 5 juegos más vendidos en el mundo

def max_globalsales():
    diccionario_juego = []
    lista_aux = get_dict()
    num_globalsales = []
    num_globalsales = heapq.nlargest(5, lista_aux, key=lambda s: float(s['Global_Sales']))
    for i in range(len(num_globalsales)):
        print(num_globalsales[i]["Name"],num_globalsales[i]["Global_Sales"])

    return diccionario_juego


# max_globalsales()
