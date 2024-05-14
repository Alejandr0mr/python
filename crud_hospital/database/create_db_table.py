import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital"
)


# Cursor para pasar información de un lado a otro.
cursor = db_connection.cursor()


#Crea la tabla libros en la base de datos.

def crear_tabla_pacientes():
    
    create_table_query ="""
    CREATE TABLE pacientes
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50),
        apellido VARCHAR(25),
        identificacion INT,
        fecha_nacimiento VARCHAR(250),
        genero VARCHAR(10),
        motivo VARCHAR(250),
        diagnostico VARCHAR(250)
    )
    """
    cursor.execute(create_table_query)
    #un comentario que si se ejecuto
    db_connection.commit()

    #se cierra
    cursor.close()
    db_connection.close()
    print("tabla pacientes creada")


def crear_tabla_trabajadores():
    
    create_table_query ="""
    CREATE TABLE trabajadores
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(20),
        apellido VARCHAR(30),
        identificacion INT,
        cargo VARCHAR(250),
        id_departamento INT,
        FOREIGN KEY (id_departamento) REFERENCES departamentos(id)
    )
    """
    cursor.execute(create_table_query)
    #un comentario que si se ejecuto
    db_connection.commit()
    print("tabla trabajadores creada")


def crear_tabla_departamentos():
    
    create_table_query ="""
    CREATE TABLE departamentos
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(20)
    )
    """
    cursor.execute(create_table_query)
    #un comentario que si se ejecuto
    db_connection.commit()

    #se cierra
    print("tabla departamentos creada")

# Llamar a las funciones para crear las tablas
crear_tabla_pacientes()
crear_tabla_departamentos()
crear_tabla_trabajadores()


# Cerrar el cursor y la conexión a la base de datos
cursor.close()
db_connection.close()

