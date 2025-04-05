import psycopg2
# crear objeto conexion
conexion = psycopg2.connect(
    user='postgres',
    password='admin',
    host='127.0.0.1',
    port='5432',
    database='test_db'
     )
##crear un cursor para ejecutar sentencias SQL
try:
    with conexion:
        with conexion.cursor() as cursor:
            # sentencia = 'SELECT * FROM persona WHERE id_persona IN (1,2,3)'
            # cursor.execute(sentencia)
            # registros = cursor.fetchall()

            # sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            # PK = ((1,2,3,4),)
            # cursor.execute(sentencia,PK)
            # registros = cursor.fetchall()

            sentencia = 'SELECT * FROM persona WHERE id_persona IN %s'
            entrada = input('Ingrese lis id\'S a buscar (seperados por comas): ')
            PK = (tuple(entrada.split(',')),)##se crea una tupla de tuplas con los valores numericos eliminando las comas
            cursor.execute(sentencia,PK)
            registros = cursor.fetchall()


            print(f'Cantidad de personas : {len(registros)}')
            for persona in registros:
                print(persona)
                
except Exception as e:
    print(f'Ocurrio un error : {e}')
finally:
    conexion.close()