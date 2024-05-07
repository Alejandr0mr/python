import json

# Cargar los usuarios desde el archivo JSON
def cargar_usuarios():
    try:
        with open("crud_biblioteca/json/usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        usuarios = []
    return usuarios

# Guardar los usuarios en el archivo JSON
def guardar_usuarios(usuarios):
    with open("crud_biblioteca/json/usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

# Inicio de sesión
def iniciar_sesion():
    usuarios = cargar_usuarios()
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    for user in usuarios:
        if user["usuario"] == usuario and user["contrasena"] == contrasena:
            print("Inicio de sesión exitoso.")
            return True
    print("Nombre de usuario o contraseña incorrectos.")
    return False

# Crear un nuevo usuario
def crear_usuario():
    usuarios = cargar_usuarios()
    usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    nuevo_usuario = {"usuario": usuario, "contrasena": contrasena}
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    print("Usuario creado exitosamente.")