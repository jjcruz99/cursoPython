#declarra variables

a,b = 'Hola','Adios'
print(a,b)

#Swap (intercambio)
a,b = b,a
print(a,b)

print('Regresar multiples valores en una funcion')
def minmax(elementos):
    return min(elementos),max(elementos)

min,max = minmax([25,58,69,63])
print(min,max)

#sum retorna la sumatoria
print(sum((1,2,3,4,5)))

def sumatoria(*args):
    return sum(args)

sumatoria_tupla = sumatoria(1,6,8)
print(sumatoria_tupla)