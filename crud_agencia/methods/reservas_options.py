from database.reservas_bd import insert_reserva_bd, read_reservas_bd, update_reserva_bd, delete_reserva_bd

# Función para crear una nueva reserva
def crear_reserva():
    aerolinea = input("Ingrese el nombre de la aerolínea: ")
    fecha = input("Ingrese la fecha de la reserva (YYYY-MM-DD): ")
    destino = input("Ingrese el destino: ")

    insert_reserva_bd(aerolinea, fecha, destino)

    print("Reserva creada con éxito.")

# Función para leer todas las reservas
def leer_reservas():
    data = read_reservas_bd()

    if data:
        print("Lista de reservas:")
        for reserva in data:
            print(f"ID: {reserva[0]}, Aerolínea: {reserva[1]}, Fecha: {reserva[2]}, Destino: {reserva[3]}")
    else:
        print("No hay reservas en la base de datos.")

# Función para actualizar una reserva existente
def actualizar_reserva():
    data = read_reservas_bd()

    if data:
        print("Lista de reservas:")
        for reserva in data:
            print(f"ID: {reserva[0]}, Aerolínea: {reserva[1]}, Fecha: {reserva[2]}, Destino: {reserva[3]}")
    else:
        print("No hay reservas en la base de datos.")

    reserva_id = int(input("Ingrese el ID de la reserva a actualizar: "))
    nueva_aerolinea = input("Ingrese el nuevo nombre de la aerolínea: ")
    nueva_fecha = input("Ingrese la nueva fecha de la reserva (YYYY-MM-DD): ")
    nuevo_destino = input("Ingrese el nuevo destino: ")

    update_reserva_bd(reserva_id, nueva_aerolinea, nueva_fecha, nuevo_destino)

    print("Reserva actualizada exitosamente.")

# Función para eliminar una reserva existente
def eliminar_reserva():
    data = read_reservas_bd()

    if data:
        print("Lista de reservas:")
        for reserva in data:
            print(f"ID: {reserva[0]}, Aerolínea: {reserva[1]}, Fecha: {reserva[2]}, Destino: {reserva[3]}")
    else:
        print("No hay reservas en la base de datos.")

    reserva_id = int(input("Ingrese el ID de la reserva a eliminar: "))

    delete_reserva_bd(reserva_id)

    print("Reserva eliminada exitosamente.")
