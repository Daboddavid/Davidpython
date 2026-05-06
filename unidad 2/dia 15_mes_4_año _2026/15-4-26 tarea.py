# no lo alcance a hacerlo asi que voy a dejarlo resuelto 
notas=int(input("ingrese la cantidad de notas "))
suma=0
for i in range (notas):
    n=float(input("ingrese la nota: "))
    suma=suma+n

prom=suma/notas
print("El promedio es ", prom)

if prom<=4:
    print("alumno aprobado")
else:
    print("alumno reprobado")