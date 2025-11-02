#JUAN MERCEDES / LR-2024-02270
import tkinter as tk

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x600")
        self.title("Mi primera app con Tkinter version Poo")
        self.config(bg="blue")
        self.create_widgets()
        
    USUARIO = "Admin"
    PASSWORD = "12345678"
    
    def iniciar_seccion(self):
        usuario = self.input_usuario.get()
        password = self.input_password.get()
        if usuario == self.USUARIO and password == self.PASSWORD:
            self.mensaje.config(text="Acceso correcto", bg="green2", fg="white")
            self.mensaje.pack()
        else:
            self.mensaje.config(text="Contraseña o usuario incorrectos", bg="red", fg="white")
            self.mensaje.pack()

    def create_widgets(self):
       self.frame1 = tk.Frame(self, width=350, height=450, bg="lightblue")
       self.frame1.pack(pady=100)
       self.frame1.pack_propagate(False)

       self.etiqueta_usuario = tk.Label(self.frame1, text="Usuario", font=("Arial", 14, "bold"))
       self.etiqueta_usuario.pack(pady=(100, 10))

       self.input_usuario = tk.Entry(self.frame1, font=("Arial", 12))
       self.input_usuario.pack()

       self.etiqueta_password = tk.Label(self.frame1, text="Password", font=("Arial", 14, "bold"))
       self.etiqueta_password.pack(pady=(50,10))

       self.input_password = tk.Entry(self.frame1, font=("Arial", 12), show="*")
       self.input_password.pack()

       self.mensaje = tk.Label(self.frame1, font=("Arial", 14, "bold"))

       self.boton = tk.Button(self.frame1, text="Iniciar Seccion", bg="darkblue", fg="white",font=("Arial", 14, "bold"), command=self.iniciar_seccion)
       self.boton.pack(pady=10)
    
if __name__ == "__main__":
    app = Login()
    app.mainloop()