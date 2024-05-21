from database.trabajadores_bd import insert_trabajador_bd, read_trabajador_bd, update_trabajador_bd, delete_trabajador_bd
from database.departamentos_bd import read_departamentos_bd
# Función para crear un nuevo trabajador
def crear_hotel():

    data = read_hotel_bd()


    nombre = input("Ingrese  del trabajador: ")
    apellido = input("Ingrese el apellido del trabajador: ")
    identificacion = int(input("Ingrese la identificación del trabajador: "))
    cargo = input("Ingrese el cargo del trabajador: ")

    if data:
        print("Lista de hoteles:")
        for hotel in data:
            print(f"ID: {hotel[0]}, Nombre: {hotel[1]}")
    else:
        print("No hay hotel en la base de datos.")

    id_departamento = int(input("Ingrese el ID del hotel: "))

    # Insertar el trabajador en la base de datos
    insert_trabajador_bd(nombre, apellido, identificacion, cargo, id_departamento)

    print("Trabajador creado con éxito.")

# Función para leer todos los trabajadores
def leer_trabajador():
    # Obtener los trabajadores de la base de datos
    data = read_trabajador_bd()

    if data:
        print("Lista de trabajadores:")
        for trabajador in data:
            print(f"ID: {trabajador[0]}, Nombre: {trabajador[1]} {trabajador[2]}, Identificación: {trabajador[3]}, Cargo: {trabajador[4]}, ID Departamento: {trabajador[5]}")
    else:
        print("No hay trabajadores en la base de datos.")

# Función para actualizar un trabajador existente
def actualizar_trabajador():
    # Obtener los trabajadores de la base de datos
    data_departamentos= read_departamentos_bd()

    data = read_trabajador_bd()

    if data_departamentos:
        print("Lista de trabajadores:")
        for trabajador in data_departamentos:
            print(f"ID: {trabajador[0]}, Nombre: {trabajador[1]} {trabajador[2]}, Identificación: {trabajador[3]}, Cargo: {trabajador[4]}, ID Departamento: {trabajador[5]}")
    else:
        print("No hay trabajadores en la base de datos.")

    trabajador_id = int(input("Ingrese el ID del trabajador a actualizar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre del trabajador: ")
    nuevo_apellido = input("Ingrese el nuevo apellido del trabajador: ")
    nueva_identificacion = int(input("Ingrese la nueva identificación del trabajador: "))
    nuevo_cargo = input("Ingrese el nuevo cargo del trabajador: ")
    nuevo_id_departamento = int(input("Ingrese el nuevo ID del departamento: "))

    # Actualizar el trabajador en la base de datos
    update_trabajador_bd(trabajador_id, nuevo_nombre, nuevo_apellido, nueva_identificacion, nuevo_cargo, nuevo_id_departamento)

    print("Trabajador actualizado exitosamente.")

# Función para eliminar un trabajador existente
def eliminar_trabajador():
    data = read_trabajador_bd()

    if data:
        print("Lista de trabajadores:")
        for trabajador in data:
            print(f"ID: {trabajador[0]}, Nombre: {trabajador[1]} {trabajador[2]}, Identificación: {trabajador[3]}, Cargo: {trabajador[4]}, ID Departamento: {trabajador[5]}")
    else:
        print("No hay trabajadores en la base de datos.")

    trabajador_id = int(input("Ingrese el ID del trabajador a eliminar: "))

    # Eliminar el trabajador de la base de datos
    delete_trabajador_bd(trabajador_id)

    print("Trabajador eliminado exitosamente.")
