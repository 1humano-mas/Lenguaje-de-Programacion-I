#JUAN MERCEDES / LR-2024-02270
import tkinter as tk

# Debes escribir un usuario y contraseña
USUARIO = "Admin"
PASSWORD = "12345678"

# Funciones
def capturar_credenciales():
  usuario = input_usuario.get()
  password = input_password.get()

  # El método config admite argumento foreground="" con el cuál podemos especificar el color del texto
  if usuario == USUARIO:
      mensaje.config(text="Acceso correcto", bg="green2", fg="white")
      mensaje.pack()
  else:  
      mensaje.config(text="Contraseña o usuario incorrectos", bg="red", fg="white")
      mensaje.pack()
  

# Ventana principal
ventana = tk.Tk()
ventana.geometry("500x600")
ventana.title("Mi primera app con Tkinter")
ventana.config(bg="blue")

frame1 = tk.Frame(ventana, width=350, height=450, bg="lightblue")
frame1.pack(pady=100)
frame1.pack_propagate(False)

# Widgets
etiqueta_usuario = tk.Label(frame1, text="Usuario", font=("Arial", 14, "bold"))
etiqueta_usuario.pack(pady=(100, 10))

input_usuario = tk.Entry(frame1, font=("Arial", 12))
input_usuario.pack()

etiqueta_password = tk.Label(frame1, text="Password", font=("Arial", 14, "bold"))
etiqueta_password.pack(pady=(50,10))

input_password = tk.Entry(frame1, font=("Arial", 12), show="*")
input_password.pack()

mensaje = tk.Label(frame1, font=("Arial", 14, "bold"))

boton = tk.Button(frame1, text="Iniciar Seccion", bg="darkblue", fg="white",font=("Arial", 14, "bold"), command=capturar_credenciales)
boton.pack(pady=10)

ventana.mainloop()