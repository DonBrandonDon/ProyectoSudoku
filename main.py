import Menús
import sudoku

# Variable global
lesta = []
lesta1 = []
lesta2 = []
lesta3 = []

print("\n+--------Bienvenido a mi programa de SUDOKU-------+")
while (opcion:=Menús.MenuPrincipal())!="3":
    if opcion=="1":
        while (opcion1:=Menús.Submenu1())!="3":
            if opcion1=="1":
                while(opcion1 := Menús.Submenu2()) != "2":
                    # nos esta retornando 4 variables
                    # w:tabla  e:solu  r:nomJ  t:nomT
                    guardatelo = w, e, r, t = sudoku.IngresaMatrizenM()
                    lesta.append(w)
                    lesta1.append(r)
                    lesta2.append(t)
                    lesta3.append(e)
                    solu = lesta3
                    nomJ = lesta1
                    nomT = lesta2
                    tab = lesta
                    sea = sudoku.OptionOfSave()
                    if sea == "si":
                        continue
                    else:
                        del tab[len(tab) - 1]
                        del nomT[len(nomT) - 1]
                        del nomJ[len(nomJ) - 1]
            elif opcion1=="2":
                while (opcion2 := Menús.Submenu3()) != "2":
                    if opcion2=="1":
                        while (opcion3 := Menús.Submenu4()) != "3":
                            nomJ = lesta1
                            nomT = lesta2
                            tab = lesta
                            if opcion3=="1":
                                for i in range(len(tab)):
                                    print([i + 1], f"{nomJ[i]:>8}", end="    ")
                                    print(f"{nomT[i]:<2}")
                                r = input("que numero de tabla quiere jugar?:")
                                print("aun no se inplemento el codigo de renudar partida guardada")
                            if opcion3=="2":
                                for i in range(len(tab)):
                                    print([i + 1], f"{nomJ[i]:>8}", end="    ")
                                    print(f"{nomT[i]:<2}")
                                    sudoku.sudokupe(tab[i])

    elif opcion=="2":
       Menús.MenuRulers()

print("\nGracias por jugar SUDOKU con nosotros.  uwu")

#Lab 1.07

#Integrantes:
#Roger Kevin Rodriguez Nolberto
#Brandon Aldrin Paitan Alva
#Linder Abel Santivañez Blanco