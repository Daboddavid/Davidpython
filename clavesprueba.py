


# Pedir password y pin
# pida al usuario password en palabra que debe ser "TEMU"
# ADEMAS pida el pin debe ser 3435
# los dos deben estar correcto para acceder al sistema



print("ingrese usuario y contraseña ")
pog="Temu"
clv=3435
us=input("Usuario ")
clav=int(input("password "))

if us==pog and clav==clv :
    print("clave correcta puede proceder")
else:
    print("clave incorrecta intente denuevo")
