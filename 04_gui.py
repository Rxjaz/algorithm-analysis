import tkinter as tk

def saludar():
    nombre = entrada.get().strip()
    if not nombre:
        nombre = "Ariel"
    lbl.config(text=f"Hola, {nombre}")

root  = tk.Tk()
root.title("Saludador de compas")
root.geometry("360x220")
lbl = tk.Label(root, text="Escribe tu nombre")
lbl.pack(pady=30)

entrada = tk.Entry(root)
entrada.pack(pady=10)

boton = tk.Button(root, text="Saludar", command=saludar)
boton.pack(pady=1)

root.mainloop()