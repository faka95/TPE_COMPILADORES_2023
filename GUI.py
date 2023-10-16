import tkinter as tk
from tkinter import filedialog

from main import main_function


def seleccionar_archivo_y_ejecutar():
    filepath = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    if filepath:
        main_function(filepath)
        print(f"Archivo seleccionado: {filepath}")
        app.destroy()

app = tk.Tk()
app.geometry("600x400")
app.title("Ejecutar main.py")

btn = tk.Button(app, text="Seleccionar archivo .txt y ejecutar", command=seleccionar_archivo_y_ejecutar)
btn.pack(pady=20)

app.mainloop()