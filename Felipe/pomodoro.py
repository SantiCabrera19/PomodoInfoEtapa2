import tkinter as tk
from reloj import RelojPomodoro
from menu_despl import crear_lista_tareas

def main():
    ventana = tk.Tk()
    ventana.title('Pomodoro App')
    ventana.geometry('800x600')

    # Frame izquierdo con el reloj
    frame_izq = tk.Frame(ventana)
    frame_izq.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Label para mostrar tarea seleccionada arriba del reloj
    tarea_seleccionada = tk.StringVar(value="Sin tarea seleccionada")
    label_tarea = tk.Label(frame_izq, textvariable=tarea_seleccionada, font=('Arial', 16))
    label_tarea.pack()

    # Reloj Pomodoro (va debajo del label de tarea)
    reloj = RelojPomodoro(frame_izq)

    # Frame derecho con las tareas
    frame_der = tk.Frame(ventana)
    frame_der.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Lista de tareas
    lista_tareas, ingreso_tarea = crear_lista_tareas(frame_der)

    # Cuando se selecciona una tarea
    def on_tarea_seleccionada(event):
        seleccion = lista_tareas.curselection()
        if seleccion:
            tarea = lista_tareas.get(seleccion[0])
            tarea_seleccionada.set(f"Tarea: {tarea}")
            reloj.reiniciar()
            reloj.iniciar_cuenta_regresiva(25 * 60)  # 25 minutos
        else:
            tarea_seleccionada.set("Sin tarea seleccionada")
            reloj.reiniciar()

    lista_tareas.bind('<<ListboxSelect>>', on_tarea_seleccionada)

    ventana.mainloop()

if __name__ == '__main__':
    main()