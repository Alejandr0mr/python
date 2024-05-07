import json

# Cargar los usuarios desde el archivo JSON
def cargar_usuarios():
    try:
        with open("crud_ia/usuarios.json", "r") as archivo:
            usuarios = json.load(archivo)
    except FileNotFoundError:
        usuarios = []
    return usuarios

# Guardar los usuarios en el archivo JSON
def guardar_usuarios(usuarios):
    with open("crud_ia/usuarios.json", "w") as archivo:
        json.dump(usuarios, archivo, indent=4)

# Cargar los datos de los libros desde el archivo JSON
def cargar_libros():
    try:
        with open("crud_ia/libros.json", "r") as archivo:
            libros = json.load(archivo)
    except FileNotFoundError:
        libros = []
    return libros

# Guardar los datos de los libros en el archivo JSON
def guardar_libros(libros):
    with open("crud_ia/libros.json", "w") as archivo:
        json.dump(libros, archivo, indent=4)


# Inicio de sesión
def iniciar_sesion():
    usuarios = cargar_usuarios()
    usuario = input("Ingrese su nombre de usuario: ")
    contrasena = input("Ingrese su contraseña: ")
    for user in usuarios:
        if user["usuario"] == usuario and user["contrasena"] == contrasena:
            print("Inicio de sesión exitoso.")
            menu_principal()
            return
    print("Nombre de usuario o contraseña incorrectos.")

# Crear un nuevo libro
def crear_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    nuevo_libro = {"titulo": titulo, "autor": autor}
    libros = cargar_libros()
    libros.append(nuevo_libro)
    guardar_libros(libros)
    print("Libro creado exitosamente.")

# Leer todos los libros
def leer_libros():
    libros = cargar_libros()
    if libros:
        print("Lista de libros:")
        for libro in libros:
            print(f"Título: {libro['titulo']}, Autor: {libro['autor']}")
    else:
        print("No hay libros en la biblioteca.")

# Actualizar un libro existente
def actualizar_libro():
    libros = cargar_libros()
    titulo_actual = input("Ingrese el título del libro a actualizar: ")
    for libro in libros:
        if libro["titulo"] == titulo_actual:
            nuevo_titulo = input("Ingrese el nuevo título del libro: ")
            nuevo_autor = input("Ingrese el nuevo autor del libro: ")
            libro["titulo"] = nuevo_titulo
            libro["autor"] = nuevo_autor
            guardar_libros(libros)
            print("Libro actualizado exitosamente.")
            return
    print("No se encontró el libro especificado.")

# Eliminar un libro existente
def eliminar_libro():
    libros = cargar_libros()
    titulo_eliminar = input("Ingrese el título del libro a eliminar: ")
    for libro in libros:
        if libro["titulo"] == titulo_eliminar:
            libros.remove(libro)
            guardar_libros(libros)
            print("Libro eliminado exitosamente.")
            return
    print("No se encontró el libro especificado.")

# Menú principal
def menu_principal():
    while True:
        print("\nSistema de Biblioteca")
        print("1. Crear libro")
        print("2. Leer libros")
        print("3. Actualizar libro")
        print("4. Eliminar libro")
        print("5. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            crear_libro()
        elif opcion == "2":
            leer_libros()
        elif opcion == "3":
            actualizar_libro()
        elif opcion == "4":
            eliminar_libro()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")

# Crear un nuevo usuario
def crear_usuario():
    usuarios = cargar_usuarios()
    usuario = input("Ingrese un nombre de usuario: ")
    contrasena = input("Ingrese una contraseña: ")
    nuevo_usuario = {"usuario": usuario, "contrasena": contrasena}
    usuarios.append(nuevo_usuario)
    guardar_usuarios(usuarios)
    print("Usuario creado exitosamente.")

# Iniciar el programa
print("Bienvenido al Sistema de Biblioteca")
print("1. Iniciar sesión")
print("2. Crear nuevo usuario")
opcion = input("Ingrese una opción: ")

if opcion == "1":
    iniciar_sesion()
elif opcion == "2":
    crear_usuario()
else:
    print("Opción inválida.")