categoria=0
ijo=0
M=0
T=0
E=0

while True:
    try:
        ijo=int(input("ingrese la cantidad de juegos a evaluar: "))
        break
    except ValueError:
        print("ingrese numeros porfavor!!")
for i in range (ijo):
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
            
            E+=1
        elif edclas>=12 and edclas<17:
            print(f"{njuego} esta clasificado para adolescentes (+12)")
            
            T+=1
        else:
            print(f"{njuego} esta clasificado para personas mayores de 18 (+18)")
           
            M+=1
        break

print(f"la cantidad de juegos fueron {ijo} ")
print(f"de esos juegos habian , {E} para todos , {T} para adolescentes y {M} para adultos")


