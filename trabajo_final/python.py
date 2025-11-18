import tkinter as tk

class ventana(tk.Tk):
    def __init__(self):
        super().__init__()
        self.geometry("500x600")
        self.title("PROYECTO 7")
        self.crear_widget()
 
    def iniciar_seccion(self):
        registro = {"admin" : "contraseña"}
        usuario = self.usuario_entrada.get()   
        contraseña = self.contraseña_entrada.get()
        
        if usuario in registro and registro[usuario] == contraseña:
            print("hola prueba") 
        else:
            print("no esta")

    
    def crear_widget(self):
        frame = tk.Frame(self, width=400, height=600, bg="gray")
        frame.pack(pady=100)
        frame.pack_propagate(False)
        
        etiqueta_usuario = tk.Label(frame, text="Usuario", font=("Arial", 14, "bold"), bg="gray")
        etiqueta_usuario.pack(pady=(40,5))
        
        usuario_entrada = tk.Entry(frame, font=("Arial", 12), borderwidth=1,relief="solid", highlightthickness=2, highlightcolor="blue")    
        usuario_entrada.pack(pady=(10))

        etiqueta_contraseña = tk.Label(frame, text="Contraseña", font=("Arial", 14, "bold"), bg="gray")
        etiqueta_contraseña.pack(pady=(5,10))
        
        contraseña_entrada = tk.Entry(frame, font=("Arial", 14), show="*",borderwidth=1, relief="solid", highlightthickness=2, highlightcolor="blue")    
        contraseña_entrada.pack(pady=(5, 10))
        
        btn = tk.Button(frame, text="Iniciar Seccion", font=("Arial", 14, "bold"), bg="gray", command=self.iniciar_seccion)
        btn.pack(pady=5)
 
        

        
        

if __name__ == "__main__":
    app = ventana()
    app.mainloop()
    