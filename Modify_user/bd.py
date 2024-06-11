import mysql.connector

# Realizamos la conexión a la base de datos.
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital_bd"
)


cursor = db_connection.cursor()


def read_enfermeros_bd():
    read_data_query = """
        SELECT COUNT(*) AS cantidad_enfermeros
        FROM trabajadores
        WHERE cargo = 'enfermero';
    """
    cursor.execute(read_data_query)
    data = cursor.fetchone()
    print("Cantidad de enfermeros en el hospital:", data[0])
    
    cursor.close()
    db_connection.close()