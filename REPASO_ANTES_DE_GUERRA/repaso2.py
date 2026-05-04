op=0
total=0


while op!=5:
    print('''bienvenido al menu de compra
            1)Televisor lg // $400.000
            2)Consola portatil switch edicion lite  // $230.000
            3)Audifonos negros bose // $69.000
            4)Teclado mecanico retargamr // $80.0000
            5)Salida''')
    op=int(input())
    match op:
        case 1:
            print("usted selecciono televisor lg")
            total+=400000
        case 2:
            print("usted selecciono consola portatil switch lite")
            total+=230000   
        case 3:
            print("usted selecciono audifonos negro bose")
            total+=69000
        case 4:
            print("usted selecciono teclado mecanico retargamr")
            total+=80000
        case 5:
            print("saliendo del programa")            
        case _:
            print("opcion invalida")
print(f"su total a pagar es ${total}")
            

