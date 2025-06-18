import tkinter
from Vistas.Vista_De_Datos import actualicion
from Vistas.Entradas import entrada_general

print(">> tablas_formulas.py se está ejecutando")

def a(ventana):
    tablas = tkinter.Frame(ventana, bg="white", width=400, height=600)
    tablas.grid(row=1, column=0, sticky="nsew")

    formulario = tkinter.Frame(ventana, bg="white", width=600, height=600)
    formulario.grid(row=1, column=1, sticky="nsew")

    entrada_general(formulario, tablas, actualicion)
    actualicion("SELECT * FROM general", tablas)