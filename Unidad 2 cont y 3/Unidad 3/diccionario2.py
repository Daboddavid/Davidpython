vegetales={
    1:"maracuya",
    2:"pera",
    3:"cebolla",
    4:"papa"
}
# print(list(vegetales.items())[-1])  #lista la key y el valor
# print(list(vegetales.keys())[-1])   #El ultimo key de la lista

# for num,nombre in vegetales.items():
#     print(f"{num}={nombre}")



def mostrarvegetales():
    print("-"*26)
    for num,nombre in vegetales.items():
        print(f"{num}={nombre}")
def agregarvegetal():
    print("-"*20)
    agregar=input("ingresar")
    nuevokey=list(vegetales.keys())[-1]
    vegetales[nuevokey]=agregar
def eliminarvegetal():
    mostrarvegetales()
    elim=int(input("ingrese el numero del vegetal que desea eliminar: "))
    del vegetales[elim]
def actualizarvegetal():
    actual=input("Que vegetal desea sobrescribir: ")
    vegetales.update(actual)

def vegetalesmenu():
    op=0
    while True:
        try:
            print("-"*20)
            print("1) agregar vegetal")
            print("2) eliminar vegetal")
            print("3) actualizar vegetal")
            print("4) mostrar vegetal")
            print("5) salir")
            op=int(input("seleccione opcion: "))
            match op:
                case 1:
                    agregarvegetal()
                case 2:
                    eliminarvegetal()
                case 3:
                    actualizarvegetal()
                case 4:
                    mostrarvegetales()
                case 5:
                    print("saliendo del programa")
                    break
                case _:
                    print("opcion invalida")
        except:
            print("ingrese numeros")

vegetalesmenu()