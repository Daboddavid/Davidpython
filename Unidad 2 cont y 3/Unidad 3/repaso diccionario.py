productosDicc={
    1:{"nombre": "maracuya","precio":3000},
    2:{"nombre": "pera","precio":1500},
    3:{"nombre": "cebolla","precio":1200},
}
# productosDicc[4]={"nombre": "piña","precio":3500}
#           # diccionario con diccionario

# for i in productosDicc.values(): #aca se necesita ver los values para poder printear los contenidos
#     print(i["nombre"],i["precio"])

# for nom,prod in productosDicc.items(): #aca se esta tomando el .item que toma todo lo de adentro del diccionario, sin embargo se toman dos indices "nom" y "prod"
#     print(prod["nombre"],prod["precios"])




# print(productosDicc.keys())
# print(productosDicc.values())
print(productosDicc.items())

# print(productosDicc[2]["precio"]) #precio del vegetal
# print(productosDicc[3]["nombre"]) #nombre del vegetal

# ------------------------------------------------------------------------------------------------------------------------

# pokemons={
#     1:{"nombre":"Eevee",
#        "nlv": 14,
#        "hp": 32,
#        "atk":
#        {
#            1:{"nombre":"placaje","daño":[16-24]},
#            2:{"nombre":"placaje","daño":[16-24]},
#            3:{"nombre":"placaje","daño":[16-24]},
#            4:{"nombre":"placaje","daño":[16-24]}
#        },
#        "def":10,
#        "type":"normal",
#        "vel":12,
#        }
# }

#------------------------------------------------------------------------------------------------------------------------
carrito=[]

def agregarproductoDICC():
    nomP=input("ingrese el nombre del producto: ")
    preP=int(input("ingrese el precio del producto: "))
    productosDicc[list(productosDicc.keys())[-1]+1]={"nombre": nomP ,"precio": preP }

def mostrarproductoDICC():
    print("-"*30)
    for nombre,precio in productosDicc.items():
        print(f"{nombre},{precio}")
    print("-"*30)

def eliminarproductoDICC():
    mostrarproductoDICC()
    borrar=input("cual producto desea borrar: ")
    del productosDicc[borrar]

def actualizarprodcutoDICC():
    mostrarproductoDICC()
    actualizar=int(input("cual producto desea actualizar: "))
    nombrenuevo=input("ingrese el nombre nuevo del producto: ")
    precionuevo=int(input("ingrese el precio nuevo del producto"))
    productosDicc[actualizar]={"nombre":nombrenuevo,"precio":precionuevo}

def comprarproductoDICC():
    while True:
        mostrarproductoDICC()
        try:
            compra=int(input("que producto desea comprar(para salir escriba 0): "))
            if compra==0:
                break
        
        except ValueError:
            print("ingrese solo numeros!!!")
        carrito.append(productosDicc[compra])
        print(carrito)

def boletaprodcutoDICC():
    total=0

    


def menuproductoDICC():
    while True:
        try:
            print("-"*30)
            print("---BIENVENIDO---")
            print("1)agregar producto")
            print("2)eliminar producto")
            print("3)actualizar producto")
            print("4)mostrar producto")
            print("5)comprar producto")
            print("6)Salir mostrar total y mostrar boleta a pagar")
            op=int(input("seleccione una opcion: "))
        except ValueError:
            print("porfavor ingrese numeros!!")
        match op:
            case 1:
                agregarproductoDICC()
            case 2:
                eliminarproductoDICC()
            case 3:
                actualizarprodcutoDICC()
            case 4:
                mostrarproductoDICC()
            case 5:
                comprarproductoDICC()
            case 6:
                print("salir")
                break
            case _:
                print("opcion invalida")

menuproductoDICC()
