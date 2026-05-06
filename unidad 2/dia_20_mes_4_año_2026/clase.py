# entrenador="Giovanni"
# pkm1=6
# entrenador2="Sabrina"
# pkmn2=7


# print(len(entrenador))  // aca verificia el lenght del strign
# estos son diferentes maneras para tomar strings

# print("El entrenador ", entrenador , "tiene ", pkm1 , " pokemons")
# print("El entrenador ", entrenador2 , "tiene ", pkmn2 , " pokemons")
# print(f"El entrenador {entrenador2} tiene  {pkmn2} pokemons")   // la manera mas facil de trabajar con strings y numeros adentro del string, tampoco es necesario colocar ""
# print("El entrenador "+ entrenador2 +" tiene 7 pokemons")
# name="EVA"
# # -3-2-1
# # 012345
# print(name [1])
# --------------------------------------------------------------------------------------------------------------------------
# name="Poggar Jose"
# print(name.strip())
# print(name.lower().strip())    // aca coloca todo en lower case
# print(name.upper())    // aca todo mayuscula
# print(name.replace("Poggar", "Smegma"))  // aca puedes cambiar un string por otro
# print(name.split())    // aca los coloca en [] entrecorchetes*
# --------------------------------------------------(tareas)------------------------------------------------------

'''pedir clave al usuario y verificar que sea shaza,'''
'''indiferente de mayusculas o minusculas'''

# code=input("Ingrese clave de usuario:  ")
# claveus="SHAZAM"
# if code.upper()==claveus:
#     print("Clave correcta puede ingresar")
# else:
#     print("Clave incorrecta")

'''Crear un nombre de usuario y verificar que su largo este entre 4 y 10 caracteres'''
# coring1=input("ingrese un nombre de usuario , tiene un minimo de 4 a 10 caracteres: ")
# if len(coring1)>=4 and len(coring1)<=10: // esta puede ser una manera de ser (no lo he comprobado)
#     print("Caracteres correctos")
# else:
#     print("Caracteres incorrectos")
# --------------------------------------- (2 maneras de leerlo)--------------------------
# if len(coring1)<4:
#     print("muy pocos caracteres")
# elif len(coring1)>10:
#     print("muchos caracteres")
# else:
#     print("Caracteres correctos")

'''Crear un pin y que tenga exactamente 4 digitos'''

# pwd=input("ingrese contraseña(ingrese solo 4 digitos): ")

# if len(pwd)==4:
#     print("El pin esta correcto")
#     pin=int(pwd)
# else:
#     print("El pin esta incorrecto")
# -------------------------------------------------------- (2 maneras para leer los digitos)----------------
# pwd=input("ingrese contraseña(ingrese solo 4 digitos): ")

# if len(str(pwd))==4:
#     print("El pin esta correcto") 
# else:
#     print("El pin esta incorrecto")
