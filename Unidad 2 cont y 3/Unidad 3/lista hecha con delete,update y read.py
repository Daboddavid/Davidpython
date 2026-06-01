# colores=["blanco","negro","purpura","naranja"]

# for c in colores:
#     print(c)

# agregar=input("ingresa un color: ")

# colores.append(agregar)

# for c in colores:
#     print(c)
#CRUD = Create Read Update Delete

juguetes=["yo-yo","pelota"]

def mostrarjuguetes():
    for j in range(len(juguetes)):
        print(f"{j+1}){juguetes[j]}")

while True:
    print("1)ingresar un juguete")
    print("2)eliminar un juguete")
    print("3)actualizar un juguete")
    print("4)mostrar juguete")
    print("5)Salir")
    try:
        op=int(input("seleccione una opcion: "))
    except ValueError:
        print("ingrese no solo numeros")
        
    match op:
        case 1:
            agrejug=input("ingrese un juguete nuevo: ")
            juguetes.append(agrejug)
        case 2:
            eliminar=int(input("cual desea eliminar: "))
            # if eliminar in juguetes:
            #     juguetes.remove(eliminar)
            #     print("elemento eliminado" , juguetes)
            # else:
            #     print("este juguete no esta en la lista")
            juguetes.pop(eliminar-1)   #este es para los indices ej: yo-yo => 0 y pelota => 1
            print(f"{juguetes[eliminar-1]}fue eliminado correctamente")
        case 3:
            mostrarjuguetes()
            actualizar=int(input("Que juguete desea actualizar: "))
            juguetes[actualizar-1]=input("Ingrese el nuevo nombre: ")
        case 4:
            print("-"*20)
            mostrarjuguetes()
            print("-"*20)
                # c=1
                # for j in juguetes:
                #     print(f"{j+1}){juguetes[j]}")
                #     c+=1                                este es lo mismo que aqui arriba

        case 5:
            print("saliendo del programa")
            break
        case _:
            print("opcion invalida")
