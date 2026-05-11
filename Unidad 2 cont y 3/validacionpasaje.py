
pasaje=int(input("cuantos pasajes deseas vender: "))
totalingreso=0
# try:
#     for i in range(pasaje):
#         p=int(input("ingrese el valor de los pasajes "))
#         totalingreso+=p
        

# except ValueError as e:
#     print("ingrese un valor numerico")
#     print(e)


# finally:
#     print("el total ingreso " , totalingreso)




for i in range(pasaje):
    while True:
        try:
            p=int(input("ingrese el valor de los pasajes"))
            break
        except:
            print("dato no valido")

    totalingreso+=p

print(f"monto {totalingreso}")




