import tkinter as tk
from tkinter import scrolledtext
from tkinter import ttk

class FormularioRegistro(tk.Tk):
    def __init__(self):
        super().__init__()  
        self.title("Formulario de Registro")
        self.config(bg="blue")
        self.crear_widgets()

    def crear_widgets(self):
        self.frame_titulo = tk.Frame(self, bg="dark blue", width=100, height=40)
        self.frame_titulo.pack(fill="x")

        
        self.titulo = tk.Label(self.frame_titulo, text="Registrate", font=("Arial", 20, "bold"), bg="dark blue", fg="white")
        self.titulo.pack()
        
        self.frame = tk.Frame(self, bg="dark blue", width=900, height=900)
        self.frame.pack(pady=30)
        self.frame.pack_propagate(False)
        
        self.nombre_label = tk.Label(self.frame, text="Nombre:", font=("Arial", 12, "bold"), bg="dark blue", fg="white")
        self.nombre_label.pack(pady=(10, 0))
        
        self.nombre_entrada = tk.Entry(self.frame, font=("Arial", 12))
        self.nombre_entrada.pack(pady=(0,5))
        
        self.apellido_label = tk.Label(self.frame, text="Apellido:", font=("Arial", 12, "bold"), bg="dark blue", fg="white")
        self.apellido_label.pack(pady=(5,0))
        
        self.apellido_entrada = tk.Entry(self.frame, font=("Arial", 12))
        self.apellido_entrada.pack(pady=(0,5))
        
        self.edad_label = tk.Label(self.frame, text="Edad:", font=("Arial", 12, "bold"), bg="dark blue", fg="white")
        self.edad_label.pack(pady=(5,0))
        
        self.edad_entrada = tk.Entry(self.frame, font=("Arial", 12))
        self.edad_entrada.pack(pady=(0,5))
        
        self.sexo_label = tk.Label(self.frame, text="Sexo:", font=("Arial", 12, "bold"), bg="dark blue", fg="white")
        self.sexo_label.pack(pady=(10,5))
        
        self.sexo_var = tk.IntVar()

        self.masculino = tk.Radiobutton(self.frame, text="Masculino", bg="dark blue", fg="white", selectcolor="black", variable=self.sexo_var, value=1)
        self.masculino.pack()

        self.femenino = tk.Radiobutton(self.frame, text="Femenino", bg="dark blue", fg="white", selectcolor="black", variable=self.sexo_var, value=2)
        self.femenino.pack()
        
        self.nacionalidad = ["Argentino","Brasileño","Canadiense","Chileno", "Cubano", "Dominicano","Español", "Estadounidense", "Frances", "Haitiano", "italiano","Japones", "jamaiquino", "Mexicano","Peruano","Puertorriqueño", "Portugues"]
        
        self.nacionalidad_label = tk.Label(self.frame, text="Elija su Nacionalidad:", font=("Arial", 12, "bold"), bg="dark blue", fg="white")
        self.nacionalidad_label.pack(pady=(5,0))
        
        self.selecionar = ttk.Combobox(self.frame, values=self.nacionalidad)
        self.selecionar.pack(pady=5)
        
        self.listbox = tk.Listbox(self.frame, selectmode="multiple", font=("Arial", 12), bg="royal blue", fg="white", selectbackground="sky blue", selectforeground="black", width=40, height=5)
        self.listbox.pack(pady=5)
        
        self.hobits = ["Descansar", "Jugar Videojuegos", "Estudiar", "Escuchar Musica", "Jugar Baloncesto", "Jugar Pelota", "jugar Futbol", "Jugar Voleyball", "jugar Ajedrez", "Armar un Rompezabeza", "Cocinar", "Derrocar el Imperio de Nicolas Maduro", "Leer", "Ver televison", "Navegar en redes Sociales", "Ver una Pelicula o Serie"]
        
        for c in self.hobits:
            self.listbox.insert(tk.END, c)
            
            
        self.btn = tk.Button(self.frame, text="registrarse", font=("Arial", 12, "bold"), bg="royal blue",fg="white", command=self.registrar)
        self.btn.pack()
        
        self.frame_msj = tk.Frame(self.frame, bg="royal blue", width=400, height=150)
        self.frame_msj.pack(pady=10)
        self.frame_msj.pack_propagate(False)
        
        self.mensaje = scrolledtext.ScrolledText(self.frame_msj, font=("Arial", 12))
        

        
    def selecionar_genero(self):
        if self.sexo_var.get() == 1:
            self.genero = "Masculino"
        else:
            self.genero = "Femenino" 
        
    def registrar(self):
        self.selecionar_genero()
        seleccion = [self.listbox.get(i) for i in self.listbox.curselection()]
    
        self.mensaje.delete("1.0", "end")
    
        self.mensaje.insert("end", f"Te acabas de registrar.\n"
            f"Tus datos son:\n\n"          
            f"Nombre: {self.nombre_entrada.get()},\n"
            f"Apellido: {self.apellido_entrada.get()},\n"
            f"Edad: {self.edad_entrada.get()} años,\n"
            f"Sexo: {self.genero},\n"
            f"Nacionalidad: {self.selecionar.get()},\n"
            f"Hobits: {', '.join(seleccion)} )"
        )
        self.mensaje.config(bg="royal blue", fg="white")
        self.mensaje.place(x=0, y=0.5, width=490, height=140)

        

if __name__ == "__main__":
    app = FormularioRegistro()
    app.mainloop()
