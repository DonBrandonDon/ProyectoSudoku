import Reglas
import graficas

def sudokupe(listanew):
    w=1
    if w==1:
        lineB = "  |---------------------------------|"
        print("\n  |  1  2  3 |  4  5  6 |  7  8  9  |")
        print("  -----------------------------------")
        for x in range(9):
            for y in range(9):
                if ((x == 3 or x == 6) and y == 0):
                    print(lineB)
                if (y == 0):
                    print(str(x + 1), "|", end=" ")
                if (y == 3 or y == 6):
                    print("|", end=" ")
                print(" " + str(listanew[x][y]), end=" ")
                if (y == 8):
                    print(" |")
        print(lineB)



def juego():
    listanew, TSolucion = graficas.sol(2)
    sudokupe(listanew)
    r = True
    while r:
        fila=Reglas.pfila()
        col=Reglas.pcolumna()
        num=Reglas.pvalor()
        while not (int(num) == TSolucion[int(fila) - 1][int(col) - 1]):
            print("error el numero que ingreso es incorrecto vuelva a intentar")
            fila = Reglas.pfila()
            col = Reglas.pcolumna()
            num = Reglas.pvalor()
        if listanew[int(fila) - 1][int(col) - 1]!=0:
            print("este casillero ya estaba lleno")
        listanew[int(fila) - 1][int(col) - 1] = int(num)
        lista = ["si", "no"]
        print("¿desea continuar?----->", end="")
        m = input("si,no:")
        while not (m in lista):
            print("caracter invalido")
            m = input("si,no:")
        if (m == "no"):
            r = False
        else:
            sudokupe(listanew)
    return listanew,TSolucion

#----------------------------------------------------------------
#Implementando Guardado
def IngresaMatrizenM():
    nombre1=input("\nIngrese nombre del jugador: ")
    partida1=input("\nIngrese nombre de la partida: ")
    #Pidiendo nombre del jugador y de la partida
    lista =[]
    lista1=[]
    lista2=[]
    lista3=[]
    #listas que contienen
    a,b=juego()
    lista.append(a)
    lista1.append(b)
    lista2.append(nombre1)
    lista3.append(partida1)
    return lista[0],lista1[0],lista2[0],lista3[0]
#----------------------------------------
def OptionOfSave():
    while True:
        option = ["si", "no"]
        print("\n¿Desea guardar la partida?----->", end="")
        m = input("si,no: ")
        if m in option:
            return m
        else:
            print("\nCaracter invalido")
