import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)

cursor = db_connection.cursor()


update_data_query = """
UPDATE usuarios 
SET name = %s, last_name = %s 
WHERE id = %s 
"""
user_id = 1
new_name = "Alejandro"
new_last_name = "Martínez"

# Los valores deben pasarse como una tupla, por lo que se agrupan en una tupla
data_to_update = (new_name, new_last_name, user_id)

cursor.execute(update_data_query, data_to_update)
db_connection.commit()


cursor.close()
db_connection.close()
