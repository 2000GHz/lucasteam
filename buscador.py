import gestion_juegos
import os
from tabulate import tabulate
contenidocsv = []
contenidocsv = gestion_juegos.get_dict()


"""

La siguiente función nos formatea todos los nombres contenidos
en 'juegos.csv' en minúsculas, con el fin de universilazar
la entrada del usuario (No distinguir entre mayúsculas y minúsculas)

"""

# Formateado de nombres


def formateador_nombres(contenidocsv):
    lista_nombres_minusculas = []
    for juego in range(len(contenidocsv)):
        juegos = contenidocsv[juego]["Name"]
        lista_nombres_minusculas.append(str(juegos).lower())
    return lista_nombres_minusculas


def formateador_editores(contenidocsv):
    lista_editores = []
    list_editores_minusculas = []
    editores = {}

    for juego in range(len(contenidocsv)):
        editores = contenidocsv[juego]["Publisher"]
        lista_editores.append(str(editores))
        list_editores_minusculas.append(str(editores).lower())
    return lista_editores, list_editores_minusculas


def formateador_generos(contenidocsv):

    lista_generos = []

    for juego in range(len(contenidocsv)):
        generos = contenidocsv[juego]["Genre"]
        lista_generos.append(str(generos))

    set_ordenador = set(lista_generos)
    lista_generos = set_ordenador

    return lista_generos


def filtrado_nombre(termino_a_buscar):

    diccionario_juego = contenidocsv

    nombreminusculas = termino_a_buscar.lower()
    lista_nombres_minusculas = formateador_nombres(contenidocsv)

    if nombreminusculas in lista_nombres_minusculas:
        for juego in range(len(contenidocsv)):
            if lista_nombres_minusculas[juego] == nombreminusculas:
                diccionario_juego = contenidocsv[juego]
                print("========================================\n",
                      tabulate(diccionario_juego.items(),
                               tablefmt="fancy_grid"))

    else:
        add_game_prompt = str(input(
                "\n***No se encuentra ningún juego con este" +
                " nombre en la base de datos," +
                " ¿Te gustaría añadirlo?***\n \n1. Sí\n2. No"
                + "\n3. Realizar otra búsqueda\n\n---> "))
        if add_game_prompt == '1':
            gestion_juegos.add_games()
        elif add_game_prompt == '2':
            print("================¡Hasta luego!=================")
            buscar()
        elif add_game_prompt == '3':
            print('\n')
            buscar()
        else:
            print("\n=====Introduce un valor correcto=====")

    return diccionario_juego


def filtrado_genero(termino_a_buscar):

    termino = ""
    termino = termino_a_buscar.capitalize()
    # print(termino)

    lista_aux = contenidocsv

    generos = formateador_generos(contenidocsv)
    # print(generos)

    if termino not in generos:
        print("\n*** El género especificado no existe ***\n")
    else:
        for juego in range(len(lista_aux)):
            if lista_aux[juego]["Genre"] == termino:

                # Devolvemos la lista de juegos correspondientes a este género

                celda_genero1 = [((lista_aux[juego]["Genre"]))]
                celda_genero2 = [[((lista_aux[juego]["Name"]))]]

                print(tabulate(celda_genero2, headers=celda_genero1,
                               tablefmt="fancy_grid", stralign='center'))


def filtrado_editor():
    lista_aux = contenidocsv

    editores = formateador_editores(contenidocsv)
    lista_originales = editores[0]
    lista_minusculas = editores[1]
    corrige_duplicados = []

    eleccion = str(input("*** ¿Qué deseas hacer? ***\n" +
                         "\n1. Mostrar todos los editores" +
                         "\n2. Mostrar los juegos de un editor" +
                         "\n3. Volver al menú" +
                         "\n ---> "))

    if eleccion == "1":
        lista_sin_duplicados = set(lista_originales)
        print(lista_sin_duplicados)

    if eleccion == "2":
        salir = False
        while not salir:
            termino_a_buscar = (str(input("--> Introduce término a buscar: ")))
            termino = ""
            termino = termino_a_buscar.lower()

            print(termino)
            if termino_a_buscar == "":
                salir = False
                print("\n*** No se ha introducido texto ***\n")
                buscar()
            else:
                if termino not in lista_minusculas:
                    print("*** El editor especificado no existe ***\n")
                else:
                    for juego in range(len(lista_aux)):
                        if lista_minusculas[juego] == termino:
                            corrige_duplicados.append(juego)
                            if juego in corrige_duplicados:
                                pass
                            else:
                                corrige_duplicados.append(juego)

                            # Devolvemos la lista de juegos del editor

            for i in corrige_duplicados:
                print(lista_aux[i]["Name"])
            salir = True

    if eleccion == "3":
        buscar()

    else:
        buscar()


def buscar():

    os.system("cls")
    head = ["Tipo de búsqueda"]
    data = [["\n1. Por nombre"], [("\n2. Por género")], [("\n3. Por editor")],
            [("\n4. Los 5 juegos más vendidos")], [("\n5. Salir")]]

    print(tabulate(data, headers=head, tablefmt="fancy_grid",
                   stralign='center'))

    eleccion = str(input("\n---> "))

    if eleccion == "1":
        print("\n")
        print("*** Has seleccionado búsqueda por nombre ***\n")
        termino_a_buscar = input("--> Introduce término a buscar: ")
        if termino_a_buscar == "":
            print("\n** No se ha introducido texto **\n")
            buscar()
        else:
            filtrado_nombre(termino_a_buscar)
            input("*** Pulsa enter para volver al menú ***")
            buscar()

    elif eleccion == "2":
        print("\n")
        print("*** Has seleccionado búsqueda por género ***\n")
        termino_a_buscar = input("--> Introduce término a buscar: ")
        if termino_a_buscar == "":
            print("\n** No se ha introducido texto **\n")
            buscar()
        else:
            filtrado_genero(termino_a_buscar)
            input("*** Pulsa enter para volver al menú ***")
            buscar()

    elif eleccion == "3":
        print("\n")
        print("*** Has seleccionado búsqueda por editor ***\n")
        filtrado_editor()
        input("*** Pulsa enter para volver al menú ***")

    elif eleccion == "4":
        gestion_juegos.max_globalsales()
        buscar()
    elif eleccion == "5":
        os.system("cls")
    else:
        print("\n*** No se ha introducido una de las opciones ***\n")

# print(formateador_nombres(contenidocsv))
# print((formateador_generos(contenidocsv)))
# formateador_editores(contenidocsv)
