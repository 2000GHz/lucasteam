import csv
import heapq
from datetime import datetime
import pandas as pd
import os
import tabulate
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


def list_all_csv(n):
    #df = pd.read_csv('juegos.csv')
    #print(df)
    pd.options.display.max_rows = None
    df = pd.read_csv('juegos.csv')
    print(df.head(n))
    input("***Pulsa cualquier tecla para volver: ")
    os.system("cls")
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
                    if fieldnames[i] == "Platform":
                        respuesta = compare_platform(lista_asubir[i+1])
                        if respuesta == False:
                            raise ValueError("***Escoge un valor de la lista: ***")
                    elif fieldnames[i] == "Year" and (int(lista_asubir[i+1]) > year_actual \
                        or int(lista_asubir[i+1]) < 1950):
                        raise ValueError("***Valor inválido***")
                    elif (fieldnames[i] == 'NA_Sales' \
                        or fieldnames[i] == 'EU_Sales'\
                            or fieldnames[i] == 'JP_Sales'\
                                or fieldnames[i] == 'Other_Sales'):
                        global_sales += float(lista_asubir[i+1])
                    salir = False
                except Exception as e :
                    print(e)
                    lista_asubir.pop()
        print("\n***Total de ventas globales: {}***"
              .format(global_sales))
        lista_asubir.append(global_sales)
        print("Estos son los datos el juego añadido:")
        print(", ".join(lista_asubir[1:-1]),",",lista_asubir[-1])
        paso2 = input("---> ¿Quieres guardar los cambios en el CSV? S/N: ")
        if paso2.lower() == "s":
            saved_csv(lista_asubir)
        paso = input("Quieres añadir algun juego mas S/N:  ")
        if paso.lower() == "n":
            true = False
#Te crea una lista con las plataformas existentes.
def search_platform():
    plataformas = []
    list_csv = get_dict()
    for plataforma in range(len(list_csv)):
        if  list_csv[plataforma]["Platform"] in plataformas :
            pass
        else:
            plataformas.append(list_csv[plataforma]["Platform"])
    return plataformas
#Compara las plataformas del csv con las escritas por el usuario
def compare_platform(n): 
    plataformas = search_platform()
    plataformas_low = [plataformas_low.lower() for plataformas_low in plataformas]
    if n.lower() in plataformas_low:
        salida = True
        pass
    else:
        a = input("La plataforma {} no exite, ¿Quieres añadir una nueva plataforma? S/N: ".format(n))
        if a.lower() == "n":
            print("\n")
            print("Escoge entre una de las plataformas existentes:")
            print(", ".join(plataformas))
            print("\n") 
            salida = False
        else:
            salida = True
    return salida
# Permite escribir nuevas lineas en el csv

def saved_csv(lista_asubir):
    with open("juegos.csv", "a", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerow(lista_asubir)
    sorted_games()
    print("***Se ha guardado en el fichero CSV y se ha ordenado de nuevo el ranking***")

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


# La función devuelve los 5 juegos más vendidos en el mundo

def max_globalsales():
    lista_aux = get_dict()
    num_globalsales = []
    num_globalsales = heapq.nlargest(5, lista_aux, key=lambda s: float(s['Global_Sales']))
    for i in range(len(num_globalsales)):
        print(num_globalsales[i]["Rank"], "juego: ", num_globalsales[i]["Name"], ", con ", num_globalsales[i]["Global_Sales"], " millones de ventas.")
    input("***Pulse cualquier tecla para continuar***")
    

