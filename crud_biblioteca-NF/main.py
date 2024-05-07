
from methods.user_options import Users
# from methods.librarian_options import Admin

import json

print("\n_________Bienvenido al sistema de libros_________\n")

while True:
    print("Opciones disponibles:\n")
    print("\t1.Iniciar sesión")
    print("\t2.Registrarse")
    print("\t0.Salir\n")

    opc = int(input("Elija una opción: "))

    if opc == 1:
        print("Inicio de sesión:\n") 
        email = input("\tCorreo: ")
        password = input("\tContraseña: ")

        if Users.login(email, password):
            print("Inicio de sesión exitoso.")
        else:
            print("Correo o contraseña incorrectos.")

    elif opc == 2:
       Users.register_menu()
    elif opc == 0:
        print("Saliendo del sistema. ¡Hasta luego!")
        break 

    else:
        print("Opción no válida. Por favor, elija una opción válida.\n")


    
      