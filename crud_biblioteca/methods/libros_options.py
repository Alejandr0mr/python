from bd.libros_db import insert_libros_bd, read_libros_bd, update_libros_bd, delete_libros_bd

# Función para crear un nuevo libro
def crear_libro():
    titulo = input("Ingrese el título del libro: ")
    autor = input("Ingrese el autor del libro: ")
    descripcion = input("Ingrese la descripción del libro: ")

    insert_libros_bd(titulo, autor, descripcion)
    print("Libro creado exitosamente.")

# Función para leer todos los libros
def leer_libros():
    data = read_libros_bd()

    # Recuperar los datos y mostrarlos
    if data:
        print("Lista de libros:")
        for row in data:
            print(f"ID: {row[0]}, Título: {row[1]}, Autor: {row[2]}, Descripción: {row[3]}")
    else:
        print("No hay libros en la biblioteca.")

# Función para actualizar un libro existente
def actualizar_libro():
    
    data = read_libros_bd();
    
    if data:
        print("Lista de libros disponibles.:")
        for row in data:
            print(f"ID: {row[0]}, Título: {row[1]}, Autor: {row[2]}, Descripción: {row[3]}")
    else:
        print("No hay libros en la biblioteca.")
    
    
    libro_id = input("Ingrese el ID del libro a actualizar: ")
    nuevo_titulo = input("Ingrese el nuevo título del libro: ")
    nuevo_autor = input("Ingrese el nuevo autor del libro: ")
    nueva_descripcion = input("Ingrese la nueva descripción del libro: ")

    update_libros_bd(libro_id, nuevo_titulo, nuevo_autor, nueva_descripcion)
    print("Libro actualizado exitosamente.")

# Función para eliminar un libro existente
def eliminar_libro():
    data = read_libros_bd();
    
    #Muestra los datos para ver los lirbos.
    if data:
        print("Lista de libros:")
        for row in data:
            print(f"ID: {row[0]}, Título: {row[1]}, Autor: {row[2]}, Descripción: {row[3]}")
    else:
        print("No hay libros en la biblioteca.")
    
    libro_id = input("Ingrese el ID del libro a eliminar: ")

    delete_libros_bd(libro_id)
    print("Libro eliminado exitosamente.")
