espacio=90
op=0
poner=0
sacar=0
ph=0
rh=0
while True:
    print("------bienvenido al sistema -------")
    print("1) espacios disponibles")
    print("2) poner libros")
    print("3) sacar libros")
    print("4) Historial ocupaciones")
    print("5) salir")
    print("------------------------------------")
    while True:
        try:
            op=int(input())
            break
        except:
            print("ingrese numeros enteros")
    match op:
        case 1:
            print(f"la cantidad de espacio disponible es {espacio}")
        case 2:
            poner=int(input("¿cuantos libros desea poner?: "))
            if espacio>=90:
                print("espacio maximo alcanzado")
            else:
                espacio=espacio+poner
                ph+=1
        case 3:
            sacar=int(input("¿cuantos libros desea sacar?: "))
            if espacio<0:
                print("no se pueden sacar mas libros")
            else:
                espacio=espacio-sacar
                rh+=1
        case 4:
            print("el historial de movimientos es: ")
            print(f"la cantidad de acciones de retiros es {rh} en esta sesion")
            print(f"la cantidad de acciones de agregado es {ph} en esta sesion")
        case 5:
            print("saliendo del programa")
            break
        case _:
            print("ingrese un numero correcto")

            
