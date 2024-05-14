import mysql.connector

# Realizamos la conexión a la base de datos.
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital"
)
cursor = db_connection.cursor()

# Función para crear un nuevo trabajador
def insert_trabajador_bd(nombre, apellido, identificacion, cargo, id_departamento):
    insert_data_query = """
        INSERT INTO trabajadores (nombre, apellido, identificacion, cargo, id_departamento)
        VALUES (%s, %s, %s, %s, %s)
    """
    data_to_insert = (nombre, apellido, identificacion, cargo, id_departamento)

    cursor.execute(insert_data_query, data_to_insert)
    db_connection.commit()
    
    close_connection()

# Función para leer todos los trabajadores
def read_trabajador_bd():
    
    db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital"
    )
    cursor = db_connection.cursor()
    read_data_query = """
    SELECT * FROM trabajadores
    """
    cursor.execute(read_data_query)
    data = cursor.fetchall()
    return data


# Función para actualizar un trabajador existente
def update_trabajador_bd(trabajador_id, nuevo_nombre, nuevo_apellido, nueva_identificacion, nuevo_cargo, nuevo_id_departamento):

    update_data_query = """
        UPDATE trabajadores
        SET nombre = %s, apellido = %s, identificacion = %s, cargo = %s, id_departamento = %s
        WHERE id = %s
    """
    data_to_update = (nuevo_nombre, nuevo_apellido, nueva_identificacion, nuevo_cargo, nuevo_id_departamento, trabajador_id)


    cursor.execute(update_data_query, data_to_update)
    db_connection.commit()
    
    close_connection()

# Función para eliminar un trabajador existente
def delete_trabajador_bd(trabajador_id):

    delete_data_query = """
        DELETE FROM trabajadores
        WHERE id = %s
    """
    data_to_delete = (trabajador_id,)

    cursor.execute(delete_data_query, data_to_delete)
    db_connection.commit()
    
    close_connection()

# Cerrar la conexión a la base de datos
def close_connection():
    cursor.close()
    db_connection.close()
