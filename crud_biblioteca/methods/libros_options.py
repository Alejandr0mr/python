import json

# Cargar los datos de los libros desde el archivo JSON
def cargar_libros():
    try:
        with open("crud_biblioteca/json/libros.json", "r") as archivo:
            libros = json.load(archivo)
    except FileNotFoundError:
        libros = []
    return libros

# Guardar los datos de los libros en el archivo JSON
def guardar_libros(libros):
    with open("crud_biblioteca/json/libros.json", "w") as archivo:
        json.dump(libros, archivo, indent=4)

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