'''
Fabrica de enlatados
Se necesita hacer el algoritomo de productos enlatados
Se debe consultar el peso del producto( en gramos) ( solo valores positivos)
El porcentaje de sodio en él ( solo valores entre 1 y 100)
y si se va a vender nacional o internacionalmente
Considerar los criterios en la siguiente tabla

menos de 500 grs, lata normal
501 hassta 1500 bgr, lata mediana
1501 y mas , lata grande
si el sodio es menos de 5%, lata queda igual
si es entre 5% y 8% lata especial
si tiene 9% o mas, lata acorazada
a las latas internacionales, se le debbe pegar 
in sticker de validacion sanitaria

Ej:800, 7%, 2==> lata mediana espacial con sticker sanitario
'''
gr=0
pr=0


while True:
    print("productos enlatados")
    try:
        gr=int(input("cuanto pesa el producto en cuestion en gramos: "))
        if gr<0:
            print("ingrese un numero correcto")
            break
    except ValueError:
        print("ingrese un numero porfavor!")

    if gr<500:
        print("producto ingresado como lata normal")
    elif gr>=501 and gr<=1500:
        print("producto ingresado como lata mediana")
    else:
        print("producto ingresado como lata grande")
        

    pr=int(input("cuanto es el porcentaje de sodio en cuestion en gramos(1 a 100): "))

   
    while glob!=2:

        glob=input("se va a vender 1)nacionalmente o 2)internacionalmente ?")
        match glob:
            case 1:
                print("")
            case 2:
                print("con sticker")
            case _:
                print("opcion invalida")


print(gr , pr , glob)



