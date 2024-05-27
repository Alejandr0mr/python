from database.hoteles_bd import insert_hotel_bd, read_hoteles_bd, update_hotel_bd, delete_hotel_bd
# Función para crear un nuevo hotel
def crear_hotel():
    nombre = input("Ingrese el nombre del hotel: ")
    direccion = input("Ingrese la dirección del hotel: ")
    ciudad = input("Ingrese la ciudad del hotel: ")

    insert_hotel_bd(nombre, direccion, ciudad)

    print("Hotel creado con éxito.")

# Función para leer todos los hoteles
def leer_hoteles():
    data = read_hoteles_bd()

    if data:
        print("Lista de hoteles:")
        for hotel in data:
            print(f"ID: {hotel[0]}, Nombre: {hotel[1]}, Dirección: {hotel[2]}, Ciudad: {hotel[3]}")
    else:
        print("No hay hoteles en la base de datos.")

# Función para actualizar un hotel existente
def actualizar_hotel():
    data = read_hoteles_bd()

    if data:
        print("Lista de hoteles:")
        for hotel in data:
            print(f"ID: {hotel[0]}, Nombre: {hotel[1]}, Dirección: {hotel[2]}, Ciudad: {hotel[3]}")
    else:
        print("No hay hoteles en la base de datos.")

    hotel_id = int(input("Ingrese el ID del hotel a actualizar: "))
    nuevo_nombre = input("Ingrese el nuevo nombre del hotel: ")
    nueva_direccion = input("Ingrese la nueva dirección del hotel: ")
    nueva_ciudad = input("Ingrese la nueva ciudad del hotel: ")

    update_hotel_bd(hotel_id, nuevo_nombre, nueva_direccion, nueva_ciudad)

    print("Hotel actualizado exitosamente.")

# Función para eliminar un hotel existente
def eliminar_hotel():
    data = read_hoteles_bd()

    if data:
        print("Lista de hoteles:")
        for hotel in data:
            print(f"ID: {hotel[0]}, Nombre: {hotel[1]}, Dirección: {hotel[2]}, Ciudad: {hotel[3]}")
    else:
        print("No hay hoteles en la base de datos.")

    hotel_id = int(input("Ingrese el ID del hotel a eliminar: "))

    delete_hotel_bd(hotel_id)

    print("Hotel eliminado exitosamente.")
