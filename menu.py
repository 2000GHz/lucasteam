import gestion_juegos
import buscador


def pedirNumero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            print("\n    ******LUCASTEAM******\n")
            print("1) Búsqueda de juegos")
            print("2) Añadir juegos")
            print("3) Salir ")
            num = int(input("\n--> Introduce una opción: "))
            if num == 1:
                print("\n=======Buscar juego=======\n")
                correcto = True
                buscador.buscar()
            elif num == 2:
                print("\n=======Añadir juego=======\n")
                gestion_juegos.add_games()
            elif num == 3:
                correcto = True
            else:
                print("\n***Introduce una opción válida***\n")
                correcto = False
        except ValueError:
            print("***Error, introduce un número entero***\n")
