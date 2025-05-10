
def fucion_externa():
    var_local_externa = 'Local externa'

    def funcion_anidada():
        var_local_anidad = 'local anidada'
        nonlocal  var_local_externa
        var_local_externa += ' +++'


    funcion_anidada()
    print(var_local_externa)

fucion_externa()

##ejemplo
contador = 0

def mostrar_contador():
    print(contador)

def modificar_contador(con):
    global contador
    contador = con

modificar_contador(10)
mostrar_contador()