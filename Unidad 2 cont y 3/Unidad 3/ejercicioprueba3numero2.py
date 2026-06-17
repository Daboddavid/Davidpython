'''crear al gestor de pacientes en un centro medico
Para poner el nombre se debe validar que no este vacio
y ademas tenga mas de 8 caracteres
Para la prevision de salud solo exiten 3 posibles valores
Fonasa, Isapre, o Fodesa
Al ingresar un paciente, se debe poner la temperatura
Crear una funcion que valide si esta grave o no
Para que este grave debe tener mas de 39°
Cada atencion vale $25.000
Los despcuentos corresponden a 
FOnasa 54%
Isapre 27%
Fodesa 12,5%

'''
pacientes=[
     {"nombre": " Aquiles Baeza",
    "prevision": "Fonasa",
    "temperatura":34.6,
    "grave": False}

]

nombre=input("ingrese el nombre del paciente: ")


prev=input("ingrese el numero de la prevision que forma parte el paciente \n1) Fonasa \n2) Isapre \n3) Fodesa \n seleccione: ")
match op:
    case "1":
        print("ingresando fonasa")
    case "2":
        print("ingresando isapre")
    case "3":
        print("ingresando fodesa")
    case _:
        print("datos invalidos")
    
temp=float(input("ingrese la temperatura del paciente: "))
def validar_temp():
    if temp>39:
        return True
    else:
        return False



pacientes.append={"nombre":nombre,
                  "prevision":prev,
                  "temperatura":temp,
                  "grave":validar_temp(temp)
                  }