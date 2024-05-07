import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)

cursor = db_connection.cursor()


delete_data_query = """
DELETE FROM usuarios 
WHERE id = %s 
"""
# Seleccionamos el ID que queremos eliminar
user_id = 1

# El valor del ID debe pasarse como una tupla
data_to_delete = (user_id,)

cursor.execute(delete_data_query, data_to_delete)
db_connection.commit()

cursor.close()
db_connection.close()
