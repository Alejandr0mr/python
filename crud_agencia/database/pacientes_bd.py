import mysql.connector

# Realizamos la conexión a la base de datos.
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital"
)
cursor = db_connection.cursor()

# Función para crear un 

def insert_paciente_bd(nombre, apellido, identificacion, fecha_nacimiento, genero, motivo_consulta, diagnostico):
    insert_data_query = """
        INSERT INTO pacientes (nombre, apellido, identificacion, fecha_nacimiento, genero, motivo, diagnostico)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
    """
    data_to_insert = (nombre, apellido, identificacion, fecha_nacimiento, genero, motivo_consulta, diagnostico)

    cursor.execute(insert_data_query, data_to_insert)
    db_connection.commit()
    
    close_connection()

# Función para leer todos los libros
def read_pacientes_bd():

    db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital"
    )
    cursor = db_connection.cursor()
    
    read_data_query = """
    SELECT * FROM pacientes
    """
    cursor.execute(read_data_query)
    data = cursor.fetchall()

    return data


# Función para actualizar un libro existente
def update_paciente_bd(paciente_id, nuevo_nombre, nuevo_apellido, nueva_identificacion, nueva_fecha_nacimiento, nuevo_genero, nuevo_motivo_consulta, nuevo_diagnostico):

    update_data_query = """
        UPDATE pacientes
        SET nombre = %s, apellido = %s, identificacion = %s, fecha_nacimiento = %s, genero = %s, motivo = %s, diagnostico = %s
        WHERE id = %s
    """
    data_to_update = (nuevo_nombre, nuevo_apellido, nueva_identificacion, nueva_fecha_nacimiento, nuevo_genero, nuevo_motivo_consulta, nuevo_diagnostico, paciente_id)


    cursor.execute(update_data_query, data_to_update)
    db_connection.commit()
    
    close_connection()

# Función para eliminar un libro existente
def delete_paciente_bd(paciente_id):

    delete_data_query = """
        DELETE FROM pacientes
        WHERE id = %s
    """
    data_to_delete = (paciente_id,)

    cursor.execute(delete_data_query, data_to_delete)
    db_connection.commit()
    
    close_connection()
    

# Cerrar la conexión a la base de datos
def close_connection():
    cursor.close()
    db_connection.close()