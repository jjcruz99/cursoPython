
import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)
#objeto tipo cursor para ejecutar sentencias SQL
mi_cursor = personas_db.cursor()
mi_cursor.execute('SELECT id_persona,nombre,edad FROM personas')
registros = mi_cursor.fetchall()
for persona in registros:
    print(persona)

personas_db.close()
