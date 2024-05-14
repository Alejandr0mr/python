import mysql.connector

# Realizamos la conexión a la base de datos.
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital"
)
cursor = db_connection.cursor()

# Función para crear un nuevo departamento
def insert_departamento_bd(nombre):
    insert_data_query = """
        INSERT INTO departamentos (nombre)
        VALUES (%s)
    """
    data_to_insert = (nombre,)

    cursor.execute(insert_data_query, data_to_insert)
    db_connection.commit()
    
    close_connection()

# Función para leer todos los departamentos
def read_departamentos_bd():
    read_data_query = """
    SELECT * FROM departamentos
    """
    cursor.execute(read_data_query)
    data = cursor.fetchall()

    return data

# Función para actualizar un departamento existente
def update_departamento_bd(departamento_id, nuevo_nombre):

    update_data_query = """
        UPDATE departamentos
        SET nombre = %s
        WHERE id = %s
    """
    data_to_update = (nuevo_nombre, departamento_id)

    cursor.execute(update_data_query, data_to_update)
    db_connection.commit()
    
    close_connection()

# Función para eliminar un departamento existente
def delete_departamento_bd(departamento_id):

    delete_data_query = """
        DELETE FROM departamentos
        WHERE id = %s
    """
    data_to_delete = (departamento_id,)

    cursor.execute(delete_data_query, data_to_delete)
    db_connection.commit()
    
    close_connection()

# Cerrar la conexión a la base de datos
def close_connection():
    cursor.close()
    db_connection.close()
