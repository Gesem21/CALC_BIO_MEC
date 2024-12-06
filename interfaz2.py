import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import time
import csv

class Application:
        def init(self,ventana):
        ventana.attributes("-fullscreen", True)
        self.ventana=ventana
        self.ventana.title("Calculadora")
        ventana.geometry("1920x1080")
        #Logo del programa
        #ventana.iconbitmap("")
        #Fondo
        #LLAMADO DE IMAGENES
        #Pantalla 1
        img0_original = Image.open("home.png")  # Carga la imagen original.
        img0_resized = img0_original.resize((1534, 862), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img0 = ImageTk.PhotoImage(img0_resized)
        
        #Pantalla 3
        
        #self.welcome = tk.PhotoImage(file="bienvenido.png") #Bienvenida pantalla 2
        
        #LABEL
        
        self.label0 = tk.Label(self.ventana, image=img0)
        self.label0.image=img0
        self.label0.place(x=0, y=0)
        
        #iniciar
        self.boton = tk.Button(ventana, text="INICIAR", command=self.anuncio)
        self.boton.config(bg="#51b6b6", fg="white", font=("Arial", 20), relief="raised", bd=10)
        self.boton.place(x=217, y=659, width=291, height=65)
        
        #cerrar
        self.boton2 = tk.Button(ventana, text="Exit", command=self.destruir)
        self.boton2.config(bg="red", fg="white", font=("Arial", 15),relief="raised", bd=10)
        self.boton2.place(relx=0, rely=0, width=80, height=60)
    
    def destruir(self): #Destruye la ventana
        self.ventana.destroy()
        
    def reinicio(self):
        self.ventana.destroy()
        ventana_principal = tk.Tk()
        Application(ventana_principal)
        ventana_principal.mainloop()
        
    def anuncio(self):
        img00_original = Image.open("advertencia.png")  # Carga la imagen original.
        img00_resized = img00_original.resize((1534, 862), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img00 = ImageTk.PhotoImage(img00_resized)
        self.label00 = tk.Label(self.ventana, image=img00)
        self.label00.image=img00
        self.label00.place(x=0, y=0)
        self.label00.image = img00
        
        #Cerrar
        self.boton2 = tk.Button(ventana, text="Exit", command=self.destruir)
        self.boton2.config(bg="red", fg="white", font=("Arial", 15),relief="raised", bd=10)
        self.boton2.place(relx=0, rely=0, width=80, height=60)
        
        #Skip
        self.boton4 = tk.Button(ventana, text="Skip", command=self.service)
        self.boton4.config(bg="#51b6b6", fg="white", font=("Arial", 15),relief="raised", bd=10)
        self.boton4.place(x=634, y=710, width=270, height=65)       
    
    def service(self):
        #Pantalla de servicios
        img69_original = Image.open("services.png")  # Carga la imagen original.
        img69_resized = img69_original.resize((1534, 862), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img69 = ImageTk.PhotoImage(img69_resized)
        self.label69 = tk.Label(self.ventana, image=img69)
        self.label69.image=img69
        self.label69.place(x=0, y=0)


