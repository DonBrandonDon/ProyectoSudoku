
def MenuPrincipal():
    while True:
        print("")
        print("*-------------------------------------------------*\n")
        print("    *--------------MENU DE SUDOKU-------------*")
        print("""    |      *****TABLA DE OPCIONES*****        |
    *****---------------------------------*****
    |INICIAR PARTIDA                       [1]|
    |REGLAS DEL JUEGO                      [2]|
    |SALIR                                 [3]|
    *****---------------------------------*****

*-------------------------------------------------*\n""")

        opcion = input("Seleccione opción: ")
        if opcion in ["1", "2", "3", "4", "5"]:
            return opcion
        else:
            print("""\n+---------------------------------------+
|Opción no válida!!! Vuelva a intentarlo|
+---------------------------------------+\n""")

       # me retorna el def

def Submenu1():
    while True:
        print("")
        print("*-------------PARTIDAS--------------*")
        print("""\n|NUEVA PARTIDA                  [1]|
|REANUDAR PARTIDA               [2]|
|REGRESAR                       [3]|\n""")

        opcion = input("Seleccione opción: ")
        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print("""\n+---------------------------------------+
|Opción no válida!!! Vuelva a intentarlo|
+---------------------------------------+\n""")




def Submenu2():
    while True:
        print("\n----------Nueva Partida---------")
        print("\n NUEVO TABLERO               [1]\n REGRESAR                    [2] \n")
        opcion = input("Seleccione opción: ")
        if opcion in ["1", "2"]:
            return opcion
        else:
            print("""\n+---------------------------------------+
|Opción no válida!!! Vuelva a intentarlo|
+---------------------------------------+\n""")
        # me retorna el def


def Submenu3():
    while True:
        print("\n-----------TABLEROS------------")
        print(
            "\n|TABLEROS GUARDADOS             [1]|\n|REGRESAR                       [2]| \n")
        opcion = input("Seleccione opción: ")
        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print("""\n+---------------------------------------+
|Opción no válida!!! Vuelva a intentarlo|
+---------------------------------------+\n""")
         # me retorna el def
def Submenu4():
    while True:
        print("\n-----------TABLEROS------------")
        print(
            "\n|JUGAR TABLEROS GUARDADOS              [1]|\n|VISUALIZAR TABLEROS GUARDADOS         [2]| \n|REGRESAR                              [3]|\n")
        opcion = input("Seleccione opción: ")
        if opcion in ["1", "2", "3"]:
            return opcion
        else:
            print("""\n+---------------------------------------+
|Opción no válida!!! Vuelva a intentarlo|
+---------------------------------------+\n""")

def MenuRulers():
    while True:
        print("\n-----------Reglas del sudoku------------")
        print(
            "Regla 1: Hay que completar las casillas vacías con un solo número del 1 al 9.""\nRegla 2: En una misma fila no puede haber números repetidos.""\nRegla 3: En una misma columna no puede haber números repetidos.""\nRegla 4: En una misma región (De 3x3) no puede haber números repetidos.""\nRegla 5: La solución de un sudoku es única")
        print("\nParar volver al menú introdusca [1]")
        opcion = input("\nSeleccione opción: ")
        if opcion in ["1"]:
            return opcion
        else:
            print("""\n+---------------------------------------+
|Opción no válida!!! Vuelva a intentarlo|
+---------------------------------------+\n""")
        # me retorna el def





