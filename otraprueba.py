import tkinter as tk
from tkinter import messagebox

class Application:
    def __init__(self, ventana):
        self.ventana = ventana
        self.ventana.geometry("1280x720")
        self.ventana.title("PROGRAMACIÓN PROYECTO FINAL")
        self.ventana.resizable(0, 0)
        self.ventana.configure(bg="lightblue")
        
        imagen_fondo = tk.PhotoImage(file="portadainicio.jpg")
        
        label_imagen = tk.Label(self.ventana, image=imagen_fondo)
        label_imagen.place(x=0, y=0, relwidth=1, relheight=1) 

        label_imagen.image = imagen_fondo

        self.img = tk.PhotoImage(file="aclaracionesmed.jpg")

        self.boton1 = tk.Button(self.ventana, text="INICIAR", height=2, width=20, command=self.iniciar)
        self.boton1.place(x=570, y=380)

        self.boton2 = tk.Button(self.ventana, text="CERRAR", height=2, width=20, command=self.mensaje)
        self.boton2.place(x=570, y=460)
        
        self.lista = [0]
        self.listaestado = []
        self.genero = tk.IntVar()
    def iniciar(self):
        self.mostrar_imagen()
        self.crear_widgets()

    def mostrar_imagen(self):
        img_label = tk.Label(self.ventana, image=self.img)
        img_label.image = self.img
        img_label.place(x=0, y=0, relwidth=1, relheight=1)
        messagebox.showinfo("MENSAJE", "¡BIENVENIDO AL TRABAJO FINAL!")