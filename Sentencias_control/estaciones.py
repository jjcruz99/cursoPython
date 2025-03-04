print('****Programa estaciones del año')
mes=int(input('Digite el numero correspondiente al mes del año: '))

if mes==1 or mes==2 or mes==12:
    print(f'Para el mes {mes} la estacion del año es invierno')
elif mes==3 or mes==4 or mes==5:
    print(f'Para el mes {mes} la estacion del año es primavera')
elif mes==6 or mes==7 or mes==8:
    print(f'Para el mes {mes} la estacion del año es verano')
elif mes==9 or mes==10 or mes==11:
    print(f'Para el mes {mes} la estacion del año es otoño')
else:
    print(f'El mes {mes} es un valor errado')