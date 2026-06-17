op=0
total=0

while op!=4:
    
    print("bienvenido")
    print("1) galletas $1500")
    print("2) bebida 3lt $2000")
    print("3) papas $1800")
    print("4) salida del programa")
    try:    
        op=int(input("seleccione una opcion:  "))
    except ValueError as e:
         print("                       ")
         print("ingrese un numero porfavor!")
         print(e)
         print("                       ")
       

    match op:
        case 1:
            print("Ha seleccionado galletas")
            total+=1500
        case 2:
            print("ha seleccionado bebida 3lt")
            total+=2000
        case 3:
            print("ha seleccionado papas")
            total+=1800
        case 4:
            print("saliendo del programa")
        case _:
            print("escriba un numero valido")


print(f"su total a pagar es ${total}")