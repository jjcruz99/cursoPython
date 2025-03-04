print('*****Sistema de Envios******')
nacional = 1000
internacional = 2000
costo_envio= None
destino = input('Digite el destino del envio (Nacional/Internacional): ')
destino = destino.strip().upper()
peso = float(input('Digite la masa del paquete en Kg: '))

if destino == 'NACIONAL':
  costo_envio = peso * nacional
elif destino == 'INTERNACIONAL':
    costo_envio = peso * internacional
else:
    print('Verifique los datos digitados')

#verificamos si se pudo realizar el calculo
if costo_envio is not None:
  print(f'Destino: {destino}\nMasa: {peso}Kg\nCosto:${costo_envio}')