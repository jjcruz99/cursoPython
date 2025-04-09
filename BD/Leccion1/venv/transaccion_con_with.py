import psycopg2 as DB

# crear objeto conexion
conexion = DB.connect(
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
            sentencia = 'INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'
            valores = ('John','Cruz','john@gmail.com')
            cursor.execute(sentencia,valores)

            sentencia = 'UPDATE persona SET nombre = %s,apellido = %s WHERE id_persona = 8'
            valores = ('Camilo','Vargas')
            cursor.execute(sentencia,valores)

            print('Trasaccion completa')
except Exception as e:
    print(f'Ocurrio un error {e}')
finally:
    conexion.close()