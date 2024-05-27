import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agencia_de_viaje"
)

# Cursor para pasar información de un lado a otro.
cursor = db_connection.cursor()

# Crea la tabla usuarios en la base de datos.
def crear_tabla_usuarios():
    create_table_query = """
    CREATE TABLE usuarios
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50),
        apellido VARCHAR(25),
        identificacion INT UNIQUE,
        id_hotel INT,
        FOREIGN KEY (id_hotel) REFERENCES hoteles(id),
        id_reserva INT,
        FOREIGN KEY (id_reserva) REFERENCES reservas(id)
    )
    """
    cursor.execute(create_table_query)
    db_connection.commit()
    print("Tabla usuarios creada")

def crear_tabla_hoteles():
    create_table_query = """
    CREATE TABLE hoteles
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(50),
        direccion VARCHAR(50),
        ciudad VARCHAR(50)
    )
    """
    cursor.execute(create_table_query)
    db_connection.commit()
    print("Tabla hoteles creada")

def crear_tabla_reservas():
    create_table_query = """
    CREATE TABLE reservas
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        aerolinea VARCHAR(50),
        fecha DATE,
        destino VARCHAR(50)
    )
    """
    cursor.execute(create_table_query)
    db_connection.commit()
    print("Tabla reservas creada")

# Llamar a las funciones para crear las tablas
crear_tabla_hoteles()
crear_tabla_reservas()
crear_tabla_usuarios()

# Cerrar el cursor y la conexión a la base de datos
cursor.close()
db_connection.close()
