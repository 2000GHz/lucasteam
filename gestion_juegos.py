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


def filtrado_nombre(nombre):

    diccionario_juego = []
    lista_aux = get_diccionario()
    for i in range(len(lista_aux)):
        if lista_aux[i]["Name"] == nombre:
            # print(lista_aux[i])
            diccionario_juego = lista_aux[i]

    return diccionario_juego

# La función devuelve el diccionario del juego solicitado


def termino_busqueda():

    Salir = False
    while (not Salir):
        try:
            nombre = str(input("Introduce un término de búsqueda: "))
            valoresfiltrado = filtrado_nombre(nombre)
            if len(valoresfiltrado) == 0:
                salir_subbucle = False
                while not salir_subbucle:

                    add_game_prompt = str(input(
                        "\nEl juego no se encuentra en la base" +
                        " de datos,¿Te gustaría añadirlo?\n1. Sí\n2. No"
                        + "\n3. Realizar otra búsqueda "))
                    if add_game_prompt == '1':
                        salir_subbucle = True
                        add_games()
                    elif add_game_prompt == '2':
                        print("¡Hasta luego!")
                        salir_subbucle = True
                    elif add_game_prompt == '3':
                        salir_subbucle = True
                        print('\n')
                        termino_busqueda()
                    else:
                        print("\nIntroduce un valor correcto")
            else:
                print(valoresfiltrado)
            Salir = True
        except ValueError:
            print('Error, revisa la entrada e inténtalo de nuevo.')

# La función devuelve los 5 juegos más vendidos en el mundo

def max_globalsales():
    diccionario_juego = []
    lista_aux = get_diccionario()
    num_globalsales = []
    num_globalsales = heapq.nlargest(5, lista_aux, key=lambda s: float(s['Global_Sales']))
    for i in range(len(num_globalsales)):
        print(num_globalsales[i]["Name"],num_globalsales[i]["Global_Sales"])
    
    return diccionario_juego


max_globalsales()

filtrado_nombre(termino_busqueda())


