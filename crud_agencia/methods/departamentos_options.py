from database.departamentos_bd import insert_departamento_bd, read_departamentos_bd, update_departamento_bd, delete_departamento_bd

# Función para crear un nuevo departamento
def crear_departamento():
    nombre = input("Ingrese el nombre del departamento: ")

    # Insertar el departamento en la base de datos
    insert_departamento_bd(nombre)

    print("Departamento creado con éxito.")

# Función para leer todos los departamentos
def leer_departamento():
    # Obtener los departamentos de la base de datos
    data = read_departamentos_bd()

    if data:
        print("Lista de departamentos:")
        for departamento in data:
            print(f"ID: {departamento[0]}, Nombre: {departamento[1]}")
    else:
        print("No hay departamentos en la base de datos.")

# Función para actualizar un departamento existente
def actualizar_departamento():
    # Obtener los departamentos de la base de datos
    data = read_departamentos_bd()

    if data:
        print("Lista de departamentos:")
        for departamento in data:
            print(f"ID: {departamento[0]}, Nombre: {departamento[1]}")
    else:
        print("No hay departamentos en la base de datos.")

    departamento_id = int(input("Ingrese el ID del departamento a actualizar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre del departamento: ")

    # Actualizar el departamento en la base de datos
    update_departamento_bd(departamento_id, nuevo_nombre)

    print("Departamento actualizado exitosamente.")

# Función para eliminar un departamento existente
def eliminar_departamento():
    # Obtener los departamentos de la base de datos
    data = read_departamentos_bd()

    if data:
        print("Lista de departamentos:")
        for departamento in data:
            print(f"ID: {departamento[0]}, Nombre: {departamento[1]}")
    else:
        print("No hay departamentos en la base de datos.")

    departamento_id = int(input("Ingrese el ID del departamento a eliminar: "))

    # Eliminar el departamento de la base de datos
    delete_departamento_bd(departamento_id)

    print("Departamento eliminado exitosamente.")
