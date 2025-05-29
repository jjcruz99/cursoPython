import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)
#objeto tipo cursor para ejecutar sentencias SQL
mi_cursor = personas_db.cursor()
sentencia_sql = ('DELETE FROM personas WHERE id_persona = %s')
id= (7,)#es una tupla
mi_cursor.execute(sentencia_sql,id)
personas_db.commit()
print('Se ha eliminado un registro')
personas_db.close()

