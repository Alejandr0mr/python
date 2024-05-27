import mysql.connector

# Conexión a la base de datos
def get_db_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="agencia_de_viaje"
    )

# Función para insertar una reserva en la base de datos
def insert_reserva_bd(aerolinea, fecha, destino):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    insert_data_query = """
        INSERT INTO reservas (aerolinea, fecha, destino)
        VALUES (%s, %s, %s)
    """
    data_to_insert = (aerolinea, fecha, destino)

    cursor.execute(insert_data_query, data_to_insert)
    db_connection.commit()

    cursor.close()
    db_connection.close()

# Función para leer todas las reservas
def read_reservas_bd():
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    read_data_query = """
    SELECT * FROM reservas
    """
    cursor.execute(read_data_query)
    data = cursor.fetchall()

    cursor.close()
    db_connection.close()

    return data

# Función para actualizar una reserva existente
def update_reserva_bd(reserva_id, nueva_aerolinea, nueva_fecha, nuevo_destino):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    update_data_query = """
        UPDATE reservas
        SET aerolinea = %s, fecha = %s, destino = %s
        WHERE id = %s
    """
    data_to_update = (nueva_aerolinea, nueva_fecha, nuevo_destino, reserva_id)

    cursor.execute(update_data_query, data_to_update)
    db_connection.commit()

    cursor.close()
    db_connection.close()

# Función para eliminar una reserva existente
def delete_reserva_bd(reserva_id):
    db_connection = get_db_connection()
    cursor = db_connection.cursor()

    delete_data_query = """
        DELETE FROM reservas
        WHERE id = %s
    """
    data_to_delete = (reserva_id,)

    cursor.execute(delete_data_query, data_to_delete)
    db_connection.commit()

    cursor.close()
    db_connection.close()
