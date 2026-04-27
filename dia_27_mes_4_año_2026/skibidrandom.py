# # uso y explicacion de random

# import random as rd
# print(rd.randint(1,200))
 
import random
import time

# num=random.randint(1,10)

# for i in range(num):
    # print("hola")


# strike=random.randint(10,70)

# if strike>50:
#     print("It's a critical hit. Damage ",strike )
# else:
#     print("It's not very effective. Damage ",strike )


# '''3 personas juegan golf. Cada persona tiene la posibilidad de golpear
# y la distancia varia entre 60 y 190 metros
# mostrar al final el golpe mas fuerte'''

# j1=random.randint(90,190)
# j2=random.randint(90,190)
# j3=random.randint(90,190)

# # print(f"el turno del primer jugador hizo un golpe de ",j1, " metros")

# # print(f"el turno del segundo jugador hizo un golpe de ",j2, " metros")

# # print(f"el turno del tercer jugador hizo un golpe de ",j3, " metros")


# print(f"el jugador 1 golpeo la pelota a {j1} metros")
# print(f"el jugador 2 golpeo la pelota a {j2} metros")
# print(f"el jugador 3 golpeo la pelota a {j3} metros")

# if j1>j2 and j1>j3:
#     print("el jugador uno hizo el tiro mas lejano")
# elif j2>j3:
#     print("el jugador dos hizo el tiro mas lejano")
# else:
#     print("el jugador tres hizo el tiro mas lejano")

# # KILLER INSTINC
''' dospeleadores se piden al inicio de la pelea
cada peleador inicia con 100 hp
se debe hacer una pelea por turnos
se debe hacer una pelea por turnos y cada golpe varia entre 7 y 18
se termina el match cuando uno de los 2 tiene su hp menor o igual a 0
se debe mostrar el ganador al final'''

nam1=input("ingrese el nombre del jugador 1 ")
nam2=input("ingrese el nombre del jugador 2 ")




hp1=100
hp2=100
turno=random.randint(1,2)




while hp1>=0 and hp2>=0:

    if turno%2==0:
        print(f"turno de {nam1}")
        g=random.randint(7,18)
        print(f"{nam1} golpea a {nam2} con un golpe de {g}")
        hp2-=g
        print(f"el hp de {nam2} es {hp2}")
        time.sleep(1)
    else:
        print(f"turno de {nam2}")
        g=random.randint(7,18)
        print(f"{nam2} golpea a {nam1} con un golpe de {g}")
        hp1-=g
        print(f"el hp de {nam1} es {hp1}")
        time.sleep(1)
tunro+=1
print(nam1, "█"*hp1)
print(nam2, "█"*hp2)

if hp1>hp2:
    print("el ganador es ", nam1)
else:
    print("el ganador es ", nam2)