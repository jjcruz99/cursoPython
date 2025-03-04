print('  ****Acceso a la Casa de los espejos***')
edad = int(input('Digite su edad: '))
miedo_oscuridad= input('Digite "Si/No" si le tiene miedo a la oscuridad: ')
miedo_oscuridad = miedo_oscuridad.strip().lower() == 'si' ##elimina espacio la vuelve minuscula y la convierte en booleano
print(miedo_oscuridad and edad < 10)
print(miedo_oscuridad and edad > 10)
if not  miedo_oscuridad :
    if not edad < 10 :
      print('Puede ingresar a la casa de los espejos')
else:
    print('No tiene acceso a la casa de los espejos')


