# ejemplo y explicacion de match
op=0
total=0
while op != 4:
    print("1.- Radio stereo Sony $70.000")
    print("2.- LGTV 55 pulgadas $500.000")
    print("3.- PS5 $680.000")
    print("4.- Salir")
    print("seleccione una opcion")
    op=int(input())

    match op:
        case 1:
            print("El precio a pagar es",70000*1.19)
            total+=70000*1.19
        case 2:
            print("El precio a pagar es",500000*1.19)
            total+=500000*1.19
        case 3:
            print("El precio a pagar es",680000*1.19)
            total+=680000*1.19
        case 4:
            print("salida")
        case _:
            print("opcion invalida")   #opcion por defecto
print("su total es: ", total)
