# vegetales={
#     1:"maracuya",
#     2:"pera",
#     3:"cebolla",
#     4:"papa"
# }
# print(list(vegetales.items())[-1])  #lista la key y el valor
# print(list(vegetales.keys())[-1])   #El ultimo key de la lista

# for num,nombre in vegetales.items():
#     print(f"{num}={nombre}")



# def mostrarvegetales():
#     print("-"*26)
#     for num,nombre in vegetales.items():
#         print(f"{num}={nombre}")
# def agregarvegetal():
#     print("-"*20)
#     agregar=input("ingresar")
#     nuevokey=list(vegetales.keys())[-1]
#     vegetales[nuevokey+1]=agregar
# def eliminarvegetal():
#     mostrarvegetales()
#     elim=int(input("ingrese el numero del vegetal que desea eliminar: "))
#     del vegetales[elim]
# def actualizarvegetal():
#     mostrarvegetales()
#     actual=int(input(("Ingrese el numero que desea sobrescribir: ")))
#     vegetales[actual]=input("ingrese el nombre que desea sobrescribir")

# # def vegetalesmenu():
#     op=0
#     while True:
#         try:
#             print("-"*20)
#             print("1) agregar vegetal")
#             print("2) eliminar vegetal")
#             print("3) actualizar vegetal")
#             print("4) mostrar vegetal")
#             print("5) salir")
#             op=int(input("seleccione opcion: "))
#             match op:
#                 case 1:
#                     agregarvegetal()
#                 case 2:
#                     eliminarvegetal()
#                 case 3:
#                     actualizarvegetal()
#                 case 4:
#                     mostrarvegetales()
#                 case 5:
#                     print("saliendo del programa")
#                     break
#                 case _:
#                     print("opcion invalida")
#         except:
#             print("ingrese numeros")

# vegetalesmenu()


#-----------------------------------------------------------------------------------------------------------------

productosDicc={
    1:{"nombre": "maracuya","precio":3000},
    2:{"nombre": "pera","precio":1500},
    3:{"nombre": "cebolla","precio":1200},
}
productosDicc[4]={"nombre": "piña","precio":3500}
          # diccionario con diccionario

print(productosDicc[2]["precio"]) #precio del vegetal
print(productosDicc[3]["nombre"]) #nombre del vegetal

def vegetalesMenuMostrar():
    for nombr,produc in productosDicc.items():
        print(f"{nombr} {produc} ")

def vegetalesMenuAgregar():
    nom=input("ingresar el nombre del producto: ")
    prec=int(input("ingrese el precio del producto: "))
    newk=list(productosDicc.keys())[-1]
    productosDicc[newk]={"nombre": nom,"precio":prec}

def vegetalesMenuEliminar():
    vegetalesMenuMostrar()
    elm=int(input("ingrese el numero del vegetal que desea eliminar: "))
    del productosDicc[elm]

def vegetalesMenuActualizar():
    vegetalesMenuMostrar()
    uptpk=int(input("ingrese el numero del prodcuto a sobrescribir: "))
    uptn=input("sobrescribir el nombre del producto:")
    uptp=int(input(("sobrescribir el precio del: ")))

    productosDicc[uptpk]={"nombre": uptn,"precio":uptp}

def vegetalesMenuDiccionario():
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
                    vegetalesMenuAgregar()
                case 2:
                    vegetalesMenuEliminar()
                case 3:
                    vegetalesMenuEliminar()
                case 4:
                    vegetalesMenuMostrar()
                case 5:
                    print("saliendo del programa")
                    break
                case _:
                    print("opcion invalida")
        except:
            print("ingrese numeros")


vegetalesMenuDiccionario()