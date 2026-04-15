# pida cantidad de alumnos
# por cada alumno , pida la cantidad de notas
# si aprueba o no
# mostrar cantidad alumnos aprobados y reprobados

alumno=int(input("ingrese la cantidad de alumnos: "))
sumaa=0
for e in range(alumno):

notas=int(input("ingrese la cantidad de notas: "))
sumap=0
for i in range (notas):
    n=float(input("ingrese la nota: "))
    sumap=sumap+n

prom=suma/notas
