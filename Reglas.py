def pfila():
    solo = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cro=False
    while (not cro):
        fil=input("\ningrese fila: ")
        if fil in solo:
            cro=True
        else:
            print("caracter invalido")
    return fil

def pcolumna():
    solo = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cro=False
    while (not cro):
        colu=input("ingrese columna: ")
        if colu in solo:
            cro=True
        else:
            print("caracter invalido")
    return colu

def pvalor():
    solo = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    cro=False
    while (not cro):
        nume=input("ingrese valor: ")
        if nume in solo:
            cro=True
        else:
            print("caracter invalido")
    return nume

