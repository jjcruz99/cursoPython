from colorsys import yiq_to_rgb

print(f'--------------Asiganacion---------\n')
a=12
print(f'a={a}')

print(f'--------------Asiganacion Multiple---------\n')
v1,v2,v3,v4=12,1369,'Hola',True
print(f'v1={v1},v2={v2},v3={v3},v4={v4}')

print(f'--------------Asiganacion encadenada---------\n')
a=b=c=0.000025898
print(f'a={a},b={b},c={c}')

#intercambio de valores de una variable
x,y=5,6
print(f'Valores inicilaes x{x}, y{y}')
x,y=y,x
print(f'Valores intercambiados x{x}, y{y}')

print('------------Recibir multiples valores------------- ')
nombre,apellido=input('Ingrese su nombre y apellido separado por una coma: ').split(',')##split divide la cadena cada vez que encuentra una coma
print(f'Nombre:{nombre.strip()}  Apellido:{apellido.strip()}')
