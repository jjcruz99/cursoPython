##Programa generador de email
print('Programa generador de email')
nombre= 'John Jairo Cruz Mogollon'
Empresa= 'Global mentoring'
Dominio= '.com.mx'
nombre_normalizado= nombre.strip() ##Quitar los espacios al inicio y final
nombre_normalizado=nombre.lower()
nombre_normalizado= nombre_normalizado.replace(' ','.')
print(f'Nombre de usuario: {nombre}')
print(f'Nombre normalizado: {nombre_normalizado} \n')

empresa_normalizado= Empresa.lower()
empresa_normalizado = empresa_normalizado.replace(' ','.')
print(f'nombre empresa: {Empresa}\n\rExtencion de dominio: {Dominio}')
dominio_normalizado= ''.join([empresa_normalizado,Dominio])
print(f'Dominio email normalizado: {dominio_normalizado}\n')

email_generado = ''.join([nombre_normalizado,'@',dominio_normalizado])
print(f'Email generado: {email_generado}')

