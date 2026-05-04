print("ingrese una contraseña de 4 digitos")

pin=int(input())
# if len(str(pin))==4:
#     print("contraseña correcta, ingresando")
# else:
#     print("ingrese un pin correcto")

while len(str(pin))!=4:
    print("ingrese un codigo correcto")
    pin=int(input())
    

print("bienvenido al sistema")