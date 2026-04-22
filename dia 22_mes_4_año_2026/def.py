# name="david"

# def saludo():
#     print(f"hola como estan")
# saludo()
# def despedida():
#     print(f"ya nos vamos? {name}")
# despedida()

def suma():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print(f"el resultado es {n1+n2}")

def resta():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print(f"el resultado es {n1-n2}")

def multiplicacion():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print(f"el resultado es {n1*n2}")

def division():
    n1=int(input("ingrese un numero: "))
    n2=int(input("ingrese otro numero: "))
    print(f"el resultado es {n1/n2}")

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
            suma()
        case 2:
            resta()
        case 3:
            multiplicacion()            
        case 4:
            division()
        case 5:
            print("salida")
        case _:
            print("opcion invalida")

