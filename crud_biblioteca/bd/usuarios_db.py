import mysql.connector

# Realizamos la conexión a la base de datos.
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)
cursor = db_connection.cursor()

# Función para crear un nuevo usuario
def insert_usuarios_bd(name, email, password):
    insert_data_query = """
    INSERT INTO usuarios (name, email, password) VALUES (%s, %s, %s)
    """
    data_to_insert = (name, email, password )

    cursor.execute(insert_data_query, data_to_insert)
    db_connection.commit()
    
    close_connection()

# Función para consultar los usuarios.
def read_usuarios_bd():
    read_data_query = """
    SELECT * FROM usuarios
    """
    cursor.execute(read_data_query)
    data = cursor.fetchall()

    return data

    close_connection()


# Cerrar la conexión a la base de datos
def close_connection():
    cursor.close()
    db_connection.close()