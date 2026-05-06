# recorriendo palabras
# cuenta la cantidad de caracteres
# cuenta la cantidad de vocales

# nombre=input("ingrese su nombre: ")
# cant=0
# for i in nombre:
#     print(i)
#     cant+=1
# # cant=cant+1


# print("la cantidad de letras es", cant)

nombre=input("ingrese su nombre: ")
vocales=0
conso=0

for i in nombre:
    print(i)
    if i in "aeiouAEOIU":
        vocales+=1
    else:
        conso+=1


# cant=cant+1


print("la cantidad de letras es", vocales)
print("consotnantes: ", conso)

