import tkinter
from tkinter import font
from PIL import Image, ImageTk

def encabezado(ventana):
    try:
        panel_encabezado = tkinter.Frame(ventana, bg="lightblue", width=1000, height=100)
        panel_encabezado.grid(row=0, column=0, columnspan=2, sticky="nsew")

        imagen = Image.open(r"C:\Users\COMPUFIRE\OneDrive\Escritorio\CODIGO\logo.jpg")
        imagen = imagen.resize((120, 120))
        logo = ImageTk.PhotoImage(imagen)

        etiqueta_logo = tkinter.Label(panel_encabezado, image=logo, bg="white", bd=2, relief="solid")
        etiqueta_logo.image = logo
        etiqueta_logo.pack(side="left", padx=20, pady=10)

        tipodeletra = font.Font(family="Arial", size=12, weight="bold")
        titulo = tkinter.Label(panel_encabezado, text="Registro", font=tipodeletra)
        titulo.pack(side="left", padx=20, pady=10)

    except Exception as e:
        print("Error en encabezado():", e)