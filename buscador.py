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


def formateador_generos(contenidocsv):

    lista_generos_minusculas = []

    for juego in range(len(contenidocsv)):
        generos = contenidocsv[juego]["Genre"]
        lista_generos_minusculas.append(str(generos).lower())

    set_ordenador = set(lista_generos_minusculas)
    lista_generos_minusculas = set_ordenador

    return lista_generos_minusculas


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
    termino_a_buscar == termino_a_buscar.lower()
    lista_aux = contenidocsv
    generos = formateador_generos(contenidocsv)
    """if termino_a_buscar in listageneros:
        termino_a_buscar = termino_a_buscar.capitalize()"""

    if termino_a_buscar not in generos:
        print("*** El género especificado no existe ***")
    else:
        for juego in range(len(lista_aux)):
            if lista_aux[juego]["Genre"] == termino_a_buscar.capitalize():

                # Devolvemos la lista de juegos correspondientes a este género

                print(lista_aux[juego]["Name"])


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


def filtrar_por():
    salir = False
    while not salir:
        print("===Tipo de búsqueda===")
        print("\n 1. Por nombre")
        print("\n 2. Por género")
        print("\n3. Salir")

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
            menu.pedirNumero()
            salir = True
        if eleccion == "":
            print("\n*** No se ha introducido texto ***\n")
    return eleccion
# print(formateador_nombres(contenidocsv))
# print((formateador_generos(contenidocsv)))
