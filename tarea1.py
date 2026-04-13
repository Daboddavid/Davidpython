# calclar el puntaje de credito
# debe de calcular cuanto credito tiene una persona
# debo considerar cantidad de ingresos ,  nivel educacion al y nacionalidad
# cantidad de ingresos
# 500.000 a 1.000.000 : 300.000
# 1.500.001 o mas : 1.000.000
# nivel educacional Basico x1 , Medio: x1.3 , superior x1.5
# nacionalidad | chilena: +300.000 , extranjera: +0



credito=0


ingreso=int(input("ingrese su sueldo: "))
print("ingrese su nacionalidad")
print("1) Basico")
print("2) Medio")
print("3) Superior")
edu=int(input("nivel educacional: "))
nacionalidad=input("ingrese su nacionalidad (chilena/otro): ")

if ingreso>500000 and ingreso<= 1000000:
    credito=credito+300000
elif ingreso>1000001 and ingreso<= 1500001:
    credito=credito+1000000
else:
    print("no obtiene creditos por su ingreso")

if edu==1:
    print("no hay creditos por su nivel de educacion")
elif edu==2:
    credito=credito*1.3
elif edu==3:
    credito=credito*1.5

if nacionalidad=="chilena":
    credito=credito+300000
else:
    print("no existen creditos por su nacionalidad")

print("su puntaje de credito es: ", credito)