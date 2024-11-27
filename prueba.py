import tkinter as tk

class Alumno:
    def __init__(self,ventana):
        self.ventana=ventana
        self.ventana.title("Calculadora")
        ventana.geometry("1920x1080")
        ventana.minsize(400,200)
        ventana.maxsize(800,500)
        #Logo del programa
        #ventana.iconbitmap("")
        
        #Titulo
        etiqueta = tk.Label(ventana, text="Salud")
        etiqueta.config(font=("Arial", 14, "bold"))
        etiqueta.pack()
        
if __name__=="__main__":
    ventana=tk.Tk()
    aplicacion=Alumno(ventana)
