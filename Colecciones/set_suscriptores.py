print("                Set de suscriptores")

suscriptores = set()
opcion = ""
suscriptor = ""

while True:
    print("""
                  Menu
        -Salir
        -Agregar
        -Eliminar
        -Mostrar
        -Cantidad
    """)
    opcion = input("Digite una opcion : ")
    if(opcion.lower() == "salir"):
        print("Fin del programa")
        break
    elif(opcion.lower() == "agregar"):
        suscriptor = input("Digite el nombre del suscriptor agregar : ")

        if(suscriptor in suscriptores): #verifica si existe el suscriptor
            print("Ya existe el suscriptor")
        else:
            suscriptores.add(suscriptor)
            print("Se agrego con exito")
    elif (opcion.upper() == "ELIMINAR"):
        suscriptor = input("Digite el nombre del suscriptor a eliminar : ")
        if(suscriptor in suscriptores): #verifica si existe el suscriptor
            suscriptores.remove(suscriptor)
            print(f'Se elimino el suscriptor : {suscriptor}')
        else:
            print("No encontrado")
    elif (opcion.lower() == "mostrar"):
        print(f'lista de suscriptores : {suscriptores}')
    elif (opcion.lower().strip() == "cantidad"):
        print("La cantidad de suscriptores  es : ", len(suscriptores))
    else:
        print("Digite una opcion valida")