# alumno={
#     "nombre":"Shinji Ikari",
#     "edad": 14,
#     "carrera":"Piloto"
# }
# for i,a in alumno.items():
#     print(f"{i} : {a}")


# print("--- cambios ---")
# alumno["carrera"]="escritor"                 #cambiando el value de un key
# alumno["email"]="shinji@nerv.com"            #agregando una key y un value nuevo
# del alumno["edad"]                           #eliminado de datos

# for i,a in alumno.items():
#     print(f"{i}:{a} ")


productos={
    1:{"nombre":"Control inalambrico",
       "Categoria": "Electronica",
       "Precio": 45000},
    1:{"nombre":"Pilas recargables",
       "Categoria": "insumos",
       "Precio": 5000},
    1:{"nombre":"Pasta termica",
       "Categoria": "Computacion",
       "Precio": 7000},
}

print(productos[1]["nombre"])


# productos=[
#     {"nombre":"Control inalambrico",
#        "Categoria": "Electronica",
#        "Precio": 45000},
#     {"nombre":"Pilas recargables",
#        "Categoria": "insumos",
#        "Precio": 5000},
#     {"nombre":"Pasta termica",
#        "Categoria": "Computacion",
#        "Precio": 7000},
# ]
#                                                              listas de diccionarios


