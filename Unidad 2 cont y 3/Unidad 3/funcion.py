#ejemplo de funciones

#----------------------------------------sin argumento y sin retorno
# def saludo():
#     print("hola como estamos...")

# saludo()

# #-------------------------------------sin argumento y con retorno
# def suma():
#     num1=3
#     num2=5
#     return(num1+num2)
# resultadosum=suma()
# print(resultadosum)

# def esmayor():
#     edad=24
#     if edad>=18:
#         return True
#     else:
#         return False
# print(esmayor)


# #---------------------------------------con argumento y sin retorno

# def saludaMe(name):
#     print(f"hola {name} porque no me envia unos wasa")
# saludaMe("mario")

# def caculaIVA(neto):
#     print(f"el precio con IVA es: {neto*1.19}")
# caculaIVA(1000)

# #---------------------------------------con argumento y con retorno

def sumaCA(n1,n2):

    return(n1+n2)

def calculaIVACA(neto):
    return neto*1.19

print("el resultado es:",sumaCA(7,10))
print("el total con iva es: ",calculaIVACA(10000))

