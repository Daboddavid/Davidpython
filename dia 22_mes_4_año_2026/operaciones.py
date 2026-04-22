'''ingrese una operacion
1.- suma
2.- resta
3.- multiplicacion
4.- division
5.- salir
'''


oper=0
opci=0

while opci != 5:


    print("Seleccione una opcion")
    print("1) Suma")
    print("2) Resta")
    print("3) Multiplicacion")
    print("4) Division")
    print("Salida")
    opci=int(input())


    match opci:
        case 1:
            n1=int(input("ingrese un numero: "))
            n2=int(input("ingrese otro numero: "))
            print(f"el resultado es {n1+n2}")
        case 2:
            n1=int(input("ingrese un numero: "))
            n2=int(input("ingrese otro numero: "))
            print(f"el resultado es {n1-n2}")
        case 3:
            n1=int(input("ingrese un numero: "))
            n2=int(input("ingrese otro numero: "))
            print(f"el resultado es {n1*n2}")
        case 4:
            n1=int(input("ingrese un numero: "))
            n2=int(input("ingrese otro numero: "))
            print(f"el resultado es {n1/n2}")
        case 5:
            print("salida")
        case _:
            print("opcion invalida")

