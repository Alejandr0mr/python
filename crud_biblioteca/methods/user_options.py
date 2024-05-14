# Importamos las funciones
from bd.usuarios_db import insert_usuarios_bd, read_usuarios_bd

# Inicio de sesión
def iniciar_sesion():
    #Traemos todos los usuarios
    usuarios = read_usuarios_bd()

    name = input("Ingrese su nombre de usuario: ")
    password = input("Ingrese su contraseña: ")

    for user in usuarios:
        #Hacemos la validación
        if user[1] == name and user[3] == password:
            print("Inicio de sesión exitoso.")
            return True

    print("Nombre de usuario o contraseña incorrectos.")
    return False

# Crear un nuevo usuario
def crear_usuario():
    name = input("Ingrese un nombre de usuario: ")
    email = input("Ingrese un correo electrónico: ")
    password = input("Ingrese una contraseña: ")

    insert_usuarios_bd(name, email, password)
    print("Usuario creado exitosamente.")