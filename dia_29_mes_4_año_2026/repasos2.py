#  preguntar el folio de una entrada a un concierto. validar que los folios esten entre 7000 y 21000
# preguntar si estan en cancha vip, general o tribuna
# cada entrada vale 40000, para los impuestos son
# vip*1.8, general *1.4 y tribuna *1.2
# mostrar el valor a pagar al final
entrada=40000
total=0
folio=int(input("numero de su folio:"))
while folio<7000 or folio>21000:
    print("ingrese denuevo su numero de folio (no puede ser menor de 7000 o mayor que 21000)")
    folio=int(input("numero de su folio:"))

cancha=int(input('''Donde esta ubicada su entrada 
                  1) cancha vip
                  2) cancha general
                  3) cancha tribuna
                 Seleccione una opcion: '''))

match cancha:
    case 1:
        print("usted eligio cancha vip")
        total+=entrada*1.8
    case 2:
        print("usted eligio cancha general")
        total+=entrada*1.4
    case 3:
        print("usted eligio cancha tribuna")
        total+=entrada*1.2
    case _:
        print("opcion invalida")

print(f"su total a pagar es: {total}")



