
try:
    archivo = open('prueba.txt','w',encoding='utf8')
    archivo.write("Agregando información al archivo\n")
    archivo.write("Agregando mas informacion al archivo")
except Exception as e:
    print(e)
finally:
    archivo.close() # despues de cerrar el archivo no se puede realizar ninguna operacion
    print("Archivo cerrado")