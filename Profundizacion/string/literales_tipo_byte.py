
#caracteres usando bytes
caracteres_en_bytes = b'Cadena manejando bytes'
print(caracteres_en_bytes)

print(caracteres_en_bytes[0])#en decimal
print(chr(caracteres_en_bytes[0]))

#volverl una cadenba a una lista
lista_caracteres = caracteres_en_bytes.split()
print(lista_caracteres)

print('Convertir de string a Byte'.center(50,'*'))
cadena = "Programación python"
bytes = cadena.encode('UTF-8')
print(f'Bytes : {bytes}')

#convertir butes a str
cadena2 = bytes.decode('UTF-8')
print('string Codificado : ',cadena2)

print('las cadenas son iguales') if cadena2 == cadena else print('No son iguales')



