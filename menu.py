def pedirNumero():

    correcto = False
    num = 0
    while (not correcto):
        try:
            print("1) Búsqueda de juegos")
            print("2) Añadir juegos")
            print("4) Salir")
            num = int(input("Introduce una opción: "))
            correcto = True

        except ValueError:
            print('Error, introduce un número entero')

        if num == 1:
            print("=======Buscar juego=======")
            from gestion_juegos import get_CSV
        elif num == 2:
            print("=======Añadir juego=======")
            from gestion_juegos import add_games
        elif num == 4:
            correcto = True
        else:
            print("Introduce una opción")
            correcto = False


pedirNumero()