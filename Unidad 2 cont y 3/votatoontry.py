# Votatoon

toon1=input("Ingrese el toon 1: ")
toon2=input("Ingrese el toon 2: ")

v1=0
v2=0

while True:
    try:
        cant=int(input("Cauntos votantes son? "))
        break
    except:
        print("solo se puede ingresar valores positivos")




while cant>0:
    # pedir votos
    voto=int(input(f"Por quien votará? 1.- {toon1} 2.- {toon2}: "))
    if voto==1:
        v1+=1
    elif voto==2:
        v2+=1
    else:
        print("Voto nulo")
    cant-=1

if v1>v2:
    print(f"Gano {toon1} con {v1} votos")
elif v2>v1:
    print(f"Gano {toon2} con {v2} votos")
else:
    print("Fue un empate")