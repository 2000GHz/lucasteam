import gestion_juegos


def filtrado_nombre(termino_a_buscar):

    diccionario_juego = []
    lista_aux = gestion_juegos.get_dict()
    for juego in range(len(lista_aux)):
        if lista_aux[juego]["Name"] == termino_a_buscar:
            # print(lista_aux[i])
            diccionario_juego = lista_aux[juego]

    return diccionario_juego


def filtrado_genero(termino_a_buscar):

    lista_aux = gestion_juegos.get_dict()
    print("La lista de juegos del género",
          termino_a_buscar, "es: ")
    for juego in range(len(lista_aux)):
        if lista_aux[juego]["Genre"] == termino_a_buscar:
            print(lista_aux[juego]["Name"])
    return "\nPrograma finalizado"


def buscar():

    salir = False
    eleccion = filtrar_por()
    while (not salir):
        try:
            termino_a_buscar = str(input("-->Introduce un término a buscar: "))

            if eleccion == "1":
                valoresfiltrados = filtrado_nombre(termino_a_buscar)
                salir = True

            if eleccion == "2":
                valoresfiltrados = filtrado_genero(termino_a_buscar)
                salir = True

            # valoresfiltrados = filtrado_genero(termino_a_buscar)

            """Si el parámetro introducido en filtrado_termino_a_buscar() no
            se encuentra en el diccionario la longitud devuelta es igual a 0"""

            if len(valoresfiltrados) == 0:
                if termino_a_buscar == '':
                    print("No se ha introducido texto")
                    buscar()  # Se vuelve a pedir la entrada

                """Se crea un subbucle para manejar cualquier entrada
                   no contenida en el diccionario distinta de 0
                """
                salir_subbucle = False

                while not salir_subbucle:
                    add_game_prompt = str(input(
                        "\n***No se encuentra ningún juego con estas" +
                        " características en la base de datos," +
                        " ¿Te gustaría añadirlo?***\n \n1. Sí\n2. No"
                        + "\n3. Realizar otra búsqueda\n\n---> "))
                    if add_game_prompt == '1':
                        salir_subbucle = True
                        gestion_juegos.add_games()
                    elif add_game_prompt == '2':
                        print("================¡Hasta luego!=================")
                        salir_subbucle = True
                    elif add_game_prompt == '3':
                        salir_subbucle = True
                        print('\n')
                        buscar()
                    else:
                        print("\n=====Introduce un valor correcto=====")
            else:
                print(valoresfiltrados)
                salir = True

        except Exception:
            print("***¡Error, revisa la entrada e inténtalo de nuevo!***")


def filtrar_por():
    salir = False
    try:
        while not salir:
            print("===Tipo de búsqueda===")
            print("\n 1. Por nombre")
            print("\n 2. Por género")
            eleccion = str(input("\n---> "))
            if eleccion == "1":
                print("\n")
                print("***Has seleccionado búsqueda por nombre***\n")
                salir = True

            if eleccion == "2":
                print("\n")
                print("***Has seleccionado búsqueda por género***\n")
                salir = True

    except ValueError:
        print("***¡Se ha producido un error, inténtalo de nuevo!***")
    return eleccion


