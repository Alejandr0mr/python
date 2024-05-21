import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="agencia_de_viaje"
)



# Cursor para pasar información de un lado a otro.
cursor = db_connection.cursor()
#Crea la tabla libros en la base de datos.

def crear_tabla_usuarios():

    cursor = db_connection.cursor()
    
    create_table_query ="""
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
    #un comentario que si se ejecuto
    db_connection.commit()

    #se cierra
    print("tabla  creada")


def crear_tabla_hoteles():
    cursor = db_connection.cursor()
    
    create_table_query ="""
    CREATE TABLE hoteles
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        nombre VARCHAR(20),
        direccion VARCHAR(30),
        ciudad INT,
       
    )
    """
    cursor.execute(create_table_query)
    #un comentario que si se ejecuto
    db_connection.commit()
    print("tabla  creada")


def crear_tabla_reservas():
    cursor = db_connection.cursor()
    create_table_query ="""
    CREATE TABLE reservas
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        aerolinea VARCHAR(25),
        fecha VARCHAR(20),
        destino VARCHAR(20),
    )
    """
    cursor.execute(create_table_query)
    #un comentario que si se ejecuto
    db_connection.commit()

    #se cierra
    print("tabla  creada")

# Llamar a las funciones para crear las tablas
# crear_tabla_hoteles()
# crear_tabla_reservas()
crear_tabla_usuarios()



# Cerrar el cursor y la conexión a la base de datos
cursor.close()
db_connection.close()

