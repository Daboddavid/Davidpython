'''def a 3 programas y que los llamen con match'''

def prom_notas():
    alumno=int(input("ingrese la cantidad de alumnos: "))
    sumap=0
    apro=0
    repro=0
    for i in range(alumno):

        notas=int(input("ingrese la cantidad de notas del alumno : "))
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
def vocalcon_nom():
    nombre=input("ingrese su nombre: ")
    vocales=0
    conso=0
    for i in nombre:
        print(i)
        if i in "aeiouAEOIU":
            vocales+=1
        else:
            conso+=1
    # cant=cant+1
    print("la cantidad de vocales es", vocales)
    print("consotnantes: ", conso)
def mult_num():
    mult=int(input("ingrese un numero para multiplicar: "))
    for i in range (10):
        print(mult,"X" ,i+1, "=" , mult*(i+1))

opcion=0
while opcion != 4:
    opcion=int(input('''Seleccione una opcion
                    1) promedio de notas
                    2) Vocales y consonantes de un nombre
                    3) tabla multiplicar de un numero
                    4) Salida 
                     '''))
    match opcion:
        case 1:
            prom_notas()
        case 2:
            vocalcon_nom()
        case 3:
            mult_num()
        case 4:
            print("saliendo del programa")
        case _:
            print("opcion invalida")


