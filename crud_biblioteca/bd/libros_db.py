import mysql.connector

# Realizamos la conexión a la base de datos.
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)
cursor = db_connection.cursor()

# Función para crear un nuevo libro
def insert_libros_bd(titulo, autor, descripcion):
    insert_data_query = """
    INSERT INTO libros (title, author, description) VALUES (%s, %s, %s)
    """
    data_to_insert = (titulo, autor, descripcion)

    cursor.execute(insert_data_query, data_to_insert)
    db_connection.commit()
    
    close_connection()

# Función para leer todos los libros
def read_libros_bd():
    read_data_query = """
    SELECT * FROM libros
    """
    cursor.execute(read_data_query)
    data = cursor.fetchall()

    return data

    close_connection()

# Función para actualizar un libro existente
def update_libros_bd(libro_id, nuevo_titulo, nuevo_autor, nueva_descripcion):
    update_data_query = """
    UPDATE libros
    SET title = %s, author = %s, description = %s
    WHERE id = %s
    """
    data_to_update = (nuevo_titulo, nuevo_autor, nueva_descripcion, libro_id)

    cursor.execute(update_data_query, data_to_update)
    db_connection.commit()
    
    close_connection()

# Función para eliminar un libro existente
def delete_libros_bd(libro_id):
    
    delete_data_query = """
    DELETE FROM libros
    WHERE id = %s
    """
    data_to_delete = (libro_id,)

    cursor.execute(delete_data_query, data_to_delete)
    db_connection.commit()
    
    close_connection()
    

# Cerrar la conexión a la base de datos
def close_connection():
    cursor.close()
    db_connection.close()