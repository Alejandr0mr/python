import mysql.connector

# Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agencia_de_viaje"
    )

# Función para insertar un usuario en la base de datos
def insert_usuario_bd(nombre, apellido, identificacion, id_hotel, id_reserva):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    insert_data_query = """
        INSERT INTO usuarios (nombre, apellido, identificacion, id_hotel, id_reserva)
        VALUES (%s, %s, %s, %s, %s)
    """
    data_to_insert = (nombre, apellido, identificacion, id_hotel, id_reserva)

    cursor.execute(insert_data_query, data_to_insert)
    db_connection.commit()
    
    cursor.close()
    db_connection.close()

# Función para leer todos los usuarios
def read_usuarios_bd():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()
    
    read_data_query = """
    SELECT * FROM usuarios
    """
    cursor.execute(read_data_query)
    data = cursor.fetchall()

    cursor.close()
    db_connection.close()
    
    return data

# Función para actualizar un usuario existente
def update_usuario_bd(usuario_id, nuevo_nombre, nuevo_apellido, nueva_identificacion, nuevo_id_hotel, nuevo_id_reserva):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    update_data_query = """
        UPDATE usuarios
        SET nombre = %s, apellido = %s, identificacion = %s, id_hotel = %s, id_reserva = %s
        WHERE id = %s
    """
    data_to_update = (nuevo_nombre, nuevo_apellido, nueva_identificacion, nuevo_id_hotel, nuevo_id_reserva, usuario_id)

    cursor.execute(update_data_query, data_to_update)
    db_connection.commit()

    cursor.close()
    db_connection.close()

# Función para eliminar un usuario existente
def delete_usuario_bd(usuario_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    delete_data_query = """
        DELETE FROM usuarios
        WHERE id = %s
    """
    data_to_delete = (usuario_id,)

    cursor.execute(delete_data_query, data_to_delete)
    db_connection.commit()

    cursor.close()
    db_connection.close()
