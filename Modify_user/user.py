import mysql.connector

# Realizamos la conexión a la base de datos.
db_connection = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="hospital_bd"
)


cursor = db_connection.cursor()

def read_pacientes_cirugia_bd():
    read_data_query = """
    SELECT COUNT(id) AS total_cirugia
    FROM pacientes
    WHERE diagnostico LIKE '%cirugia%'

    """
    cursor.execute(read_data_query)
    data = cursor.fetchall()

    

    print("Total de pacientes con diagnóstico de cirugía:", data[0][0])



def read_pacientes_dengue_bd():
    read_data_query = """
    SELECT COUNT(id) AS total_dengue
    FROM pacientes
    WHERE diagnostico LIKE '%dengue%'
    """
    cursor.execute(read_data_query)
    
    data = cursor.fetchall()

    print("Total de pacientes con diagnóstico de dengue:", data[0][0])

def read_doctores_departamento_bd():

    print("Doctores por departamento:")

    read_data_query = """
    SELECT d.nombre AS departamento, COUNT(t.id) AS cantidad_doctores
    FROM trabajadores t
    JOIN departamentos d ON t.id_departamento = d.id
    WHERE t.cargo = 'doctor'
    GROUP BY d.nombre;
    """
    cursor.execute(read_data_query)
    data = cursor.fetchall()

    for departamento, cantidad_doctores in data:
        print(f"{departamento}: {cantidad_doctores}")


def read_enfermeros_bd():
    read_data_query = """
        SELECT COUNT(*) AS cantidad_enfermeros
        FROM trabajadores
        WHERE cargo = 'enfermero';
    """
    cursor.execute(read_data_query)
    data = cursor.fetchone()
    print("Cantidad de enfermeros en el hospital:", data[0])

    

def close_connection():
    cursor.close()
    db_connection.close()