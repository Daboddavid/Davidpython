#Funciones guia examen
 
 
 
autos = {
    'A001' : ['Toyota','Corolla',2010,5],
    'A002' : ['Ford', 'Ranger',2019,4],
    'A003' : ['Chevrolet', 'Spark',2022,4],
    'A004' : ['Suzuki', 'Aerio',2005,4],
    'A005' : ['Toyota','Yaris',2015,5],
    'A006' : ['Chevrolet', 'Impala',1950,1],
}
operaciones = {
    'A001' : ['01-01-2024','12-12-2025'],
    'A002' : ['07-08-2024','Pendiente'],
    'A003' : ['09-01-2025','Pendiente'],
    'A004' : ['24-03-2025','Pendiente'],
    'A005' : ['24-03-2024','24-07-2024'],
    'A006' : ['24-03-2024','24-09-2024'],
}



# autos.setdefault(id,[]).append(f"")

def autos_vendidos_por_marca(marca):
    total=0
    for key,values in autos.items():
        if operaciones[key][1]!="Pendiente":
            if values[0].lower()==marca.lower():
                total+=1
    print(f"hay {total} vendidos de la marca {marca}")

def busqueda_anio(anio_min,anio_max):
    listaanio=[]
    for key,values in autos.items():
        if operaciones[key][1]!="Pendiente":
            if anio_min<values[2]<anio_max:
                listaanio.append(f"{values[0]},{values[1]}--{key}")
    print(listaanio)


# while True:
#     try:
#         min=int(input("ingrese la fecha minima: "))
#         max=int(input("ingrese la fecha maxima: "))
#         busqueda_anio(min,max)
#         next=input("desea buscar otro vehiculo (s/n): ")
#         if next=="n":
#             break
#     except ValueError as e:
#         print(e)


# def actualizado(id_auto,nuevafecha):
#     if id_auto in operaciones:
#         operaciones[id_auto]=nuevafecha
#         return True
#     else:
#         return False
    
# while True:
#     try:
#         id_auto=input("ingrese la id del auto: ")
#         d=int(input("ingrese el numero del dia: "))
#         m=int(input("ingrese el numero del mes: "))
#         y=int(input("ingrese el numero del año: "))
#         nuevafecha=(f"{d}-{m}-{y}")
#         if actualizado(id_auto,nuevafecha):
#             print(operaciones)
#         else:
#             print("error en el actualizado")
#     except ValueError as e:
#         print(e)
#         next=input("desea actualizar otro vehiculo(s/n): ")
#         if next=="n":
#             break

def id(id_nueva):
    if id_nueva not in autos:
        return True
    else:
        return False

def añonue(añonuevo):
    if añonuevo>1900:
        return True
    else:
        return False

def rankin(rank):
    if rank>1 and rank<=5:
        return True
    else:
        return False

while True:
    id_nueva=input("ingrese la id nueva: ")
    if id(id_nueva):
        print("ingresando datos")
    else:
        break
    marca=input("ingrese marca:")
    modelo=input("ingrese modelo:")
    try:
        añonuevo=int(input("ingrese el año: "))
        if añonue(añonuevo):
            print("ingresando año nuevo")
        else:
            break
    except ValueError:
        print("ingrese solo numeros")
    try:
        rank=int(input("ingrese su rank: "))
        if rankin(rank):
            print("ingresando su ranking")
        else:
            break
    except ValueError:
        print("ingrese solo numeros")
    autos.setdefault(id_nueva,[]).append(f"{marca},{modelo},{añonuevo},{rank}]")
    print(autos)
    break

    





def eliminado(id_auto):
    if id_auto in autos:
        autos.pop(id_auto)
        operaciones.pop(id_auto)
        return True
    else:
        return False

