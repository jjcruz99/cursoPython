

print('\n                     Combinacion listas y tuplas')

#definir lista con tuplas para los productos

productos = [
    ('P001','CAMISETA',20.00),
    ('P002','JEANS',40.00),
    ('P003','CHAQUETA',60.00)
]

#IMPRIMIR LA INFORMACION

precio_total= 0
print('\nInformacion de los productos\n')

for producto in productos:
    #print(producto)
    id,descripcion,precio = producto #unpacking
    print(f'Detalles producto: id= {id}, Descripcion= {descripcion}, Precio= ${precio}')
    precio_total += precio # tambien se puede usar productos[2] para acceder a los precios

print(f'Precio total de los productos= {precio_total}')
