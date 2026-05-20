op=0
saldo= 500000
# esto es un menu con comando if es del ejercicio de experiencia de aprendizaje 2

while True:
    print("1) Ver mi saldo")
    print("2) Retirar Dinero")
    print("3) Salir")
    
    
    try:
        op=int(input("ingrese una opcion: "))
        if op>0 and op<4:

            if op==1:
                print(f"su saldo es {saldo}")
                contop=int(input("ingrese un numero para volver 1)volver atras 2)salir"))
                if contop==2:
                    print("Cerrando sesion exitoso, adios")
                    break

            if op==2:
                try:
                    retiro=int(input("cuanto desea retirar: "))
                    if retiro>=saldo:
                        print("su retiro no puede igual o exceder su saldo")
                    elif retiro<0:
                        print("porfavor escriba una opcion correcta")
                    else:
                        # el else esta para evitar que quede en saldo 0 ahora si cambiamos la linea 25 a "retiro>saldo" si se podria descontar el saldo
                        saldo=saldo-retiro
                        print(f"quedan ${saldo}")
                except:
                    print("ingrese numeros porfavor!")
            if op==3:
                print("Cierre de sesion exitoso, adios")
                break
        else:
            print("seleccion fuera de rango")
    except:
        print("ingreso erroneo")