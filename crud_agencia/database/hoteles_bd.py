import mysql.connector

# Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agencia_de_viaje"
    )

# Función para insertar un hotel en la base de datos
def insert_hotel_bd(nombre, direccion, ciudad):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    insert_data_query = """
        INSERT INTO hoteles (nombre, direccion, ciudad)
        VALUES (%s, %s, %s)
    """
    data_to_insert = (nombre, direccion, ciudad)

    cursor.execute(insert_data_query, data_to_insert)
    db_connection.commit()

    cursor.close()
    db_connection.close()

# Función para leer todos los hoteles
def read_hoteles_bd():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    read_data_query = """
    SELECT * FROM hoteles
    """
    cursor.execute(read_data_query)
    data = cursor.fetchall()

    cursor.close()
    db_connection.close()

    return data

# Función para actualizar un hotel existente
def update_hotel_bd(hotel_id, nuevo_nombre, nueva_direccion, nueva_ciudad):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    update_data_query = """
        UPDATE hoteles
        SET nombre = %s, direccion = %s, ciudad = %s
        WHERE id = %s
    """
    data_to_update = (nuevo_nombre, nueva_direccion, nueva_ciudad, hotel_id)

    cursor.execute(update_data_query, data_to_update)
    db_connection.commit()

    cursor.close()
    db_connection.close()

# Función para eliminar un hotel existente
def delete_hotel_bd(hotel_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    delete_data_query = """
        DELETE FROM hoteles
        WHERE id = %s
    """
    data_to_delete = (hotel_id,)

    cursor.execute(delete_data_query, data_to_delete)
    db_connection.commit()

    cursor.close()
    db_connection.close()
