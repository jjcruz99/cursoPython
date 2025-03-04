print('-------Sistema de descuentos VIP')

N0_producros_descuento=10
compras = int(input('Digite la cantidad de productos de su compra: '))
membresia = input('Tienen tarjeta puntos (si/no) : ')

aplica_descuento = (compras == N0_producros_descuento and membresia.strip().lower() =='si')

print(f'Tiene descuento : {aplica_descuento}')