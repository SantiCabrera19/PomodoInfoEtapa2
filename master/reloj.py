import tkinter as tk
import time

# Función para crear el reloj
def crear_reloj(ventana):
    reloj = tk.Label(ventana, font=('Arial', 60), bg='blue', fg='white') 
    # reloj va a ser igual a un label de tkinter

    # hora va a ser igual a una funcion que va a actualizar el reloj
    def hora():
        tiempo_actual = time.strftime('%H:%M:%S')
        reloj.config(text=tiempo_actual)
        ventana.after(1000, hora)
     
    # pack es para que el reloj se muestre en la ventana
    reloj.pack(anchor='center') # pack es de tkinter y es para que el reloj se muestre en el centro de la ventana
    hora()
    return reloj
