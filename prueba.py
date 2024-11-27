import tkinter as tk

class Application:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Calculadora")
        ventana.geometry("1080x720")
        #Logo del programa
        #ventana.iconbitmap("")
        
        #Fondo
        #LLAMADO DE IMAGENES
        fondo = tk.PhotoImage(file="fondo10.png")
        self.img = tk.PhotoImage(file="fondo20.png") #Fondo pantalla 2
        self.img3 = tk.PhotoImage(file="fondo30.png")
        #self.welcome = tk.PhotoImage(file="bienvenido.png") #Bienvenida pantalla 2
        
        #LABEL
        label1 = tk.Label(self.ventana, image=fondo)
        label1.place(x=0, y=0, relwidth=1, relheight=1)
        label1.image = fondo
        
        
        
        """#Titulo
        etiqueta = tk.Label(ventana, text="Salud")
        etiqueta.config(font=("Arial", 40, "bold"))
        etiqueta.pack()"""
        
        #BOTONES
        #iniciar
        
        self.boton = tk.Button(ventana, text="INICIAR", command=self.entradas)
        self.boton.config(bg="skyblue3", fg="white", font=("Arial", 20))
        self.boton.place(x=378, y=420, width=300, height=70)
        #cerrar
        self.boton2 = tk.Button(ventana, text="X", command=self.destruir)
        self.boton2.config(bg="gray25", fg="white", font=("Arial", 25))
        self.boton2.place(relx=0.95, rely=0.899, width=80, height=80)
    
    def destruir(self): #Destruye la ventana
        self.ventana.destroy()
    
    def entradas(self):
        fondo2_label = tk.Label(self.ventana, image=self.img)
        fondo2_label.image = self.img
        fondo2_label.place(x=0, y=0, relwidth=1, relheight=1)
        """welcome_label = tk.Label(self.ventana, image=self.welcome)
        welcome_label.image = self.welcome
        welcome_label.place(x=0, y=0, width=1, height=1)"""
        
        """etiqueta = tk.Label(ventana, text="DOSIS")
        etiqueta.config(font=("Arial", 40, "bold"), bg="steel blue")
        etiqueta.place(relx=0.42, y=10)"""
        
        #ENTRADAS
        #Nombre
        nombre_in = tk.Entry(ventana, text="Nombre")
        nombre_in.place(relx=0.25,y=350,width=180, height=40,anchor='c')
        peso_in = tk.Entry(ventana)
        peso_in.place(relx=0.25,y=500,width=180, height=40,anchor='c')
        edad_in = tk.Entry(ventana)
        edad_in.place(relx=0.25,y=650,width=180, height=40,anchor='c')
        
        #BOTONES
        #go
        self.boton3 = tk.Button(ventana, text="GO!", command=self.medicamentos)
        self.boton3.config(bg="gray75", fg="Black", font=("Arial", 20))
        self.boton3.place(relx=0.47, rely=0.85, width=80, height=80)
        #volver
        self.boton4 = tk.Button(ventana, text="Volver!", command=self.destruir)
        self.boton4.config(bg="lavender", fg="white", font=("Arial", 20))
        self.boton4.place(relx=0.85, rely=0.85, width=150, height=80)
        
    def medicamentos(self):
        #fondo
        label3 = tk.Label(self.ventana, image=self.img3)
        label3.image = self.img
        label3.place(x=0, y=0, relwidth=1, relheight=1)
        
        #go
        self.boton3 = tk.Button(ventana, text="GO!", command=self.medicamentos)
        self.boton3.config(bg="gray75", fg="Black", font=("Arial", 20))
        self.boton3.place(relx=0.47, rely=0.85, width=80, height=80)
        
        #volver
        self.boton4 = tk.Button(ventana, text="Volver!", command=self.destruir)
        self.boton4.config(bg="lavender", fg="white", font=("Arial", 20))
        self.boton4.place(relx=0.85, rely=0.85, width=150, height=80)
        
    def reinicio(self):
        self.ventana.destroy()
        ventana_principal = tk.Tk()
        Application(ventana_principal)
        ventana_principal.mainloop()
        
        
        
if __name__=="__main__":
    ventana=tk.Tk()
    app=Application(ventana)
    ventana.mainloop

