def pedirNumero():

    correcto = False
    num = 0
    while (not correcto):
        try:
            print("1. Opción 1")
            print("2. Opción 2")
            print("3. Opción 3")
            print("4. Salir")
            num = int(input("Introduce un número entero: "))
            correcto = True

        except ValueError:
            print('Error, introduce un número entero')

        if num == 1:
            print("Opción 1")
        elif num == 4:
            correcto = True
        else:
            print("Introduce un número 1 o 4")
            correcto = False


pedirNumero()