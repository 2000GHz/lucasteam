import csv
import heapq
import menu
from datetime import datetime
import pandas as pd
# Esta función abre el archivo CSV, lo vuelca en una lista y la devuelve.


def get_csv():
    try:
        with open("juegos.csv", newline="", encoding="utf-8") as csvfile:
            lista_csv = list(csv.reader(csvfile))
    except Exception:
        print("***No se ha podido cargar el fichero CSV***")
        print("***Coloque el fichero juegos.csv en la carpeta***")
    return lista_csv

# Lista el csv con formato pandas
def list_all_csv():
    df = pd.read_csv('data.csv')
    print(df)
# Esta funcion genera una lista y dentro de ellas un diccionario

def get_dict():
    lista = get_csv()
    columnas = lista[0]
    diccionario_aux = {}
    lista_dict = []
    for i in range(1, len(lista)):
        datos = zip(columnas, lista[i])
        diccionario_aux = (dict(datos))
        lista_dict.append(diccionario_aux)
    return lista_dict

# Esta funcion añade juegos nuevos con bucle para solicitar datos a añadir


def add_games():

    true = True
    fecha_actual = datetime.now()
    year_actual = fecha_actual.year
    print("----------", year_actual, "----------\n")
    while true:
        fieldnames = ['Name', 'Platform', 'Year', 'Genre', 'Publisher',
                      'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
        lista_asubir = []
        lista_asubir.append(" ")
        global_sales = 0
        for i in range(len(fieldnames)):
            salir = True
            while salir:
                try:
                    lista_asubir.append(
                        input("--> Introduce el/la {}: ".format(fieldnames[i]))
                        )
                    if lista_asubir[i+1] == "":
                        raise ValueError("***No puede estar vacío***")
                    if fieldnames[i] == "Year" and ((int(
                         lista_asubir[i+1]) > year_actual)):
                        raise ValueError("***Valor inválido***")
                    if (fieldnames[i] == 'NA_Sales'
                       or fieldnames[i] == 'EU_Sales'
                       or fieldnames[i] == 'JP_Sales'
                       or fieldnames[i] == 'Other_Sales'):
                        global_sales += float(lista_asubir[i+1])
                    salir = False
                except ValueError:
                    print("\n   ***Error valor/es***\n")
                    lista_asubir.pop()
        print("\n***Total de ventas globales: {}***"
              .format(global_sales))
        lista_asubir.append(global_sales)
        paso2 = input("---> ¿Quieres guardar los cambios en el CSV? S/N: ")
        if paso2.lower() == "s":
            saved_csv(lista_asubir)
            input("---> ¿Ordenar el fichero CSV por ventas globales? S/N: ")
            if paso2.lower() == "s":
                sorted_games()
        paso = input("Quieres añadir algun juego mas S/N:  ")
        if paso.lower() == "n":
            true = False
    menu.pedirNumero()


# Permite escribir nuevas lineas en el csv


def saved_csv(lista_asubir):
    with open("juegos.csv", "a", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(lista_asubir)
    print("***Se ha guardado en el fichero CSV***")

# Funcion que permite ordenar los datos del fichero modificado y los guarda


def sorted_games():

    csv2 = get_csv()
    lista_csv = []
    for i in range(1, len(csv2)):
        lista_csv.append(csv2[i])
    diccionario = ['Rank', 'Name', 'Platform', 'Year', 'Genre',
                   'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales',
                   'Other_Sales', 'Global_Sales']
    sorted_list = sorted(lista_csv, key=lambda x: float(x[10]), reverse=True)
    for i in range(len(sorted_list)):
        sorted_list[i][0] = i+1
    sorted_list = sorted_list[::-1]
    sorted_list.append(diccionario)
    sorted_list = sorted_list[::-1]
    with open("juegos.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(sorted_list)
    print("***Se ha ordenado el fichero CSV***")


# La función devuelve los 5 juegos más vendidos en el mundo

def max_globalsales():
    diccionario_juego = []
    lista_aux = get_dict()
    num_globalsales = []
    num_globalsales = (
        heapq.nlargest(5, lista_aux, key=lambda s: float(s['Global_Sales'])))
    for i in range(len(num_globalsales)):
        print(num_globalsales[i]["Name"], num_globalsales[i]["Global_Sales"])

    return diccionario_juego
