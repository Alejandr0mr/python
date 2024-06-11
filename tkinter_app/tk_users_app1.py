import tkinter as tk
from tkinter import messagebox, simpledialog

class HospitalApp:
    """
    Class to create, delete and update users in the database
    """
    
    def __init__(self, root):
        self.root = root 
        # Name app
        self.root.title("Hospital application")
        
        self.users = {}
        
        # Muestra un label
        self.label = tk.Label(root, text="Hospital application")
        self.label.pack(pady=10)
        
        # Botones
        self.register_button = tk.Button(root, text="Register User", command=self.register_user)
        self.register_button.pack(pady=5)
        
        self.modify_button = tk.Button(root, text="Modify User", command=self.modify_user)
        self.modify_button.pack(pady=5)
        
        self.delete_button = tk.Button(root, text="Delete User", command=self.delete_user)
        self.delete_button.pack(pady=5)
        
        self.show_button = tk.Button(root, text="Show Users", command=self.show_users)
        self.show_button.pack(pady=5)

    def register_user(self):
        username = simpledialog.askstring("Input", "Username:")
        if not username:
            return
        if username in self.users:
            messagebox.showerror("Error", "User already exists")
            return
        password = simpledialog.askstring("Input", "Enter password:", show='*')
        if not password:
            return
        name = simpledialog.askstring("Input", "Enter full name:")
        if not name:
            return
        age = simpledialog.askinteger("Input", "Enter age:")
        if not age:
            return
        address = simpledialog.askstring("Input", "Enter address:")
        if not address:
            return

        # Almacenar los datos del usuario en el diccionario
        self.users[username] = {
            "username": username,
            "password": password,
            "name": name,
            "age": age,
            "address": address
        }

        messagebox.showinfo("Success", f"User {username} registered successfully")

    def modify_user(self):
        username = simpledialog.askstring("Modify", "Enter current username:")
        if not username:
            return
        if username not in self.users:
            messagebox.showerror("Error", "User does not exist")
    
    password = simpledialog.askstring("")

    def delete_user(self):
        username = simpledialog.askstring("Delete", "Enter username to delete:")
        if username and username in self.users:
            del self.users[username]
            messagebox.showinfo("Success", f"User {username} deleted successfully")
        else:
            messagebox.showwarning("Error", "User not found")
    
    def show_users(self):
        if not self.users:
            messagebox.showinfo("Users", "No users registered")
            return
        
        users_info = "Registered Users:\n\n"
        for username, details in self.users.items():
            users_info += (f"Username: {username}\n"
                           f"Full Name: {details['name']}\n"
                           f"Age: {details['age']}\n"
                           f"Address: {details['address']}\n"
                           f"{'-'*20}\n")
        
        messagebox.showinfo("Users", users_info)

if __name__ == "__main__":
    root = tk.Tk()
    app = HospitalApp(root)
    root.mainloop()
