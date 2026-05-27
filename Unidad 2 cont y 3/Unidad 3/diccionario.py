alumno={
    "nombre":"Shinji Ikari",
    "edad": 14,
    "carrera":"Piloto"
}
# print(alumno)
print(alumno["carrera"])

# for key,value in alumno.items():
#     print(key,value)
for i,a in alumno.items():
    print(f"{i} : {a}")