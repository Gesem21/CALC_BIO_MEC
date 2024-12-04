import tkinter as tk
from tkinter import ttk, messagebox
from PIL import Image, ImageTk
import time

class Application:
    def __init__(self,ventana):
        ventana.attributes("-fullscreen", True)
        self.ventana=ventana
        self.ventana.title("Calculadora")
        ventana.geometry("1920x1080")
        #Logo del programa
        #ventana.iconbitmap("")
        #Fondo
        #LLAMADO DE IMAGENES
        #Pantalla 1
        img0_original = Image.open("fondo10.png")  # Carga la imagen original.
        img0_resized = img0_original.resize((1534, 862), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img0 = ImageTk.PhotoImage(img0_resized)
        
        
        
        #Pantalla 3
        self.img3 = tk.PhotoImage(file="fondo30.png")
        #self.welcome = tk.PhotoImage(file="bienvenido.png") #Bienvenida pantalla 2
        
        #LABEL
        
        self.label0 = tk.Label(self.ventana, image=img0)
        self.label0.image=img0
        self.label0.place(x=0, y=0)
        
        #BOTONES
        #iniciar
        
        self.boton = tk.Button(ventana, text="INICIAR", command=self.anuncio)
        self.boton.config(bg="#92c8fe", fg="white", font=("Arial", 20), relief="raised", bd=10)
        self.boton.place(x=619, y=442, width=300, height=70)
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
        img00_original = Image.open("aclaracionesmed.png")  # Carga la imagen original.
        img00_resized = img00_original.resize((1534, 862), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img00 = ImageTk.PhotoImage(img00_resized)
        self.label00 = tk.Label(self.ventana, image=img00)
        self.label00.image=img00
        self.label00.place(x=0, y=0)
        self.label00.image = img00
        
        #Skip
        self.boton4 = tk.Button(ventana, text="Skip", command=self.entradas)
        self.boton4.config(bg="lavender", fg="white", font=("Arial", 20))
        self.boton4.place(relx=0.45, rely=0.8, width=150, height=80)       
        
    def entradas(self):
        #Pantalla 2
        img2_original = Image.open("entradas.png")  # Carga la imagen original.
        img2_resized = img2_original.resize((1534, 862), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img2 = ImageTk.PhotoImage(img2_resized)
        self.label2 = tk.Label(self.ventana, image=img2)
        self.label2.image=img2
        self.label2.place(x=0, y=0)
        
        #Cerrar
        self.boton2 = tk.Button(ventana, text="Exit", command=self.destruir)
        self.boton2.config(bg="red", fg="white", font=("Arial", 15),relief="raised", bd=10)
        self.boton2.place(relx=0, rely=0, width=80, height=60)
        
        #ENTRADAS
        #Nombre    
        self.nombre_in = tk.Entry(ventana)
        self.nombre_in.config(font=("Comic Sans MS", 20), bg = "#c7f2e7")
        self.nombre_in.insert(0, "Obligatorio")
        self.nombre_in.place(relx=0.25,y=400,width=200, height=50)
        
        
        #Peso
        self.peso_in = tk.Entry(ventana)
        self.peso_in.config(font=("Comic Sans MS", 20), bg="#c7f2e7")
        self.peso_in.insert(0, "[Kg]")
        self.peso_in.place(relx=0.25,y=500,width=150, height=50)
        
        #Edad
        self.edad_in = tk.Entry(ventana)
        self.edad_in.config(font=("Comic Sans MS", 20), bg="#c7f2e7")
        self.edad_in.insert(0, "[#]")
        self.edad_in.place(relx=0.25,y=650,width=150, height=50)
        
        
        #BOTONES
        #go
        self.boton3 = tk.Button(ventana, text="GO!!!", command=self.validar_edad)
        self.boton3.config(bg="brown2", fg="White", font=("Arial", 25), relief="groove", bd=10)
        self.boton3.place(relx=0.47, rely=0.85, width=150, height=80)
        
        #volver
        self.boton4 = tk.Button(ventana, text="Volver!", command=self.destruir)
        self.boton4.config(bg="lavender", fg="white", font=("Arial", 20))
        self.boton4.place(relx=0.85, rely=0.85, width=150, height=80)
    
    def validar_edad(self):
        #Restirccion de edad
        try:
            edaddato = int(self.edad_in.get())  # Convertir el valor de edad a un entero
            if edaddato < 2 or edaddato > 14:
                messagebox.showinfo("Error", "¡Estás fuera del rango de edad!")
            else:
                self.medicamentos()
        except ValueError:
            messagebox.showinfo("Error", "Por favor, ingresa una edad válida.")
        
        
    def medicamentos(self):
        #fondo
        label3 = tk.Label(self.ventana, image=self.img3)
        label3.image = self.img3
        label3.place(x=0, y=0, relwidth=1, relheight=1)
        
        #Cerrar
        self.boton2 = tk.Button(ventana, text="Exit", command=self.destruir)
        self.boton2.config(bg="red", fg="white", font=("Arial", 15),relief="raised", bd=10)
        self.boton2.place(relx=0, rely=0, width=80, height=60)
        
        #MEDICAMENTOS
        #Paracetamol
        img10_original = Image.open("paracetamol.png")  # Carga la imagen original.
        img10_resized = img10_original.resize((250, 100), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img10 = ImageTk.PhotoImage(img10_resized)
        
        self.boton4 = tk.Button(ventana, image=img10)
        self.boton4.image=img10
        self.boton4.config(bd=0, bg="#92c8fe")
        self.boton4.place(x=270, y=350, width=250, height=100)
        
        # Imagen informativa
        self.img_info = Image.open("paracetamol_info.png")  # Aquí debes colocar la imagen que deseas mostrar
        self.img_info_resized = self.img_info.resize((300, 150), Image.Resampling.LANCZOS)  # Ajusta el tamaño según necesites
        self.img_info_tk = ImageTk.PhotoImage(self.img_info_resized)

        self.info_label = tk.Label(self.ventana, image=self.img_info_tk)
        self.info_label.image = self.img_info_tk  # Mantén una referencia de la imagen
        self.info_label.place(x=270, y=460)  # Coloca la imagen debajo del botón Paracetamol
        self.info_label.place_forget()  # Inicialmente oculta la imagen

        # Eventos para mostrar y ocultar la imagen informativa
        self.boton4.bind("<Enter>", self.mostrar_imagen_paracetamol)
        self.boton4.bind("<Leave>", self.ocultar_imagen_paracetamol)
        
        #Ibuprofeno
        img11_original = Image.open("ibuprofeno.png")  # Carga la imagen original.
        img11_resized = img11_original.resize((250, 100), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img11 = ImageTk.PhotoImage(img11_resized)
        
        self.boton5 = tk.Button(ventana, image=img11)
        self.boton5.image=img11
        self.boton5.config(bd=0, bg="#92c8fe")
        self.boton5.place(x=270, y=602, width=250, height=100)
        
        #Antialergicos
        img12_original = Image.open("antialergico.png")  # Carga la imagen original.
        img12_resized = img12_original.resize((250, 100), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img12 = ImageTk.PhotoImage(img12_resized)
        
        self.boton6 = tk.Button(ventana, image=img12)
        self.boton6.image=img12
        self.boton6.config(bd=0, bg="#92c8fe")
        self.boton6.place(x=1015, y=350, width=250, height=100)
        
        #Setericina
        img13_original = Image.open("cetirizina.png")  # Carga la imagen original.
        img13_resized = img13_original.resize((250, 100), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        img13 = ImageTk.PhotoImage(img13_resized)
        
        self.boton7 = tk.Button(ventana, image=img13)
        self.boton7.config(bd=0, bg="#92c8fe")
        self.boton7.image=img13
        self.boton7.place(x=1015, y=602, width=250, height=100)
        
        #Go
        self.boton3 = tk.Button(ventana, text="GO!", command=self.medicamentos)
        self.boton3.config(bg="brown2", fg="Black", font=("Arial", 20), relief="groove", bd=10)
        self.boton3.place(relx=0.47, rely=0.85, width=150, height=80)
        
        #volver
        self.boton4 = tk.Button(ventana, text="Volver!", command=self.destruir)
        self.boton4.config(bg="lavender", fg="white", font=("Arial", 20))
        self.boton4.place(relx=0.85, rely=0.85, width=150, height=80)
    
    def paracetamol(self):
        peso_dato = int(self.peso_in.get())
        dosis = 12.5 * peso_dato
        print(dosis)
        
    def ibuprofeno(self):
        peso_dato = int(self.peso_in.get())
        dosis = 7.5 * peso_dato
        
    def mostrar_imagen_paracetamol(self, event):
        self.info_label.place(x=270, y=460)  # Muestra la imagen cuando el cursor pasa por encima

    def ocultar_imagen_paracetamol(self, event):
        self.info_label.place_forget()
        
        
        
if __name__=="__main__":
    ventana=tk.Tk()
    app=Application(ventana)
    ventana.mainloop


