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

# Bucle para solicitar datos a añadir
    true = True
    while true:
        fieldnames = ['Name', 'Platform', 'Year', 'Genre', 'Publisher',
                'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales']
        lista_asubir = []
        lista_asubir.append("")
        global_sales = 0
        for i in range(len(fieldnames)):
                lista_asubir.append(input("Introduce el {}: ".format(fieldnames[i])))
                if fieldnames[i] == 'NA_Sales' or fieldnames[i] == 'EU_Sales' or fieldnames[i] == 'JP_Sales' or fieldnames[i] == 'Other_Sales':
                    global_sales += float(lista_asubir[i])
        lista_asubir.append(global_sales)
                # Permite escribir nuevas lineas en el csv
        with open("juegos.csv", "a", newline="", encoding="utf-8") as csvfile:
                csv_writer = csv.writer(csvfile)
                csv_writer.writerow(lista_asubir)

def sorted_games():
    csv2 = get_CSV()
    lista_csv = []
    for i in range(1,len(csv2)):
        lista_csv.append(csv2[i])
    diccionario = ['Rank', 'Name', 'Platform', 'Year', 'Genre', 'Publisher', 'NA_Sales', 'EU_Sales', 'JP_Sales', 'Other_Sales', 'Global_Sales']
    sorted_list = sorted(lista_csv, key=lambda x: float(x[10]), reverse= True)
    for i in range(len(sorted_list)):
        sorted_list[i][0] = i+1
    sorted_list = sorted_list[::-1]
    sorted_list.append(diccionario)
    sorted_list = sorted_list[::-1]
    with open("juegos.csv", "w", newline="", encoding="utf-8") as csvfile:
        csv_writer = csv.writer(csvfile)
        csv_writer.writerows(sorted_list)
sorted_games()


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
