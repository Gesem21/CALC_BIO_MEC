#hola
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
        #Cerrar
        self.boton2 = tk.Button(ventana, text="Exit", command=self.destruir)
        self.boton2.config(bg="red", fg="white", font=("Arial", 15),relief="raised", bd=10)
        self.boton2.place(relx=0, rely=0, width=80, height=60)
        
        #Boton de go
        self.boton4 = tk.Button(ventana, text="Ir!", command=self.entradas)
        self.boton4.config(bg="#51b6b6",relief="raised", bd=10,  fg="white", font=("Arial", 20))
        self.boton4.place(x=634, y=744, width=270, height=65)
        
    def entradas(self):
        #Pantalla 2
        img2_original = Image.open("personales.png")  # Carga la imagen original.
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
        self.nombre_in.config(font=("Comic Sans MS", 20), bg = "White")
        """self.nombre_in.insert(0, "Obligatorio")"""
        self.nombre_in.place(x=770,y=142,width=696, height=83)
        
        
        #Peso
        self.peso_in = tk.Entry(ventana)
        self.peso_in.config(font=("Comic Sans MS", 20), bg="white")
        self.peso_in.insert(0, "50")
        self.peso_in.place(x=770,y=326,width=696, height=83)
        
        #Edad
        self.edad_in = tk.Entry(ventana)
        self.edad_in.config(font=("Comic Sans MS", 20), bg="white")
        self.edad_in.insert(0, "12")
        self.edad_in.place(x=770,y=510,width=696, height=83)
        
        #Altura
        self.altura_in = tk.Entry(ventana)
        self.altura_in.config(font=("Comic Sans MS", 20), bg="white")
        self.altura_in.insert(0, "160")
        self.altura_in.place(x=770,y=692,width=696, height=83)
        
        
        #BOTONES
        #go
        self.boton3 = tk.Button(ventana, text="GO!!!", command=self.validacion)
        self.boton3.config(bg="#51b6b6", fg="White", font=("Arial", 25), relief="raised", bd=10)
        self.boton3.place(x=140, y=622, width=373, height=80)
    
    def validacion(self):
        """Este apartado se guardaran y enviaran los datos introducidos"""
        try:
            nombre = self.nombre_in.get()
            peso = float(self.peso_in.get())
            altura = float(self.altura_in.get())
            edad = int(self.edad_in.get())

            # Guardar en CSV
            with open("datos.csv", mode="a", newline="") as file:
                writer = csv.writer(file)
                writer.writerow([nombre, edad, peso, altura])

            messagebox.showinfo("Éxito", "Datos guardados correctamente")
        except ValueError:
            messagebox.showerror("Error", "Verifica los datos ingresados.")
        
        
        """Este apartado es para validar datos dentro del rango saludable"""
        try:
            # Validar edad
            edaddato = int(self.edad_in.get())  # Convertir el valor de edad a un entero
            if edaddato < 2 or edaddato > 14:
                messagebox.showinfo("Error", "¡Estás fuera del rango de edad!")
                return  # Salir si la edad no es válida

            # Validar peso y altura para calcular el IMC
            peso = float(self.peso_in.get())  # Obtener peso en kg
            altura = float(self.altura_in.get())  # Obtener altura en cm

            # Cálculo del IMC
            imc = peso / ((altura / 100) ** 2)

            # Verificar si el IMC está fuera del rango saludable
            if imc < 18.5 or imc > 30:
                self.mostrar_alerta_imc()  # Mostrar pantalla de alerta si el IMC es preocupante
                return  # Salir si el IMC no es saludable

            # Continuar con el flujo normal si todo es válido
            self.medicamentos()

        except ValueError:
            messagebox.showinfo("Error", "Por favor, ingresa valores válidos para peso, altura y edad.")
        
        
    def mostrar_alerta_imc(self):
        # Crear ventana de alerta
        alerta = tk.Toplevel(self.ventana)
        alerta.title("Alerta: IMC no saludable")
        alerta.geometry("960x540")

        # Mostrar imagen
        img_alerta_original = Image.open("imcinsaluble.png")
        img_alerta_resized = img_alerta_original.resize((960, 540), Image.Resampling.LANCZOS)
        img_alerta = ImageTk.PhotoImage(img_alerta_resized)

        label_img = tk.Label(alerta, image=img_alerta)
        label_img.image = img_alerta
        label_img.place(x=0, y=0)

        # Botón de salida
        boton_salir = tk.Button(alerta, text="Salir", command=self.ventana.destroy)
        boton_salir.config(bg="red", fg="white", font=("Arial", 15))
        boton_salir.place(relx=0.45,rely=0.8)

        alerta.mainloop()

    def destruir(self):
        self.ventana.destroy()
            
    def medicamentos(self):
        #fondo
        self.img3 = tk.PhotoImage(file="medicamentos.png")
        self.label3 = tk.Label(self.ventana, image=self.img3)
        self.label3.image = self.img3
        self.label3.place(x=0, y=0, relwidth=1, relheight=1)
        
        #Cerrar
        self.boton2 = tk.Button(ventana, text="Exit", command=self.destruir)
        self.boton2.config(bg="red", fg="white", font=("Arial", 15),relief="raised", bd=10)
        self.boton2.place(relx=0, rely=0, width=80, height=60)
        
        #Go
        """Paracetamol"""
        self.botonp = tk.Button(ventana, text="Recetar", command=self.paracetamol)
        self.botonp.config(bg="#51b6b6", fg="Black", font=("Arial", 20), relief="groove", bd=6)
        self.botonp.place(x=175, y=655, width=185, height=50)
        
        # Imagen cruz
        self.img_cruz = Image.open("mas_info.png")  # Aquí debes colocar la imagen que deseas mostrar
        self.img_cruz_resized = self.img_cruz.resize((40, 40), Image.Resampling.LANCZOS)  # Ajusta el tamaño según necesites
        self.img_cruz_tk = ImageTk.PhotoImage(self.img_cruz_resized)

        self.cruz_label = tk.Label(self.ventana, image=self.img_cruz_tk)
        self.cruz_label.image = self.img_cruz_tk
        self.cruz_label.place(x=350, y=250)

        # Eventos para mostrar y ocultar la imagen informativa
        self.cruz_label.bind("<Enter>", self.mostrar_imagen_paracetamol)
        self.cruz_label.bind("<Leave>", self.ocultar_imagen_paracetamol)
        
        #Imagen de informacion
        self.img_infop = Image.open("info_paracetamol.png")  # Aquí debes colocar la imagen que deseas mostrar
        self.img_infop_resized = self.img_infop.resize((500, 250), Image.Resampling.LANCZOS)  # Ajusta el tamaño según necesites
        self.img_infop_tk = ImageTk.PhotoImage(self.img_infop_resized)

        self.infop_label = tk.Label(self.ventana, image=self.img_infop_tk)
        self.infop_label.image = self.img_infop_tk
        self.infop_label.place_forget()
        
        """Ïbuprofeno"""
        self.botoni = tk.Button(ventana, text="Recetar", command=self.ibuprofeno)
        self.botoni.config(bg="#51b6b6", fg="Black", font=("Arial", 20), relief="groove", bd=6)
        self.botoni.place(x=497, y=655, width=185, height=50)
        
        # Imagen cruz
        self.img_cruz2 = Image.open("mas_info.png")  # Aquí debes colocar la imagen que deseas mostrar
        self.img_cruz2_resized = self.img_cruz2.resize((40, 40), Image.Resampling.LANCZOS)  # Ajusta el tamaño según necesites
        self.img_cruz2_tk = ImageTk.PhotoImage(self.img_cruz2_resized)

        self.cruz_label2 = tk.Label(self.ventana, image=self.img_cruz2_tk)
        self.cruz_label2.image = self.img_cruz2_tk
        self.cruz_label2.place(x=680, y=250)

        # Eventos para mostrar y ocultar la imagen informativa
        self.cruz_label2.bind("<Enter>", self.mostrar_imagen_ibuprofeno)
        self.cruz_label2.bind("<Leave>", self.ocultar_imagen_ibuprofeno)
        
        #Imagen de informacion
        self.img_infoi = Image.open("info_ibuprofeno.png")  # Aquí debes colocar la imagen que deseas mostrar
        self.img_infoi_resized = self.img_infoi.resize((500, 250), Image.Resampling.LANCZOS)  # Ajusta el tamaño según necesites
        self.img_infoi_tk = ImageTk.PhotoImage(self.img_infoi_resized)

        self.infoi_label = tk.Label(self.ventana, image=self.img_infoi_tk)
        self.infoi_label.image = self.img_infoi_tk
        self.infoi_label.place_forget()
        
        """Cetirizina"""
        self.botonc = tk.Button(ventana, text="Recetar", command=self.ceritizina)
        self.botonc.config(bg="#51b6b6", fg="Black", font=("Arial", 20), relief="groove", bd=6)
        self.botonc.place(x=835, y=655, width=185, height=50)
        
        # Imagen cruz
        self.img_cruz3 = Image.open("mas_info.png")  # Aquí debes colocar la imagen que deseas mostrar
        self.img_cruz3_resized = self.img_cruz3.resize((40, 40), Image.Resampling.LANCZOS)  # Ajusta el tamaño según necesites
        self.img_cruz3_tk = ImageTk.PhotoImage(self.img_cruz3_resized)

        self.cruz_label3 = tk.Label(self.ventana, image=self.img_cruz3_tk)
        self.cruz_label3.image = self.img_cruz3_tk
        self.cruz_label3.place(x=1000, y=250)

        # Eventos para mostrar y ocultar la imagen informativa
        self.cruz_label3.bind("<Enter>", self.mostrar_imagen_cetirizina)
        self.cruz_label3.bind("<Leave>", self.ocultar_imagen_cetirizina)
        
        #Imagen de informacion
        self.img_infoc = Image.open("info_ibuprofeno.png")  # Aquí debes colocar la imagen que deseas mostrar
        self.img_infoc_resized = self.img_infoc.resize((500, 250), Image.Resampling.LANCZOS)  # Ajusta el tamaño según necesites
        self.img_infoc_tk = ImageTk.PhotoImage(self.img_infoc_resized)

        self.infoc_label = tk.Label(self.ventana, image=self.img_infoc_tk)
        self.infoc_label.image = self.img_infoc_tk
        self.infoc_label.place_forget()
        
        """"Loratadina"""
        self.botonl = tk.Button(ventana, text="Recetar", command=self.loratadina)
        self.botonl.config(bg="#51b6b6", fg="Black", font=("Arial", 20), relief="groove", bd=6)
        self.botonl.place(x=1172, y=655, width=185, height=50)
        
        #Imagen cruz
        self.img_cruz4 = Image.open("mas_info.png")  # Aquí debes colocar la imagen que deseas mostrar
        self.img_cruz4_resized = self.img_cruz4.resize((40, 40), Image.Resampling.LANCZOS)  # Ajusta el tamaño según necesites
        self.img_cruz4_tk = ImageTk.PhotoImage(self.img_cruz4_resized)

        self.cruz_label4 = tk.Label(self.ventana, image=self.img_cruz4_tk)
        self.cruz_label4.image = self.img_cruz4_tk
        self.cruz_label4.place(x=1340, y=250)

        # Eventos para mostrar y ocultar la imagen informativa
        self.cruz_label4.bind("<Enter>", self.mostrar_imagen_loratadina)
        self.cruz_label4.bind("<Leave>", self.ocultar_imagen_loratadina)
        
        #Imagen de informacion
        self.img_infol = Image.open("info_ibuprofeno.png")  # Aquí debes colocar la imagen que deseas mostrar
        self.img_infol_resized = self.img_infol.resize((500, 250), Image.Resampling.LANCZOS)  # Ajusta el tamaño según necesites
        self.img_infol_tk = ImageTk.PhotoImage(self.img_infol_resized)

        self.infol_label = tk.Label(self.ventana, image=self.img_infol_tk)
        self.infol_label.image = self.img_infol_tk
        self.infol_label.place_forget()
        
    def paracetamol(self):
        #Cargar fondo
        fondo11_original = Image.open("dosisfondo.png")  # Carga la imagen original.
        fondo11_resized = fondo11_original.resize((1534, 862), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        fondo11 = ImageTk.PhotoImage(fondo11_resized)
        self.labe11 = tk.Label(self.ventana, image=fondo11)
        self.labe11.image=fondo11
        self.labe11.place(x=0, y=0)
        
        #Calculo de dosis
        peso_dato = int(self.peso_in.get())
        dosis = 12.5 * peso_dato
        
        #Label de dosis
        self.label_dosis1 = tk.Label(self.ventana, text=f"Tu dosis es {dosis} mg", font=("Comic Sans MS", 40), bg="white", fg="black")
        self.label_dosis1.place(relx=0.33, rely=0.5)
        
        #Cerrar
        self.boton2 = tk.Button(ventana, text="Exit", command=self.destruir)
        self.boton2.config(bg="red", fg="white", font=("Arial", 15),relief="raised", bd=10)
        self.boton2.place(relx=0, rely=0, width=80, height=60)
        
    def ibuprofeno(self):
        #Cargar fondo
        fondo11_original = Image.open("dosisfondo.png")  # Carga la imagen original.
        fondo11_resized = fondo11_original.resize((1534, 862), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        fondo11 = ImageTk.PhotoImage(fondo11_resized)
        self.labe11 = tk.Label(self.ventana, image=fondo11)
        self.labe11.image=fondo11
        self.labe11.place(x=0, y=0)
        
        #Calculo de dosis
        peso_dato = int(self.peso_in.get())
        dosis = 7.5 * peso_dato
        
        #Label de dosis
        self.label_dosis1 = tk.Label(self.ventana, text=f"Tu dosis es {dosis} mg", font=("Comic Sans MS", 40), bg="white", fg="black")
        self.label_dosis1.place(relx=0.33, rely=0.5)
        
        #Cerrar
        self.boton2 = tk.Button(ventana, text="Exit", command=self.destruir)
        self.boton2.config(bg="red", fg="white", font=("Arial", 15),relief="raised", bd=10)
        self.boton2.place(relx=0, rely=0, width=80, height=60)
    
    def ceritizina(self):
        #Cargar fondo
        fondo11_original = Image.open("dosisfondo.png")  # Carga la imagen original.
        fondo11_resized = fondo11_original.resize((1534, 862), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        fondo11 = ImageTk.PhotoImage(fondo11_resized)
        self.labe11 = tk.Label(self.ventana, image=fondo11)
        self.labe11.image=fondo11
        self.labe11.place(x=0, y=0)
        
        #Calculo de dosis
        peso_dato = int(self.peso_in.get())
        dosis = peso_dato * 0.25
        
        #Label de dosis
        self.label_dosis1 = tk.Label(self.ventana, text=f"Tu dosis es {dosis} ml", font=("Comic Sans MS", 40), bg="white", fg="black")
        self.label_dosis1.place(relx=0.33, rely=0.5)
        
        #Cerrar
        self.boton2 = tk.Button(ventana, text="Exit", command=self.destruir)
        self.boton2.config(bg="red", fg="white", font=("Arial", 15),relief="raised", bd=10)
        self.boton2.place(relx=0, rely=0, width=80, height=60)
    
    def loratadina(self):
        #Cargar fondo
        fondo11_original = Image.open("dosisfondo.png")  # Carga la imagen original.
        fondo11_resized = fondo11_original.resize((1534, 862), Image.Resampling.LANCZOS)  # Ajusta el tamaño de la imagen al botón.
        fondo11 = ImageTk.PhotoImage(fondo11_resized)
        self.labe11 = tk.Label(self.ventana, image=fondo11)
        self.labe11.image=fondo11
        self.labe11.place(x=0, y=0)
        
        #Calculo de dosis
        peso_dato = int(self.peso_in.get())
        dosis = 0.2 * peso_dato
        
        #Label de dosis
        self.label_dosis1 = tk.Label(self.ventana, text=f"Tu dosis es {dosis} ml", font=("Comic Sans MS", 40), bg="white", fg="black")
        self.label_dosis1.place(relx=0.33, rely=0.5)
        
        #Cerrar
        self.boton2 = tk.Button(ventana, text="Terminar", command=self.reinicio)
        self.boton2.config(bg="#51b6b6", fg="white", font=("Arial", 15),relief="raised", bd=10)
        self.boton2.place(relx=0.43, rely=0.8, width=200, height=70)
    
    def mostrar_imagen_paracetamol(self, event):
        self.infop_label.place(x=390, y=290)  # Muestra la imagen cuando el cursor pasa por encima
    def ocultar_imagen_paracetamol(self, event):
        self.infop_label.place_forget()
        
    def mostrar_imagen_ibuprofeno(self, event):
        self.infoi_label.place(x=720, y=290)  # Muestra la imagen cuando el cursor pasa por encima
    def ocultar_imagen_ibuprofeno(self, event):
        self.infoi_label.place_forget()
        
    def mostrar_imagen_cetirizina(self, event):
        self.infoc_label.place(x=500, y=290)  # Muestra la imagen cuando el cursor pasa por encima
    def ocultar_imagen_cetirizina(self, event):
        self.infoc_label.place_forget()
        
    def mostrar_imagen_loratadina(self, event):
        self.infol_label.place(x=840, y=290)  # Muestra la imagen cuando el cursor pasa por encima
    def ocultar_imagen_loratadina(self, event):
        self.infol_label.place_forget()
        
        
if name=="main":
    ventana=tk.Tk()
    app=Application(ventana)
    ventana.mainloop



