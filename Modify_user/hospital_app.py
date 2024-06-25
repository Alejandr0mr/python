import tkinter as tk
from tkinter import ttk, messagebox
from db_connection import DatabaseConnection

class HospitalApp:
    def __init__(self, root):
        # Inicializa la aplicación
        self.root = root
        self.root.title("Hospital Application")
        
        # Crea una conexión a la base de datos
        self.db = DatabaseConnection()
        
        # Crea los elementos visuales de la aplicación
        self.create_widgets()

    def create_widgets(self):
        # Crea un sistema de pestañas
        self.notebook = ttk.Notebook(self.root)
        self.notebook.pack(expand=True, fill="both", padx=10, pady=10)
        
        # Crea la pestaña para modificar usuarios
        self.create_modify_user_tab()

    def create_modify_user_tab(self):
        # Crea un marco para la pestaña de modificar usuario
        modify_frame = ttk.Frame(self.notebook)
        self.notebook.add(modify_frame, text="Modificar Usuario")

        # Crea un menú desplegable para seleccionar usuarios
        ttk.Label(modify_frame, text="Seleccione un usuario:").grid(row=0, column=0, padx=5, pady=5)
        self.user_combobox = ttk.Combobox(modify_frame, state="readonly")
        self.user_combobox.grid(row=0, column=1, padx=5, pady=5)
        
        # Cuando se selecciona un usuario, carga sus datos
        self.user_combobox.bind("<<ComboboxSelected>>", self.load_user_data)
        
        # Llena el menú desplegable con los usuarios
        self.populate_user_combobox()

        # Define los campos de información del usuario
        self.fields = ['nombre', 'apellido', 'email', 'telefono', 'id_departamento', 'diagnostico']
        self.entries = {}
        
        # Crea etiquetas y campos de entrada para cada atributo del usuario
        for i, field in enumerate(self.fields):
            ttk.Label(modify_frame, text=field.capitalize() + ":").grid(row=i+1, column=0, padx=5, pady=5)
            self.entries[field] = ttk.Entry(modify_frame)
            self.entries[field].grid(row=i+1, column=1, padx=5, pady=5)

        # Crea un botón para guardar cambios
        ttk.Button(modify_frame, text="Guardar cambios", command=self.save_changes).grid(row=len(self.fields)+1, column=0, columnspan=2, pady=10)

    def populate_user_combobox(self):
        # Obtiene la lista de usuarios de la base de datos
        users = self.db.get_users()
        # Llena el menú desplegable con los nombres de los usuarios
        self.user_combobox['values'] = [f"{user['id_usuario']} - {user['nombre']} {user['apellido']}" for user in users]

    def load_user_data(self, event):
        # Obtiene el usuario seleccionado del menú desplegable
        selected = self.user_combobox.get()
        if selected:
            # Extrae el ID del usuario
            user_id = int(selected.split(' - ')[0])
            # Obtiene los datos del usuario de la base de datos
            user_data = self.db.get_user(user_id)
            if user_data:
                # Llena los campos de entrada con los datos del usuario
                for field in self.fields:
                    self.entries[field].delete(0, tk.END)
                    self.entries[field].insert(0, str(user_data[field]))

    def save_changes(self):
        # Obtiene el usuario seleccionado
        selected = self.user_combobox.get()
        if not selected:
            messagebox.showerror("Error", "Por favor, seleccione un usuario")
            return
        
        # Extrae el ID del usuario
        user_id = int(selected.split(' - ')[0])
        changes_made = False
        
        # Actualiza cada campo en la base de datos
        for field in self.fields:
            new_value = self.entries[field].get()
            if self.db.update_user(user_id, field, new_value):
                changes_made = True
        
        # Muestra un mensaje según si se hicieron cambios o no
        if changes_made:
            messagebox.showinfo("Éxito", "Cambios guardados correctamente")
            self.populate_user_combobox()
        else:
            messagebox.showinfo("Información", "No se realizaron cambios")

    def __del__(self):
        # Cierra la conexión a la base de datos al cerrar la aplicación
        self.db.close_connection()

if __name__ == "__main__":
    # Crea la ventana principal
    root = tk.Tk()
    root.geometry("500x400")
    # Crea una instancia de la aplicación
    app = HospitalApp(root)
    # Inicia el bucle principal de la aplicación
    root.mainloop()