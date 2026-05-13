
op=0
saldoinicial=100000
ret=0
dep=0

while op!=4:
    print("bienvenido al sistema seleccione una opcion: ")
    print("1)consultar saldo")
    print("2)retirar dinero")
    print("3)depositar dinero")
    print("4)salir del programa")

    op=int(input("seleccionando opcion: "))

    match op:
        case 1:
            print(f"su saldo es: ${saldoinicial}")
        case 2:
            try:
                ret=int(input("por cuanto desea retirar?(escriba montos de $5000):"))
                if ret%5000==0:
                    print("retirando dinero")
                    saldoinicial-=ret
                else:
                    print("ingrese un monto correcto")
            except ValueError:
                print("ingrese un numero porfavor!")
        case 3:
            try:
                dep=int(input("cuanto desea depositar?(escriba montos $5000): "))
                if dep%5000==0:
                    print("depositando dinero")
                    saldoinicial+=dep
                else:
                    print("ingrese un monto correcto")
            except ValueError:
                print("ingrese un numero porfavor!")
        case 4:
            print("saliendo del programa")
            print(f"su saldo final es de {saldoinicial}")
        case _:
            print("opcion invalida")


