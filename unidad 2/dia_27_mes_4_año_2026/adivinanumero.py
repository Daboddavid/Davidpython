'''crea un numero random entre 1 y 100 pida al usuario que adivine el numero
si el usuario pone un numero mayoral generado debe decir "te pasaste", en caso contrario
el numero ha adivinar es menor
solo hay 5 posibilidades de adivinar'''

import random

numa=random.randint(1,100)
turno=1

adv=int(input("advinine un numero del 1 al 100"))

while adv<1 and adv>100:
    print("intente nuevamente numero fuera de rango")
    adv=int(input("advinine un numero del 1 al 100"))
while turno<5 and numa!=adv:
    print(f"turno" ,turno)
    if adv>numa:
        print("te pasaste")
    else:
        print("el numero a adivinar es mayor")
    adv=int(input("advinine un numero del 1 al 100"))
    while adv<1 and adv>100:
        print("intente nuevamente numero fuera de rango")
        adv=int(input("advinine un numero del 1 al 100"))
if adv==numa:
    print("has adivinado")
else:
    print("se te acabaron las oportunidades")




