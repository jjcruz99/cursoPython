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
    conexion.autocommit = False
    cursor = conexion.cursor()
    sentencia = 'INSERT INTO persona (nombre,apellido,email) VALUES (%s,%s,%s)'
    valores = ('Carlos','Lara','carlos@gmail.com')
    cursor.execute(sentencia,valores)

    sentencia = 'UPDATE persona SET nombre = %s,apellido = %s WHERE id_persona = 1'
    valores = ('Karlita','Arevalo')
    cursor.execute(sentencia,valores)

    conexion.commit() #se guardan los cambios
    print('Trasaccion completa, se hizo commit')
except Exception as e:
    conexion.rollback()
    print(f'Ocurrio un error, se realizo rollback: {e}')
finally:
    conexion.close()