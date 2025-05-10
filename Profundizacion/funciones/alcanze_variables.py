#scope

var_global = 'Global'

def imprimir():
    global var_global
    print(f'Desde imprimir: {var_global}')

    var_local = 'local'
    print(f'Variable {var_local}')
    def mostrar():
        print(f'Desde mostra() funcion anidada Variable {var_local}')

    mostrar()

    var_global += ' Global Global'
    print(var_global)

imprimir()