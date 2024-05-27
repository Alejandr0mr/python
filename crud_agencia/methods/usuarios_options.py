from database.usuarios_bd import insert_usuario_bd, read_usuarios_bd, update_usuario_bd, delete_usuario_bd
from database.hoteles_bd import read_hoteles_bd
from database.reservas_bd import read_reservas_bd

# Función para crear un nuevo usuario
def crear_usuario():
    data_hoteles = read_hoteles_bd()
    data_reservas = read_reservas_bd()

    nombre = input("Ingrese nombre del usuario: ")
    apellido = input("Ingrese el apellido del usuario: ")
    identificacion = int(input("Ingrese la identificación del usuario: "))

    if data_hoteles:
        print("Lista de hoteles:")
        for hotel in data_hoteles:
            print(f"ID: {hotel[0]}, Nombre: {hotel[1]}")
    else:
        print("No hay hoteles en la base de datos.")

    id_hotel = int(input("Ingrese el ID del hotel: "))

    if data_reservas:
        print("Lista de reservas:")
        for reserva in data_reservas:
            print(f"ID: {reserva[0]}, Aerolinea: {reserva[1]}, Fecha: {reserva[2]}, Destino: {reserva[3]}")
    else:
        print("No hay reservas en la base de datos.")

    id_reserva = int(input("Ingrese el ID de la reserva: "))

    insert_usuario_bd(nombre, apellido, identificacion, id_hotel, id_reserva)

    print("Usuario creado con éxito.")

# Función para leer todos los usuarios
def leer_usuarios():
    data = read_usuarios_bd()

    if data:
        print("Lista de usuarios:")
        for usuario in data:
            print(f"ID: {usuario[0]}, Nombre: {usuario[1]} {usuario[2]}, Identificación: {usuario[3]}, ID Hotel: {usuario[4]}, ID Reserva: {usuario[5]}")
    else:
        print("No hay usuarios en la base de datos.")

# Función para actualizar un usuario existente
def actualizar_usuario():
    data_hoteles = read_hoteles_bd()
    data_reservas = read_reservas_bd()
    
    data = read_usuarios_bd()

    if data:
        print("Lista de usuarios:")
        for usuario in data:
            print(f"ID: {usuario[0]}, Nombre: {usuario[1]} {usuario[2]}, Identificación: {usuario[3]}, ID Hotel: {usuario[4]}, ID Reserva: {usuario[5]}")
    else:
        print("No hay usuarios en la base de datos.")

    usuario_id = input("Ingrese el ID del usuario a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del usuario: ")
    nuevo_apellido = input("Ingrese el nuevo apellido del usuario: ")
    nueva_identificacion = int(input("Ingrese la nueva identificación del usuario: "))

    
    if data_hoteles:
        print("Lista de hoteles:")
        for hotel in data_hoteles:
            print(f"ID: {hotel[0]}, Nombre: {hotel[1]}")
    else:
        print("No hay hoteles en la base de datos.")

    nuevo_id_hotel = int(input("Ingrese el nuevo ID del hotel: "))

    if data_reservas:
        print("Lista de reservas:")
        for reserva in data_reservas:
            print(f"ID: {reserva[0]}, Aerolinea: {reserva[1]}, Fecha: {reserva[2]}, Destino: {reserva[3]}")
    else:
        print("No hay reservas en la base de datos.")


    nuevo_id_reserva = int(input("Ingrese el nuevo ID de la reserva: "))

    update_usuario_bd(usuario_id, nuevo_nombre, nuevo_apellido, nueva_identificacion, nuevo_id_hotel, nuevo_id_reserva)

    print("Usuario actualizado exitosamente.")

# Función para eliminar un usuario existente
def eliminar_usuario():
    data = read_usuarios_bd()

    if data:
        print("Lista de usuarios:")
        for usuario in data:
            print(f"ID: {usuario[0]}, Nombre: {usuario[1]} {usuario[2]}, Identificación: {usuario[3]}, ID Hotel: {usuario[4]}, ID Reserva: {usuario[5]}")
    else:
        print("No hay usuarios en la base de datos.")

    usuario_id = input("Ingrese el ID del usuario a eliminar: ")

    delete_usuario_bd(usuario_id)

    print("Usuario eliminado exitosamente.")