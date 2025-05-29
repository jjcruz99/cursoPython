
import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)
#objeto tipo cursor para ejecutar sentencias SQL
mi_cursor = personas_db.cursor()
sentencia_sql= ('UPDATE personas SET nombre=%s, apellido=%s, edad=%s WHERE id_persona=%s')
valores = ('Victoria','Ruiz',18,5)
mi_cursor.execute(sentencia_sql,valores)
personas_db.commit()
print('Se actualizo un registro')
personas_db.close()

