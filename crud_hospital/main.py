
from methods.pacientes_options import crear_paciente, leer_paciente, actualizar_paciente, eliminar_paciente
from methods.trabajadores_options import crear_trabajador, leer_trabajador, actualizar_trabajador, eliminar_trabajador
from methods.departamentos_options import crear_departamento, leer_departamento, actualizar_departamento, eliminar_departamento
from database.consultas_bd import read_pacientes_dengue_bd, read_pacientes_cirugia_bd, read_doctores_departamento_bd, read_enfermeros_bd

def create():
    while True:
     print("\nIngresar nuevos datos al hospital")
     print("1. Ingresar nuevo paciente")
     print("2. Ingresar nuevo trabajador")
     print("3. Ingresar nuevo departamento")
     print("0. Salir")
     opcion = input("Ingrese una opción: ") 
     if opcion == "1":
         crear_paciente()
     elif opcion == "2":
         crear_trabajador()
     elif opcion == "3":
         crear_departamento()
     elif opcion == "0":
         print("¡Hasta luego!")
         break
     else:
         print("Opción inválida. Intente nuevamente.")

def read():
    while True:
     print("\n_________Consulta datos del hospital__________")
     print("1. Consultar pacientes")
     print("2. Consultar trabajadores")
     print("3. Consultar departamentos")
     print("0. Salir")
     opcion = input("Ingrese una opción: ") 
     if opcion == "1":
         leer_paciente()
     elif opcion == "2":
         leer_trabajador()
     elif opcion == "3":
         leer_departamento()
     elif opcion == "0":
         print("¡Hasta luego!")
         break
     else:
         print("Opción inválida. Intente nuevamente.")

def update():
    while True:
        print("\nActualizar datos del hospital")
        print("1. Actualizar información de un paciente")
        print("2. Actualizar información de un trabajador")
        print("3. Actualizar información de un departamento")
        print("0. Salir")
        opcion = input("Ingrese una opción: ") 
        if opcion == "1":
            actualizar_paciente()
        elif opcion == "2":
            actualizar_trabajador()
        elif opcion == "3":
            actualizar_departamento()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")






def delete():
    while True:
     print("\nEliminar datos del hospital")
     print("1. Eliminar paciente")
     print("2. Eliminar trabajador")
     print("3. Eliminar departamento")
     print("0. Salir")
     opcion = input("Ingrese una opción: ") 
     if opcion == "1":
         eliminar_paciente()
     elif opcion == "2":
         eliminar_trabajador()
     elif opcion == "3":
         eliminar_departamento()
     elif opcion == "0":
         print("¡Hasta luego!")
         break
     else:
         print("Opción inválida. Intente nuevamente.")


def consultas():
     
     while True:
        print("\n ------Consulta personalizada-----")
        print("1. Consultar pacientes internados por cirugia")
        print("2. Consultar pacientes internados por dengue")
        print("3. Consultar doctores por departamento")
        print("4. Consultar total enfermeros en el hospital")

        print("0. Salir")
        opcion = input("Ingrese una opción: ") 
        if opcion == "1":
         read_pacientes_cirugia_bd()
         
        elif opcion == "2":
         read_pacientes_dengue_bd()
        elif opcion == "3":
         read_doctores_departamento_bd()
        elif opcion == "4":
         read_enfermeros_bd()
        elif opcion == "0":
         print("¡Hasta luego!")
         break
        else:
         print("Opción inválida. Intente nuevamente.")




# Menú principal
def menu_principal():


    while True:
        print("\nBienvenido al sistema del hospital")
        print("1. Ingresar datos")
        print("2. Visualizar datos")
        print("3. Actualizar datos")
        print("4. Eliminar datos")
        print("5. Consultas personalizadas")
        print("0. Salir")
        opcion = input("Ingrese una opción: ")

        if opcion == "1":
            create()
        elif opcion == "2":
            read()
        elif opcion == "3":
            update()
        elif opcion == "4":
            delete()
        elif opcion == "5":
            consultas()
        elif opcion == "0":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intente nuevamente.")



menu_principal();