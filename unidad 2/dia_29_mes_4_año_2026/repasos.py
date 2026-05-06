# repaso de for

import random

# for i in range(random.randint(1.8)):
#     print("hola mundo")
# ----------------------------------------------------repaso match----------------------------------------------------------
op=0
cantpersonas=0
niño=0
adulto=0
adultomayor=0
total=0

while op!=4:
    print('''
    1) niño (1-17) 1000
    2) adulto (18-64) 3000
    3) Adulto mayor (64 o mas) 1500
    4) salir''')

    op=int(input("Seleccione una opcion: "))
    match op:
        case 1:
            # limitar la cant de personas 1 a 10
            niño=int(input("cuantos niños son(entradas limitadas a 10 niños max): "))
            while niño<1 or niño>10:
                print("ingrese denuevo la cantidad")
                niño=int(input("cuantos niños son(entradas limitadas a 10 niños max): "))
                total+=1000*niño
                cantpersonas+=niño
        case 2:
            adulto=int(input("cuantos adultos son: "))
            total+=3000*adulto
            cantpersonas+=adulto
        case 3:
            adultomayor=int(input("cuantos adultos mayores son: "))
            total+=1500*adultomayor
            cantpersonas+=adultomayor
        case 4:
            print("saliendo")
            print(f"el total a pagar es: {total}")
            print(f"el total de personas es: {cantpersonas}")
        case _:
            print("opcion invalida")