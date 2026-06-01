
'''
Modificar el programa del carrito de compras
para poder utilizarlo con listas
'''
productos=[]
op=0
while op!=4:
    print("1) Agregar producto")
    print("2) Mostrar producto")
    print("3) Eliminar producto")
    print("4) Salir del sistema")
    try:
        op=int(input("seleccione una opcion: "))
    except ValueError:
        print("ingrese numeros porfavor")
match op:
    case 1:
        nombre=input("ingrese nombre del producto")
        precio=int(input("ingrese el precio del producto: "))

