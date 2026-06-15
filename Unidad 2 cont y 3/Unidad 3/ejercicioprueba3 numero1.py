parking={1:[],
         2:[],
         3:[],
         4:[]
         }

import random



def menuparking():
    while True:
        try:
            print("bienvenido al menu de parking")
            print("1)ingresar vehiculo")
            print("2)contar ganancias")
            print("3)contar vehiculos")
            print("4)ganancia promedio")
            print("5)mostrar pisos")
            print("6)salir del programa")
            op=int(input("que opcion desea seleccionar: "))
        except ValueError:
            print("ingrese solo numeros")
            
        match op:
            case 1:
                auto=int(input("ingrese el tipo de vehiculo:\n1 ligero \n2 mediano \n3 pesado"))
                piso=int(input("en que piso quedara?(1/2/3/4): "))
                if len(parking[piso])<10:
                    if auto==1:
                        parking[piso].append(2000)
                    elif auto==2:
                        parking[piso].append(3000)
                    elif auto==3:
                        parking[piso].append(3500)
                    else:
                        print("vehiculo no valido")
                else:
                    print("el piso esta lleno")
            case 2:
                # for piso,espacios in parking.items():     #creo que esto tambien funciona pero me va a contar el precio por los pisos
                #     totalparking=sum(espacios)
                #     print(f"${totalparking}")
                print("conteo ganancias")
                totalganancias=0
                for pesos in parking.values():
                    totalganancias+=sum(pesos)
                print(f"el total ganancias es {totalganancias}")
            case 3:
                totalvehiculos=sum(len(lista) for lista in parking.values())
                print(f"el total de vehiculos es: {totalvehiculos}")
            case 4:
                totalprom=0
                pisosusados=0 #revisar el github del profe

            case 5:
                for piso,espacios in parking.items():
                    print(f"piso {piso} : {espacios}")
            case 6:
                print("saliendo")
                break
            case _:
                print("ingrese una opcion valida")


menuparking()