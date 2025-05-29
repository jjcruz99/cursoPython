import mysql.connector

personas_db = mysql.connector.connect(
    host='localhost',
    user='root',
    password='admin',
    database='personas_db'
)
#objeto tipo cursor para ejecutar sentencias SQL
mi_cursor = personas_db.cursor()
sentencia = ('INSERT INTO personas (nombre,apellido,edad)'
             'VALUES (%s, %s, %s);')
valores = ('Victor','Ramos',46)
mi_cursor.execute(sentencia,valores)
personas_db.commit()#guardar los cambios en la DB
mi_cursor.close()
personas_db.close()