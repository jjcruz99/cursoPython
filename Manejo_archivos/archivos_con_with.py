from Manejo_archivos.manejo_archivos import Manejo_Archivos

#with open('prueba.txt', 'r',encoding='utf8') as archivo :
with Manejo_Archivos('prueba.txt') as archivo:
    print(archivo.read())

