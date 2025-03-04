print('********Generacion Ticket de venta *******')

precio_leche = float(input('Ingrese el valor de la leche: '))
precio_pan =  float(input('Ingrese el valor del pan: '))
descuento = int(input('Por favor digite el descuento %: '))

subtotal= precio_pan + precio_leche
descuento = subtotal*(descuento/100)
iva = (subtotal-descuento)*0.19
total = subtotal+ iva

print(f'Subtotal= {subtotal}\nDescuento= {descuento}\niva= {iva}\nTotal= {total}\n')


