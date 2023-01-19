import gestion_juegos
import menu
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
    for juego in range(len(contenidocsv)):
        juegos = contenidocsv[juego]["Publisher"]
        lista_editores.append(str(juegos).lower())
    return lista_editores


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

    juegoexiste = False

    if nombreminusculas in lista_nombres_minusculas:
        juegoexiste = True
        for juego in range(len(contenidocsv)):
            if lista_nombres_minusculas[juego] == nombreminusculas:
                diccionario_juego = contenidocsv[juego]
                print(diccionario_juego)
    else:
        juegoexiste = False

        if not juegoexiste:
            add_game_prompt = str(input(
                "\n***No se encuentra ningún juego con este" +
                " nombre en la base de datos," +
                " ¿Te gustaría añadirlo?***\n \n1. Sí\n2. No"
                + "\n3. Realizar otra búsqueda\n\n---> "))
            if add_game_prompt == '1':
                gestion_juegos.add_games()
            elif add_game_prompt == '2':
                print("================¡Hasta luego!=================")
            elif add_game_prompt == '3':
                print('\n')
                buscar()
            else:
                print("\n=====Introduce un valor correcto=====")

        return diccionario_juego


def filtrado_genero(termino_a_buscar):

    termino = ""
    termino = termino_a_buscar.capitalize()
    print(termino)

    lista_aux = contenidocsv

    generos = formateador_generos(contenidocsv)
    print(generos)

    if termino not in generos:
        print("*** El género especificado no existe ***")
    else:
        for juego in range(len(lista_aux)):
            if lista_aux[juego]["Genre"] == termino:

                # Devolvemos la lista de juegos correspondientes a este género

                print(lista_aux[juego]["Name"])


def filtrado_editor(termino_a_buscar):
    diccionario_juego = contenidocsv

    nombreminusculas = termino_a_buscar.lower()
    lista_nombres_minusculas = formateador_nombres(contenidocsv)

    juegoexiste = False

    if nombreminusculas in lista_nombres_minusculas:
        juegoexiste = True
        for juego in range(len(contenidocsv)):
            if lista_nombres_minusculas[juego] == nombreminusculas:
                diccionario_juego = contenidocsv[juego]
                print(diccionario_juego)
    else:
        juegoexiste = False

        if not juegoexiste:
            add_game_prompt = str(input(
                "\n***No se encuentra ningún juego con este" +
                " nombre en la base de datos," +
                " ¿Te gustaría añadirlo?***\n \n1. Sí\n2. No"
                + "\n3. Realizar otra búsqueda\n\n---> "))
            if add_game_prompt == '1':
                gestion_juegos.add_games()
            elif add_game_prompt == '2':
                print("================¡Hasta luego!=================")
            elif add_game_prompt == '3':
                print('\n')
                buscar()
            else:
                print("\n=====Introduce un valor correcto=====")

        return diccionario_juego


def buscar():

    salir = False
    eleccion = filtrar_por()
    while (not salir):

        if eleccion == "1":
            termino_a_buscar = (str(input("--> Introduce término a buscar: ")))
            if termino_a_buscar == "":
                print("\n*** No se ha introducido texto ***\n")
                salir = False
            else:
                salir = True
            filtrado_nombre(termino_a_buscar)

        if eleccion == "2":
            termino_a_buscar = (str(input("--> Introduce término a buscar: ")))
            if termino_a_buscar == "":
                print("\n*** No se ha introducido texto ***\n")
                salir = False
            else:
                salir = True
            filtrado_genero(termino_a_buscar)
            
        if eleccion == "3":
            termino_a_buscar = (str(input("--> Introduce término a buscar: ")))
            if termino_a_buscar == "":
                print("\n*** No se ha introducido texto ***\n")
                salir = False
            else:
                salir = True
            filtrado_editor(termino_a_buscar)
        break


def filtrar_por():
    salir = False
    while not salir:
        print("===Tipo de búsqueda===")
        print("\n1. Por nombre")
        print("\n2. Por género")
        print("\n3. Por editor")
        print("\n4. Salir")

        eleccion = str(input("\n---> "))

        if eleccion == "1":
            print("\n")
            print("*** Has seleccionado búsqueda por nombre ***\n")
            salir = True
        if eleccion == "2":
            print("\n")
            print("*** Has seleccionado búsqueda por género ***\n")
            salir = True
        if eleccion == "3":
            print("\n")
            print("*** Has seleccionado búsqueda por editor ***\n")
            salir = True
        if eleccion == "4":
            menu.pedirNumero()
            salir = True
        if eleccion == "":
            print("\n*** No se ha introducido texto ***\n")
    return eleccion

# print(formateador_nombres(contenidocsv))
# print((formateador_generos(contenidocsv)))
