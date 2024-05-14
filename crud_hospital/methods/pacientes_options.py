from database.pacientes_bd import insert_paciente_bd, read_pacientes_bd, update_paciente_bd, delete_paciente_bd


# Función para crear un nuevo paciente
def crear_paciente():
    nombre = input("Ingrese nombre del paciente: ")
    apellido = input("Ingrese el apellido del paciente: ")
    identificacion = int(input("Ingrese la identificación del paciente: "))
    fecha_nacimiento = input("Ingrese la fecha de nacimiento del paciente (YYYY-MM-DD): ")
    genero = input("Ingrese el género del paciente: ")
    motivo_consulta = input("Ingrese el motivo de la consulta del paciente: ")
    diagnostico = input("Ingrese el diagnóstico del paciente: ")

    # Aquí iría la función para insertar el paciente en la base de datos, 
    insert_paciente_bd(nombre, apellido, identificacion, fecha_nacimiento, genero, motivo_consulta, diagnostico)

    print("Paciente creado con éxito.")

# Función para leer todos los pacientes
def leer_paciente():
    # Aquí iría la función para leer todos los pacientes de la base de datos,
    data = read_pacientes_bd()

    if data:
        print("Lista de pacientes:")
        for paciente in data:
            print(f"ID: {paciente[0]}, Nombre: {paciente[1]} {paciente[2]}, Identificación: {paciente[3]}, Fecha de Nacimiento: {paciente[4]}, Género: {paciente[5]}, Motivo de consulta: {paciente[6]}, Diagnóstico: {paciente[7]}")
    else:
        print("No hay pacientes en la base de datos.")

    
    

# Función para actualizar un paciente existente
def actualizar_paciente():
    data = read_pacientes_bd()

    if data:
        print("Lista de pacientes:")
        for paciente in data:
            print(f"ID: {paciente[0]}, Nombre: {paciente[1]} {paciente[2]}, Identificación: {paciente[3]}, Fecha de Nacimiento: {paciente[4]}, Género: {paciente[5]}, Motivo de consulta: {paciente[6]}, Diagnóstico: {paciente[7]}")
    else:
        print("No hay pacientes en la base de datos.")

    paciente_id = input("Ingrese el ID del paciente a actualizar: ")
    nuevo_nombre = input("Ingrese el nuevo nombre del paciente: ")
    nuevo_apellido = input("Ingrese el nuevo apellido del paciente: ")
    nueva_identificacion = int(input("Ingrese la nueva identificación del paciente: "))
    nueva_fecha_nacimiento = input("Ingrese la nueva fecha de nacimiento del paciente (YYYY-MM-DD): ")
    nuevo_genero = input("Ingrese el nuevo género del paciente: ")
    nuevo_motivo_consulta = input("Ingrese el nuevo motivo de la consulta del paciente: ")
    nuevo_diagnostico = input("Ingrese el nuevo diagnóstico del paciente: ")

    # Aquí iría la función para actualizar el paciente en la base de datos
    update_paciente_bd(paciente_id, nuevo_nombre, nuevo_apellido, nueva_identificacion, nueva_fecha_nacimiento, nuevo_genero, nuevo_motivo_consulta, nuevo_diagnostico)

    print("Paciente actualizado exitosamente.")

# Función para eliminar un paciente existente
def eliminar_paciente():

    data = read_pacientes_bd()

    if data:
        print("Lista de pacientes:")
        for paciente in data:
            print(f"ID: {paciente[0]}, Nombre: {paciente[1]} {paciente[2]}, Identificación: {paciente[3]}, Fecha de Nacimiento: {paciente[4]}, Género: {paciente[5]}, Motivo de consulta: {paciente[6]}, Diagnóstico: {paciente[7]}")
    else:
        print("No hay pacientes en la base de datos.")

    paciente_id = input("Ingrese el ID del paciente a eliminar: ")

    delete_paciente_bd(paciente_id)

    print("Paciente eliminado exitosamente.")

def leer_cirujia():
    # Aquí iría la función para leer todos los pacientes de la base de datos,
    # como no proporcionaste la implementación, dejaré un comentario
    data = read_pacientes_bd()

    if data:
        print("Lista de pacientes:")
        for paciente in data:
            print(f"ID: {paciente[0]}, Nombre: {paciente[1]} {paciente[2]}, Identificación: {paciente[3]}, Fecha de Nacimiento: {paciente[4]}, Género: {paciente[5]}, Motivo de consulta: {paciente[6]}, Diagnóstico: {paciente[7]}")
    else:
        print("No hay pacientes en la base de datos.")
