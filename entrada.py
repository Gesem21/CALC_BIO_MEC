import tkinter as tk
from tkinter import portada

def abrir_aclaraciones():
    ventana_inicio.destroy()  # Cierra la ventana inicial

    # Crear ventana de aclaraciones
    ventana_aclaraciones = tk.Tk()
    ventana_aclaraciones.title("Aclaraciones")
    ventana_aclaraciones.geometry("600x400")

    # Fondo con imagen
    fondo_aclaraciones = portada(file="fondo_aclaraciones.png")  # Cambia el nombre si usas otra imagen
    fondo_label = tk.Label(ventana_aclaraciones, image=fondo_aclaraciones)
    fondo_label.place(relwidth=1, relheight=1)

    # Texto de aclaraciones
    texto_aclaraciones = tk.Label(
        ventana_aclaraciones,
        text="Aquí van las aclaraciones importantes para los usuarios.",
        bg="white",
        fg="black",
        font=("Arial", 12),
        wraplength=500,
    )
    texto_aclaraciones.place(relx=0.5, rely=0.4, anchor="center")

    # Botón de continuar
    boton_continuar = tk.Button(
        ventana_aclaraciones,
        text="Continuar",
        command=ventana_aclaraciones.destroy,  # Cierra la ventana
        font=("Arial", 14),
        bg="#4CAF50",
        fg="white",
    )
    boton_continuar.place(relx=0.5, rely=0.7, anchor="center")

    ventana_aclaraciones.mainloop()


# Crear ventana inicial
ventana_inicio = tk.Tk()
ventana_inicio.title("Inicio")
ventana_inicio.geometry("600x400")

# Fondo con imagen
fondo_inicio = portada(file="fondo_inicio.png")  # Cambia el nombre si usas otra imagen
fondo_label = tk.Label(ventana_inicio, image=fondo_inicio)
fondo_label.place(relwidth=1, relheight=1)

# Botón de iniciar
boton_iniciar = tk.Button(
    ventana_inicio,
    text="Iniciar",
    command=abrir_aclaraciones,  # Llama a la función que abre la segunda ventana
    font=("Arial", 14),
    bg="#4CAF50",
    fg="white",
)
boton_iniciar.place(relx=0.5, rely=0.7, anchor="center")

ventana_inicio.mainloop()

