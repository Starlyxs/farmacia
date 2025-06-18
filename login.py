import tkinter as tk
import json
from tkinter import messagebox
usuarios_dicc = {}

root = tk.Tk()
root.title("Login") 
root.geometry("600x300")
# root.resizable(False, False)
root.configure(bg="#FDF0D5")

titulo = tk.Label(root, text="Login", font=("Google Sans Bold", 25), fg="#003049", bg="#FDF0D5")
titulo.pack(pady=20)

usuario_label = tk.Label(root, text="Usuario:", font=("Google Sans Bold", 12), fg="#355070", bg="#FDF0D5")
usuario_label.pack(pady=5)

usuario_entry = tk.Entry(root, font=("Google Sans Bold", 12))
usuario_entry.pack(pady=5)

pass_label = tk.Label(root, text="Contraseña:", font=("Google Sans Bold", 12), fg="#355070", bg="#FDF0D5")
pass_label.pack(pady=5)

pass_entry = tk.Entry(root, font=("Google Sans Bold", 12), show="*")
pass_entry.pack(pady=5)


def on_login():
    usuario = usuario_entry.get()
    contraseña = pass_entry.get()

    with open('database/user.json', 'r') as file:
        usuarios_dicc = json.load(file)

    if usuario in usuarios_dicc and usuarios_dicc[usuario]["password"] == contraseña:
        import main
        main
        root.destroy()
    else:
        if len(usuario) == 0 and len(contraseña) == 0:
            messagebox.showerror("Error", "Por favor, ingrese usuario y contraseña.")
        else:
            messagebox.showerror("Error", "Usuario o contraseña incorrectos.")
            
            
login_button = tk.Button(root, text="Login", font=("Google Sans Bold", 12), bg="#355070", fg="#FFFFFF", command=on_login)
login_button.pack(pady=20)

root.mainloop()