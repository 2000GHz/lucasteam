import gestion_juegos
import buscador
import os


def pedirNumero():
    correcto = False
    num = 0
    while (not correcto):
        try:
            print("\n    ******LUCASTEAM******\n")
            print("1) Listar CSV")
            print("2) Búsqueda de juegos")
            print("3) Añadir juegos")
            print("4) Salir ")
            num = int(input("\n--> Introduce una opción: "))
            if num == 1:
                print("\n=======Listar CSV=======\n")
                os.system("cls")
                correcto = True
                print("\n=======Listar CSV=======\n")
                n = int(input("***Pon el numero de filas que quieres mostrar: "))
                gestion_juegos.list_all_csv(n)
            if num == 2:
                print("\n=======Buscar juego=======\n")
                os.system("cls")
                correcto = True
                buscador.buscar()
            elif num == 3:
                print("\n=======Añadir juego=======\n")
                os.system("cls")
                gestion_juegos.add_games()
            elif num == 4:
                correcto = True
                os.system("cls")
            else:
                print("\n***Introduce una opción válida***\n")
                correcto = False
                os.system("cls")
        except ValueError:
            print("***Error, introduce un número entero***\n")
            os.system("cls")
        except Exception as e:
            print(e)