categoria=0
classif=0
ijuego=0


while True:
        njuego=input("ingrese nombre del juego: ").upper().replace(" ","")
    
        if len(njuego) >5:
            break
        print ("ingrese alomenos 5 caracteres!")

while True:
    try:
        nprecio=int(input("ingrese el precio del juego: "))

        if nprecio < 20000 and nprecio <40000:
            print(f"{njuego} es un juego indie")
            categoria="indie"
        elif nprecio > 40000:
            print(f"{njuego} es un juego de estudio ")
            categoria="estudio"

        break
    except TypeError:
        print("ingrese solo numeros positivos")
while True:
    edclas=int(input("ingrese para que edad esta dirigida este juego: "))
    if edclas <12:
        print(f"{njuego} esta clasificado para todos")
        classif="E para todos"
    elif edclas>=12 and edclas<17:
        print(f"{njuego} esta clasificado para adolescentes (+12)")
        classif="T para adolescentes"
    else:
        print(f"{njuego} esta clasificado para personas mayores de 18 (+18)")
        classif="M para adultos"
    break


print(f"{njuego} tiene un precio de {nprecio}, {categoria} y esta clasificado como un juego {classif}")


# tengo que encontrar maneras de evitar los numeros negativos y ceros
# estudiar mas while true, try,except , break
# estudiar DEF
# tengo que colocar un FOR arriba


