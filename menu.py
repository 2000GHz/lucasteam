import gestion_juegos
import buscador
import os
from tabulate import tabulate


def pedirNumero():
    correcto = True
    os.system("cls")
    while correcto:
        try:
            col_name = ["\n  ******LUCASTEAM******\n"]
            data = [["1 · Líbrería de juegos"],
                    ["2 · Búsqueda de juegos"],
                    ["3 · Añadir juegos"],
                    ["4 · Salir "]]
            print(tabulate(data, headers=col_name, tablefmt="fancy_grid",
                           stralign='center'))
            num = int(input("\n---> Introduce una opción: "))
            if num == 1:
                print("\n=======Listar CSV=======\n")
                os.system("cls")
                print("\n=======Listar CSV=======\n")
                n = int(input("*** Introduce el numero" +
                              " de filas a mostrar ***\n"))
                print("\n")
                gestion_juegos.list_all_csv(n)
                os.system("cls")
            elif num == 2:
                print("\n=======Buscar juego=======\n")
                os.system("cls")
                buscador.buscar()
            elif num == 3:
                print("\n=======Añadir juego=======\n")
                os.system("cls")
                gestion_juegos.add_games()
            elif num == 4:
                correcto = False
                os.system("cls")
            else:
                print("\n*** Introduce una opción válida ***\n")
                os.system("cls")
        except ValueError:
            os.system("cls")
            print("\n*** Error, introduce un número entero ***\n")

        except Exception as e:
            print(e)
