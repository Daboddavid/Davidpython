
pasajes=int(input("ingrese la cantidad de pasajes que desea vender: "))
totales=0

for i in range(pasajes):
    
    prec=int(input("ingrese el precio de cada pasaje: "))
    totales=totales+prec

print(f"la cantidad total de los pasajes es: {totales}")
