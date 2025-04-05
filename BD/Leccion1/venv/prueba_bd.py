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
            sentencia = 'SELECT * FROM persona WHERE id_persona= %s'
            id_persona = 1
            cursor.execute(sentencia,(id_persona,)) # se envia como una tupla
            registros = cursor.fetchone()
            print(f'Cantidad de personas : {len(registros)}')
            print(registros)
except Exception as e:
    print(f'Ocurrio un error : {e}')
finally:
    conexion.close()

