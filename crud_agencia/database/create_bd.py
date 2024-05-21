import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password=""
)

# Cursor para pasar información de un lado a otro.
cursor = db_connection.cursor()


#Crea la base de datos
create_database_query ="CREATE DATABASE agencia_de_viaje"
cursor.execute(create_database_query)

#un comentario que si se ejecuto
db_connection.commit()

#se cierra
cursor.close()
db_connection.close()


