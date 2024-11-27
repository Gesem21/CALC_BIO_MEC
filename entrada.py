import tkinter as tk
from tkinter import PhotoImage

def show_next_image():
    # Oculta la ventana de portada
    portada_window.withdraw()

    # Crea una nueva ventana para la imagen de aclaraciones
    aclaraciones_window = tk.Toplevel()
    aclaraciones_window.title("Aclaraciones")

    aclaraciones_img = PhotoImage(file="aclaracionesmed.png")
    aclaraciones_label = tk.Label(aclaraciones_window, image=aclaraciones_img)
    aclaraciones_label.image = aclaraciones_img  # Necesario para mantener la referencia
    aclaraciones_label.pack()

    continue_button = tk.Button(aclaraciones_window, text="CONTINUAR", command=aclaraciones_window.destroy)
    continue_button.pack()

# Ventana principal para la portada
portada_window = tk.Tk()
portada_window.title("Portada")

portada_img = PhotoImage(file="portadainicio.png")
portada_label = tk.Label(portada_window, image=portada_img)
portada_label.pack()

start_button = tk.Button(portada_window, text="INICIAR", command=show_next_image)
start_button.pack()

portada_window.mainloop()

