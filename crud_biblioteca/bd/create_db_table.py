import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)


# Cursor para pasar información de un lado a otro.
cursor = db_connection.cursor()


#Crea la base de datos
create_table_query ="""
CREATE TABLE usuarios
(
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(10),
    last_name VARCHAR(10),
    age INT,
    email VARCHAR(15)
)
"""
cursor.execute(create_table_query)
#un comentario que si se ejecuto
db_connection.commit()

#se cierra
cursor.close()
db_connection.close()