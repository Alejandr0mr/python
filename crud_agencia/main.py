
from methods.usuarios_options import crear_usuario, leer_usuarios, actualizar_usuario, eliminar_usuario
from methods.hoteles_options import crear_hotel, leer_hoteles, actualizar_hotel, eliminar_hotel
from methods.reservas_options import crear_reserva, leer_reservas, actualizar_reserva, eliminar_reserva

def usuarios():
    while True:
     print("\nSistema para gestiona usuarios de la aerolina")
     print("1. Ingresar un usuario")
     print("2. Ver usuarios")
     print("3. Modificar usuario")
     print("4. Eliminar usuario")
     print("0. Salir")
     opcion = input("Ingrese una opción: ") 
     if opcion == "1":
         crear_usuario()
     elif opcion == "2":
         leer_usuarios()
     elif opcion == "3":
         actualizar_usuario()
     elif opcion == "4":
         eliminar_usuario()
     elif opcion == "0":
         print("¡Hasta luego!")
         break
     else:
         print("Opción inválida. Intente nuevamente.")

def hoteles():
    while True:
     print("\nSistema para gestiona los hoteles de la aerolina")
     print("1. Ingresar un hotel")
     print("2. Ver hoteles")
     print("3. Modificar hotel")
     print("4. Eliminar hotel")
     print("0. Salir")
     opcion = input("Ingrese una opción: ") 
     if opcion == "1":
         crear_hotel()
     elif opcion == "2":
         leer_hoteles()
     elif opcion == "3":
         actualizar_hotel()
     elif opcion == "4":
         eliminar_hotel()
     elif opcion == "0":
         print("¡Hasta luego!")
         break
     else:
         print("Opción inválida. Intente nuevamente.")

def reservas():
    while True:
     print("\nSistema para gestiona las reservas/vuelos de la aerolina")
     print("1. Ingresar una reserva")
     print("2. Ver reservas")
     print("3. Modificar reserva")
     print("4. Eliminar reserva")
     print("0. Salir")
     opcion = input("Ingrese una opción: ") 
     if opcion == "1":
         crear_reserva()
     elif opcion == "2":
         leer_reservas()
     elif opcion == "3":
         actualizar_reserva()
     elif opcion == "4":
         eliminar_reserva()
     elif opcion == "0":
         print("¡Hasta luego!")
         break
     else:
         print("Opción inválida. Intente nuevamente.")






# Menú principal
def menu_principal():


    while True:
        print("\nBienvenido al sistema de agencia de viajes")
        print("1. Usuarios")
        print("2. Hoteles")
        print("3. Reservas")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            usuarios()
        elif opcion == "2":
            hoteles()
        elif opcion == "3":
            reservas()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")



menu_principal();