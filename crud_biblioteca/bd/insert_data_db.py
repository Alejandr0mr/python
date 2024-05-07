import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)

cursor = db_connection.cursor()


insert_data_query = """
INSERT INTO usuarios (name, last_name, age, email) VALUES (%s, %s, %s, %s)
"""
data_to_insert = ("Mariana", "Bedoya", 18, "mariana@gmail.com")

cursor.execute(insert_data_query, data_to_insert)
db_connection.commit()

cursor.close()
db_connection.close()
