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
                sentencia = 'UPDATE persona SET nombre = %s, apellido= %s,email=%s WHERE id_persona = %s'
                valores = (
                    ('Karla','Ruiz','kar@hotmail.com',1),
                    ('Juanca', 'Sanchez', 'anca@hotmail.com', 2),
                )
                cursor.executemany(sentencia,valores)
                #observar los registros actualizados
                resgistros_actualizados = cursor.rowcount
                print(f'Registros actualizados : {resgistros_actualizados}')
except Exception as e:
    print(f'Ocurrio un error : {e}')
finally:
    conexion.close()