# pida cantidad de alumnos
# por cada alumno , pida la cantidad de notas
# si aprueba o no
# mostrar cantidad alumnos aprobados y reprobados

alumno=int(input("ingrese la cantidad de alumnos: "))
sumaa=0
apro=0
repro=0
for i in range(alumno):

    notas=int(input("ingrese la cantidad de notas del alumno : "))
    {i+1}
    sumap=0
    for j in range (notas):
        n=float(input("ingrese la nota: "))
        sumap=sumap+n
    prom=sumap/notas
    print("el promedio de las notas es: ", prom)
    if prom<=4:
        print("alumno aprobado")
        apro+=1
    else:
        print("alumno reprobado")
        repro+=1

print("la cantidad de alumnos que tomaron prueba fueron:",alumno)
print("la cantidad de alumnos aprobados es: ", apro )
print("la cantidad de alumnos reprobado es ", repro)