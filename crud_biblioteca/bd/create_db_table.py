import mysql.connector

db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="biblioteca"
)


# Cursor para pasar información de un lado a otro.
cursor = db_connection.cursor()


#Crea la tabla libros en la base de datos.

def crear_tabla_libros():
    
    create_table_query ="""
    CREATE TABLE libros
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        title VARCHAR(50),
        author VARCHAR(25),
        description VARCHAR(250)
    )
    """
    cursor.execute(create_table_query)
    #un comentario que si se ejecuto
    db_connection.commit()

    #se cierra
    cursor.close()
    db_connection.close()
    print("tabla LIBROS creada")


def crear_tabla_usuarios():
    
    create_table_query ="""
    CREATE TABLE usuarios
    (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(50),
        email VARCHAR(30),
        password VARCHAR(200)
    )
    """
    cursor.execute(create_table_query)
    #un comentario que si se ejecuto
    db_connection.commit()

    #se cierra
    cursor.close()
    db_connection.close()
    print("tabla USUARIOS creada")


print("Hola, acá puedes crear las tabla del sistema de biblioteca")
print("1. Crear tabla LIBROS")
print("2. Crear tabla USUARIOS")
opcion = input("Ingrese una opción: ")

if opcion == "1":
    crear_tabla_libros()
elif opcion == "2":
    crear_tabla_usuarios()
else:
    print("Opción inválida.")