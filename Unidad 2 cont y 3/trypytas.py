# try:
#     edad=int(input("escriba su edad: "))
# except ValueError as mostrarerror:
#     print("solo debe ingresar numeros enteros")
#     print(mostrarerror)


# while True:

#     try:
#         edad=int(input("ingrese su edad ")) #si hay error, salta a la linea 12
#         break
#     except ValueError as e:
#         print("solo se aceptan numeros enteros ")
#         print(e)
# print("su edad es", edad)


# for i in range(10):
#     n1=int(input("ingrese un numero: "))
#     if n1%2!=0:  #el resto de la division es distinto de 0 (esto es para detectar impares)
#         break



while True:
    try:

        n1=int(input("ingrese un numero: "))
        num+=n1
        if n1==0:
            break
    except:
        print("solo numero entero")

print("el total es: ", num)


