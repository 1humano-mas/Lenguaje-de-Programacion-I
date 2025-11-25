#JUAN MERCEDES / LR-2024-02270
import tkinter as tk

class Login(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x600")
        self.title("INICIAR SECCION CON .GRID")
        self.config(bg="blue")
        self.create_widgets()
        
    USUARIO = "Admin"
    PASSWORD = "12345678"

    def iniciar_seccion(self):
        usuario = self.input_usuario.get()
        password = self.input_password.get()

        if usuario == self.USUARIO and password == self.PASSWORD:
            self.mensaje.config(text="Acceso correcto", bg="green2", fg="white")
            self.mensaje.grid(row=5, column=0, pady=10)
        else:
            self.mensaje.config(text="Usuario o contraseña incorrectos", bg="red", fg="white")
            self.mensaje.grid(row=5, column=0, pady=10)

    def create_widgets(self):

        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(0, weight=1)

        self.frame1 = tk.Frame(self, width=350, height=450, bg="lightblue")
        self.frame1.grid(row=0, column=0)
        self.frame1.grid_propagate(False)
        self.frame1.grid_columnconfigure(0, weight=1)

        self.etiqueta_usuario = tk.Label(self.frame1, text="Usuario", font=("Arial", 14, "bold"))
        self.etiqueta_usuario.grid(row=0, column=0, pady=(60, 10), sticky="n")

        self.input_usuario = tk.Entry(self.frame1, font=("Arial", 12), width=22)
        self.input_usuario.grid(row=1, column=0, pady=5)

        self.etiqueta_password = tk.Label(self.frame1, text="Password", font=("Arial", 14, "bold"))
        self.etiqueta_password.grid(row=2, column=0, pady=(40, 10), sticky="n")

        self.input_password = tk.Entry(self.frame1, font=("Arial", 12), show="*", width=22)
        self.input_password.grid(row=3, column=0, pady=5)

        self.boton = tk.Button(self.frame1, text="Iniciar Seccion", bg="darkblue", fg="white", font=("Arial", 14, "bold"), command=self.iniciar_seccion)
        self.boton.grid(row=4, column=0, pady=(40, 10))

        self.mensaje = tk.Label(self.frame1, font=("Arial", 14, "bold"))

if __name__ == "__main__":
    app = Login()
    app.mainloop()