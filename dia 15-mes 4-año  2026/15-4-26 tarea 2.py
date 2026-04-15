# pida cantidad de alumnos
# por cada alumno , pida la cantidad de notas
# si aprueba o no
# mostrar cantidad alumnos aprobados y reprobados

alumno=int(input("ingrese la cantidad de alumnos: "))
sumaa=0
for i in range(alumno):

    notas=int(input("ingrese la cantidad de notas del alumno {i+1}: "))
    sumap=0
    for j in range (notas):
        n=float(input("ingrese la nota: "))
        sumap=sumap+n

    prom=suma/notas
