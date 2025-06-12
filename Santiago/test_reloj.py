import tkinter as tk
from reloj import crear_reloj

def main():
    # Crear ventana principal
    ventana = tk.Tk()
    ventana.title('Prueba Temporizador Pomodoro - Santiago')
    ventana.geometry('400x500')
    ventana.config(bg='#1e1e1e')
    
    # Crear el reloj/temporizador
    reloj = crear_reloj(ventana)
    
    # Iniciar la aplicación
    ventana.mainloop()

if __name__ == '__main__':
    main() 