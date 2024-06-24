import mysql.connector
from mysql.connector import Error

class DatabaseConnection:
    def __init__(self):
        self.connection = None
        try:
            self.connection = mysql.connector.connect(
                host='localhost',
                database='hospital_bdd',
                user='root',
                password=''
            )
            if self.connection.is_connected():
                print("Conexión exitosa a la base de datos")
        except Error as e:
            print(f"Error al conectar a la base de datos: {e}")

    def get_users(self):
        if self.connection.is_connected():
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT id_usuario, nombre, apellido FROM usuarios")
            return cursor.fetchall()
        return []

    def get_user(self, user_id):
        if self.connection.is_connected():
            cursor = self.connection.cursor(dictionary=True)
            cursor.execute("SELECT * FROM usuarios WHERE id_usuario = %s", (user_id,))
            return cursor.fetchone()
        return None

    def update_user(self, user_id, field, value):
        if self.connection.is_connected():
            cursor = self.connection.cursor()
            query = f"UPDATE usuarios SET {field} = %s WHERE id_usuario = %s"
            cursor.execute(query, (value, user_id))
            self.connection.commit()
            return cursor.rowcount > 0
        return False

    def close_connection(self):
        if self.connection.is_connected():
            self.connection.close()
            print("Conexión a la base de datos cerrada")