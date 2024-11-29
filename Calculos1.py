import tkinter as tk
from tkinter import messagebox
class DosisApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculadora de Dosis")

        # Etiqueta y entrada para el peso
        tk.Label(root, text="Ingrese el peso (kg):").grid(row=0, column=0, padx=10, pady=10)
        self.peso_dato = tk.Entry(root)
        self.peso_dato.grid(row=0, column=1, padx=10, pady=10)

        # Botón para calcular dosis de paracetamol
        tk.Button(root, text="Calcular Paracetamol", command=self.calcular_paracetamol).grid(row=1, column=0, padx=10, pady=10)

        # Botón para calcular dosis de ibuprofeno
        tk.Button(root, text="Calcular Ibuprofeno", command=self.calcular_ibuprofeno).grid(row=1, column=1, padx=10, pady=10)

    def calcular_paracetamol(self):
        try:
            peso = float(self.peso_dato.get())
            dosis = 12.5 * peso  # Dosis en mg
            messagebox.showinfo("Resultado", f"Dosis de Paracetamol: {dosis:.2f} mg")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un peso válido.")

    def calcular_ibuprofeno(self):
        try:
            peso = float(self.peso_dato.get())
            dosis = 12.5 * peso  # Dosis en mg
            messagebox.showinfo("Resultado", f"Dosis de Ibuprofeno: {dosis:.2f} mg")
        except ValueError:
            messagebox.showerror("Error", "Ingrese un peso válido.")

# Crear ventana principal
if __name__ == "__main__":
    root = tk.Tk()
    app = DosisApp(root)
    root.mainloop()

