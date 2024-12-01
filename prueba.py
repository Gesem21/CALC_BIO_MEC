import tkinter as tk
from tkinter import ttk
from PIL import Image, ImageTk

class Application:
    def _init_(self,ventana):
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
        self.nombre_label=tk.Label(ventana, text="Nombre")
        self.nombre_label.config(font=("Courier New", 20), fg="gray75")
        self.nombre_label.place(relx=0.195, y=290)
        
        self.nombre_in = tk.Entry(ventana)
        self.nombre_in.config(font=("Arial", 15))
        self.nombre_in.place(relx=0.25,y=350,width=200, height=40,anchor='c')
        
        #Peso
        self.peso_label=tk.Label(ventana, text="Peso [Kg]")
        self.peso_label.config(font=("Courier New", 20), fg="gray75")
        self.peso_label.place(relx=0.195, y=440)
        
        self.peso_in = tk.Entry(ventana)
        self.peso_in.config(font=("Arial", 15))
        self.peso_in.place(relx=0.25,y=500,width=180, height=40,anchor='c')
        
        #edad
        self.edad_label=tk.Label(ventana, text="Edad")
        self.edad_label.config(font=("Courier New", 20), fg="gray75")
        self.edad_label.place(relx=0.195, y=590)
        
        self.edad_in = tk.Entry(ventana)
        self.edad_in.config(font=("Arial", 15))
        self.edad_in.place(relx=0.25,y=650,width=180, height=40,anchor='c')
        
        
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
        #OBTENER DATOS
        peso_dato= self.peso_in.get()
        edad_dato= self.edad_in.get()
        nombre_dato = self.nombre_in.get()
        
        #fondo
        label3 = tk.Label(self.ventana, image=self.img3)
        label3.image = self.img
        label3.place(x=0, y=0, relwidth=1, relheight=1)
        print(peso_dato)
        
        #MEDICAMENTOS
        #Paracetamol
        img10_original = Image.open("paracetamol.png")  # Carga la imagen original.
        img10_resized = img10_original.resize((200, 80), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img10 = ImageTk.PhotoImage(img10_resized)
        
        self.boton4 = tk.Button(ventana, image=img10)
        self.boton4.image=img10
        self.boton4.config(relief="raised", bd=5)
        self.boton4.place(relx=0.15, rely=0.35, width=200, height=80)
        
        #Ibuprofeno
        img11_original = Image.open("ibuprofeno.png")  # Carga la imagen original.
        img11_resized = img11_original.resize((200, 80), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img11 = ImageTk.PhotoImage(img11_resized)
        
        self.boton5 = tk.Button(ventana, image=img11)
        self.boton5.image=img11
        self.boton5.config(relief="raised", bd=5)
        self.boton5.place(relx=0.15, rely=0.6, width=200, height=90)
        
        #Antialergicos
        img12_original = Image.open("antialergico.png")  # Carga la imagen original.
        img12_resized = img12_original.resize((200, 80), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img12 = ImageTk.PhotoImage(img12_resized)
        
        self.boton6 = tk.Button(ventana, image=img12)
        self.boton6.image=img12
        self.boton6.config(relief="raised", bd=5)
        self.boton6.place(relx=0.65, rely=0.35, width=200, height=80)
        
        #Setericina
        img13_original = Image.open("cetirizina.png")  # Carga la imagen original.
        img13_resized = img13_original.resize((200, 80), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img13 = ImageTk.PhotoImage(img13_resized)
        
        self.boton7 = tk.Button(ventana, image=img13)
        self.boton7.config(relief="raised",bd=5)
        self.boton7.image=img13
        self.boton7.place(relx=0.65, rely=0.6, width=200, height=80)
        
        #Sefixima
        img14_original = Image.open("cefixima.png")  # Carga la imagen original.
        img14_resized = img14_original.resize((200, 80), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img14 = ImageTk.PhotoImage(img14_resized)
        
        self.boton8 = tk.Button(ventana, image=img14)
        self.boton8.config(relief="raised", bd=5)
        self.boton8.image=img14
        self.boton8.place(relx=0.4, rely=0.48, width=200, height=80)
        
        #Go
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
        
    """def ceritizina(self):
        pesodato= self.peso_dato.get()
        if pesodato > 30:
            dosis="10 mg / dia"
            #print("10 mg/dia")
        elif pesodato < 30: 
            #print("15 mg/dia")
            dosis = "15 mg / dia"
        dosislabel = tk.Label(ventana, text=dosis)
        self.dosislabel.config(relx = 0.5, rely = 0.5)"""

        
        
        
if _name=="main_":
    ventana=tk.Tk()
    app=Application(ventana)
    ventana.mainloop


