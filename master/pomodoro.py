import tkinter as tk
from reloj import crear_reloj
from menu_despl import crear_lista_tareas
from barra_despl import crear_lista_desplazable

def main():
    ventana = tk.Tk()
    ventana.title('Pomodoro App')
    ventana.geometry('800x600')
    
    # Frame izquierdo para el reloj
    frame_izquierdo = tk.Frame(ventana)
    frame_izquierdo.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    reloj = crear_reloj(frame_izquierdo)
    
    # Frame derecho para las listas
    frame_derecho = tk.Frame(ventana)
    frame_derecho.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)
    
    # Lista de tareas
    lista_tareas, ingreso_tarea = crear_lista_tareas(frame_derecho)
    
    # Lista desplazable
    lista_desplazable = crear_lista_desplazable(frame_derecho)
    
    ventana.mainloop()

if __name__ == '__main__':
    main()
