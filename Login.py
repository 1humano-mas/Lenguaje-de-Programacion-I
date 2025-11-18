import tkinter as tk
from tkinter import messagebox

ventana = tk.Tk()
ventana.title("Inicio de Seccion")
ventana.configure(bg="black")


frame_titulo = tk.Frame(ventana, bg="darkgreen")
frame_titulo.pack(fill="x")


titulo = tk.Label(frame_titulo, text="INICIO DE SECION", font=("Arial", 20, "bold"), bg="darkgreen", fg="white")
titulo.pack(pady=5)

frame1 = tk.Frame(ventana, width=300, height=450, bg="black",highlightbackground="green2", highlightcolor="green2",highlightthickness=2)
frame1.pack(pady=100)
frame1.pack_propagate(False)

cuentas = {
    "Admin": "",
    "Juan Mercedes": "12345678",
    "Roberto prado": "00000000"
}

def iniciar_seccion():
    usuario = entrada_usuario.get()
    contraseña = entrada_contraseña.get()
    
    if usuario in cuentas and cuentas[usuario] == contraseña:
        messagebox.showinfo("Correcto", f"Bienvenido {usuario}")
        etiqueta_error.config(text="")
    else:
        etiqueta_error.config(text="El usuario o la contraseña son incorrectos")
        
def registrarse():
    pass
    

etiqueta_usuario = tk.Label(frame1, text="USUARIO: ", font=("Arial", 15, "bold"), bg="black", fg="white")
etiqueta_usuario.pack(padx=(20,140),pady=(100,5))

entrada_usuario = tk.Entry(frame1, font=("Arial", 14), bg="black", fg="white", width=20, highlightcolor="green2", highlightthickness=2, insertbackground="white")
entrada_usuario.pack()

etiqueta_contraseña = tk.Label(frame1, text="CONTRASEÑA: ", font=("Arial", 15, "bold"), bg="black", fg="white")
etiqueta_contraseña.pack(padx=(20,100),pady=(50,5))

entrada_contraseña = tk.Entry(frame1, font=("Arial", 14), bg="black", fg="white", width=20, highlightcolor="green2", highlightthickness=2, insertbackground="white", show="*")
entrada_contraseña.pack(pady=10)

btn = tk.Button(frame1, text="Iniciar Seccion", font=("Arial", 10, "bold"), bg="green4", fg="white", command=iniciar_seccion)
btn.pack()

btn_registrarse = tk.Button(frame1,text="Registrarse", font=("Arial", 10, "bold"), bg="green", fg="white", command=registrarse)
btn_registrarse.pack(pady=(5,0))

etiqueta_error = tk.Label(frame1, text="", font=("Arial", 10), bg="black", fg="red")
etiqueta_error.pack()

ventana.mainloop()