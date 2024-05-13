from methods.user_options import iniciar_sesion, crear_usuario
from methods.libros_options import crear_libro, leer_libros, actualizar_libro, eliminar_libro

# Menú principal
def menu_principal():

    # menú que sale si el inicio de sesión es valido
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

# Iniciar el programa
print("Bienvenido al Sistema de Biblioteca")
print("1. Iniciar sesión")
print("2. Crear nuevo usuario")
opcion = input("Ingrese una opción: ")

if opcion == "1":
    # Llamamos la función de iniciar sesión y si es valido muestra el menú principal 
    if iniciar_sesion():
        menu_principal()
elif opcion == "2":
    crear_usuario()
else:
    print("Opción inválida.")