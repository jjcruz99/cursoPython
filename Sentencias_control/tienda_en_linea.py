print('           ****Sistemas de Descuentos****\n')
valor_de_compra = float(input('Digite el valor de su compra: '))
miembro= input('Digite "Si o No" si es miembro de la tienda: ')
miembro = miembro.strip().lower() # se eliminan los espacios digitados y todo el texto se pone ern minuscula

if valor_de_compra > 1000 and miembro == 'si':
    valor_de_compra = valor_de_compra-(valor_de_compra*0.1)
    print(f'Tiene un descuento del 10%\nTotal a pagar=${valor_de_compra} ')
elif miembro == 'si':
    valor_de_compra = valor_de_compra-(valor_de_compra*0.05)
    print(f'Tiene un descuento del 5%\nTotal a pagar=${valor_de_compra} ')
elif valor_de_compra > 1000 :
    valor_de_compra = valor_de_compra-(valor_de_compra*0.03)
    print(f'Tiene un descuento del 3%\nTotal a pagar=${valor_de_compra} ')
else:
    print(f'0% de descuento\nTotal a pagar:${valor_de_compra}')
print('Gracias vuelva pronto')

