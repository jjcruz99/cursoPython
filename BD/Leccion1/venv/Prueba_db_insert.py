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
                sentencia = 'INSERT INTO persona(nombre,apellido,email) VALUES(%s,%s,%s)'
                # valores = ('Carlos','Lara','Carlos@email.com')
                # cursor.execute(sentencia,valores)

                valores = (
                    ('Carlos','Lara','Carlos@email.com'),
                    ('Mariela', 'Mogo', 'mari@email.com'),
                    ('Cristian', 'Cruz', 'cris@email.com')
                )
                cursor.executemany(sentencia,valores)
                ##conexion.commit() ##cuando se usa with no es necesario
                #observar los registros insertados
                resgistros_insertados = cursor.rowcount
                print(f'Registros insertados : {resgistros_insertados}')
except Exception as e:
    print(f'Ocurrio un error : {e}')
finally:
    conexion.close()