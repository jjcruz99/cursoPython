
contador_global = 0

def incrementar ():
    contador_local = 0
    global contador_global #se utiliza la plabra reservada global para usar la variable global dentro de la funcion

    contador_local += 1
    contador_global += contador_local

    print(f'Contador local {contador_local}')
    print(f'Contador global {contador_global}')

incrementar()
incrementar()
incrementar()