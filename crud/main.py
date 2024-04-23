import os
import json
# from methods.user_options import Usuario
# from methods.admin_options import Admin

class Usuario:
    def __init__(self, id, nombre, apellido, email, edad):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.email = email
        self.edad = edad

class AdministrarUsuario:
   


   #envio el id y el dato que voy a actuailizar
   def actualizar_usuario(id, datos):
        #leo el json
        with open(r'./crud/usuarios.json', encoding="utf-8") as file:
            usuarios_dict = json.load(file)


        usuarios_actualizados = []
        usuario_actualizado = False

        #busca el usuario con el id
        for usuario in usuarios_dict:
            if usuario['id'] == id:
                #actualiza los datos
                print("Tipo de variable usuario: ", type(usuario))
                usuario.update(datos)
                usuarios_actualizados.append(usuario)
                usuario_actualizado = True
            else:
                usuarios_actualizados.append(usuario)

        if usuario_actualizado:
            with open('./crud/usuarios.json', 'w', encoding="utf-8") as file:
                json.dump(usuarios_actualizados, file)
            return True
        else:
            return False
   
   def leer_usuario(id):
        with open('./crud/usuarios.json', 'r', encoding="utf-8") as file:
            usuarios_dict = json.load(file)

        for usuario in usuarios_dict:
            if usuario['id'] == id:
                return usuario


   def guardar_usuarios(lista_usuarios):
        usuarios_dict = []
        for usuario in lista_usuarios:
            usuario_dict = {
                'id': usuario.id,
                'nombre': usuario.nombre,
                'apellido': usuario.apellido,
                'email': usuario.email,
                'edad': usuario.edad
            }
            usuarios_dict.append(usuario_dict)

        with open('./crud/usuarios.json', 'w', encoding="utf-8") as file:
            json.dump(usuarios_dict, file)
            


    
            

usuario1 = Usuario(1, "Alejandro", "Martínez", "alejandro@gmail.com", 19) 
usuario2 = Usuario(2, "Mariana", "Bedoya", "mariana@gmail.com", 18) 

lista_usuarios = [usuario1, usuario2]
AdministrarUsuario.guardar_usuarios(lista_usuarios)


usuario_encontrado = AdministrarUsuario.leer_usuario(2)
if usuario_encontrado:
    print(f"Usuario encontrado: {usuario_encontrado}")
else:
    print("Usuario no encontrado")


resultado = AdministrarUsuario.actualizar_usuario(2, {'email': 'mariana.bedoya@example.com'})
if resultado:
    print("Usuario actualizado correctamente.")
else:
    print("No se encontró el usuario para actualizar.")

# print("Bienvenido al menú de usuario\n")
# print("Opciones disponibles:\n")
# print("\t1.Crear usuario")
# print("\t2.Modificar usuario")
# print("\t3.Leer todos los usuarios")
# print("\t4.Eliminar usuario")
# print("\t4.Salir")

# opc = int(input("Elija una opción"))


#guarde datos
# archivo =open(r"./crud/usuarios.txt", "w")
# archivo.write(usuario1.nombre)
# archivo.close()

#guarda en un diccionario
# dict_usuario = {'id': usuario1.id,
#                 'nombre': usuario1.nombre,
#                 'apellido': usuario1.apellido,
#                 'email': usuario1.email,
#                 'edad': usuario1.edad}

