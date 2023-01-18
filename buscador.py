import gestion_juegos


def termino_busqueda():

    Salir = False
    while (not Salir):
        try:
            nombre = str(input("Introduce un término de búsqueda: "))
            valoresfiltrado = filtrado_nombre(nombre)

            """Si el parámetro introducido en filtrado_nombre() no se encuentra
            en el diccionario, la longitud devuelta es igual a 0"""

            if len(valoresfiltrado) == 0:
                if nombre == '':
                    print("No se ha introducido texto")
                    termino_busqueda()  # Se vuelve a pedir la entrada

                """Se crea un subbucle para manejar cualquier entrada
                   no contenida en el diccionario distinta de 0
                """
                salir_subbucle = False

                while not salir_subbucle:
                    add_game_prompt = str(input(
                        "\nEl juego no se encuentra en la base" +
                        " de datos,¿Te gustaría añadirlo?\n1. Sí\n2. No"
                        + "\n3. Realizar otra búsqueda "))
                    if add_game_prompt == '1':
                        salir_subbucle = True
                        # add_games()
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
        except Exception:
            print('Error, revisa la entrada e inténtalo de nuevo.')


def filtrado_nombre(nombre):

    diccionario_juego = []
    lista_aux = gestion_juegos.get_dict()
    for i in range(len(lista_aux)):
        if lista_aux[i]["Name"] == nombre:
            # print(lista_aux[i])
            diccionario_juego = lista_aux[i]

    return diccionario_juego


def filtrado_genero(nombre):

    diccionario_juego = []
    lista_aux = gestion_juegos.get_dict()
    for i in range(len(lista_aux)):
        if lista_aux[i]["Genre"] == nombre:
            # print(lista_aux[i])
            diccionario_juego = lista_aux[i]

    return diccionario_juego