import tkinter as tk 
from tkinter import ttk
import json

root= tk.Tk()
root.title("Login")
root.geometry("900x550")
root.configure(bg="#FDF0D5")

menu = tk.Menu(font=("Google Sans", 12),type="menubar", fg="#003049", bg="#FDF0D5")
menu.add_command(label="Inicio")
menu.add_command(label="Salir", command=root.quit)
root.config(menu=menu)


labelWelcome = tk.Label(root, text="Bienvenido",font=("Google Sans", 20), fg="#003049", bg="#FDF0D5")
labelWelcome.pack(pady=20)

inventory = {}

with open('database/product.json', 'r') as file:
    usuarios_dicc = json.load(file)

print(usuarios_dicc)


frame = tk.Frame(root, bg="#FDF0D5")
frame.pack(pady=10, fill="both", expand=True)

section1 = tk.LabelFrame(frame, text="Menu", font=("Google Sans", 14), fg="#003049", bg="#FDF0D5", width=300, height=250)
section1.pack(side="left", fill="both", expand=True, padx=10, pady=10)

section2 = tk.LabelFrame(frame, text="Compra", font=("Google Sans", 14), fg="#003049", bg="#FDF0D5", width=300, height=250)
section2.pack(side="right", fill="both", expand=True, padx=10, pady=10)
    
frameCat = tk.Frame(section1, bg="#FDF0D5", height=34, width=330)
frameCat.pack(pady=10)
   
cat = ttk.Combobox(frameCat, values=list(usuarios_dicc.keys()), font=("Google Sans", 12), state="readonly")
cat.set("Selecciona una categoría")

labelTitlecat = tk.Label(section1, text="Productos disponibles:", font=("Google Sans", 12), bg="#FDF0D5", fg="#003049")
labelTitlecat.pack(padx=5)

cat.place(x=0, y=5)

btnCat = tk.Button(frameCat, text="Seleccionar", font=("Google Sans Bold", 12), bg="#c1121f", fg="#FFFFFF", command=lambda: select_cat())
btnCat.place(x = 230, y = 0)


lista = tk.Listbox(section1, font=("Google Sans", 12), bg="#FFFFFF", fg="#003049")
lista.pack(pady=10, fill="both", expand=True, padx=10)


def select_cat():
    select_cat = cat.get()
    lista.delete(0, tk.END) 
    
    for producto in usuarios_dicc[select_cat].keys():
        lista.insert(tk.END, f"->{producto}")
    lista.pack(pady=10, fill="both", expand=True, padx=10)

btnAceptar = tk.Button(section1, text="Aceptar", font=("Google Sans", 12), bg="#c1121f", fg="#FFFFFF", width=10)
btnAceptar.pack(pady=10, padx=10, fill="both")



root.mainloop()