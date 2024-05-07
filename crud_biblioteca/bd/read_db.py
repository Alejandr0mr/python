import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)

cursor = db_connection.cursor()

read_data_query = """
SELECT * FROM usuarios
"""
cursor.execute(read_data_query)
data = cursor.fetchall()
# Recuperar los datos y mostrarlos

# print(type(data))

for row in data:
    print(f"ID: {row[0]}")
    print(f"Nombre: {row[1]}")
    print(f"Apellido: {row[2]}")



cursor.close()
db_connection.close()
