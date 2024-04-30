import json

class Users: 

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

    def register_menu():
        print("Registro:\n")
        name = input("\tNombre: ")
        email = input("\tCorreo: ")
        password = input("\tContraseña: ")
        
        # Obtener el siguiente ID disponible
        next_id = Users.get_next_id()
        
        User = Users(next_id, name, email, password)
        Users.registrar_usuario(User)
    

    def get_next_id():
        with open('./crud_biblioteca/bd/usuarios.json', 'r') as file:
            usuarios = json.load(file)

        if not usuarios:
            return 1
        else:
            return max(usuario['id'] for usuario in usuarios) + 1
    
    def registrar_usuario(user):
        usuario_dict = {
            'id': user.id,
            'nombre': user.name,
            'email': user.email,
            'password': user.password
        }

        with open('./crud_biblioteca/bd/usuarios.json', 'w', encoding="utf-8") as file:
            json.dump(usuario_dict, file)
            file.write('\n')  # Agregar un salto de línea después de cada usuario

        print(f"______________Usuario {usuario_dict['nombre']} registrado exitosamente!______________\n")


    def login(email, password):
        with open('./crud_biblioteca/bd/usuarios.json', 'r') as file:
            usuarios = json.load(file)

        for usuario in usuarios:
         if usuario['email'] == email and usuario['password'] == password:
            return True

        return False