
try:
    archivo = open('prueba.txt','r',encoding='utf8')##c:\\Cursos\\ruta\\ruta\\archivo.txt
   # print(archivo.read()) ## leer todo el archivo

    ##leer algunos caracteres
    # print(archivo.read(5))
    #print(archivo.read(3))

    #leer las lineas
    #print(archivo.readline())

    #iterar lineas del archivo
    # for contador,linea in enumerate(archivo):
    #     print(f'{contador} {linea}')

    #leer lineas
    ##print(archivo.readlines()[0])

    ##abrir un nuevo archivo
    archivo2 = open('copia.txt','a',encoding='utf8') ##a anexar nueva informacion
    archivo2.write(archivo.read())
except Exception as e:
    print(e)
finally:
    archivo.close()
    archivo2.close()
    print('Archivos cerrados')