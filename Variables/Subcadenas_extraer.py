
#una sub cadena es una parte de una cadena principal
texto1= "El segundo es el primero de los perdedores.Senna"
subcadena= texto1[0:11]# la ultima poscion no se obtiene osea en este caso la 11
print(subcadena)
subcadena2= texto1[3:11]
print(subcadena2)

###buscar sub cadena

buscar_primero= texto1.find('primero')
print(f"indice de la subcadena 'primero': {buscar_primero}")
#--------------OJO--------------------
#si no encuentra el valor buscado devuelve -1 y si se repite el valor devuelve el indice del primero

#BUSCAR Y EXTRAER
buscar=texto1.find('Senna')
extraer= buscar+6
print(texto1[buscar:extraer])

####reemplazar subcadena
texto2="Hola mundo"
nuevo_texto= texto2.replace('mundo','a todos')##crea una nuevo objeto no reemplaza
print(f'Nueva cadena: {nuevo_texto}')
#nuevo_texto2= nuevo_texto.replace('Hola','Adios')
#print(f"Reemplazando 'hola' : {nuevo_texto2}")
print(nuevo_texto.replace('Hola','Adios'))

#Seperar cadenas

datos="John,32,Colombia"
#split() por default separa epacios en blanco
lista= datos.split(',')
print(f'Se separaron los elementos de la cadena en una lista{lista}')
print(f"poscion 3 de la lista: {lista[2]} \n")

#########################multiplicacion de cadenas###############
print("MULTIPLICACION DE CADENAS")
texto3= 'Hola'
veces = 4
resultado = texto3*veces
print(resultado+"\n")



