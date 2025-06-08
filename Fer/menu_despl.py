import tkinter as tk

# Función para crear la lista de tareas
def crear_lista_tareas(ventana):
    ingreso_tarea = tk.Entry(ventana) # entry es como un input de tkinter
    ingreso_tarea.pack() # packeamos el input para ponerlo en la ventana
    
    lista_tareas = tk.Listbox(ventana) # listbox es como un select de tkinter
    lista_tareas.pack() # packeamos el select para ponerlo en la ventana
    
    # Funcion para agregar una tarea
    def agregar_tarea():
        tarea = ingreso_tarea.get() # get es para obtener el valor del input
        if tarea: # si hay una tarea
            lista_tareas.insert(tk.END, tarea) # insertamos la tarea en la lista
            ingreso_tarea.delete(0, tk.END) # borramos el input
    
    def eliminar_tarea():
        seleccion = lista_tareas.curselection() # curselection es para obtener la seleccion de la lista
        if seleccion: # si hay una seleccion
            lista_tareas.delete(seleccion) # borramos la seleccion de la lista
    
    boton_agregar = tk.Button(ventana, text='Agregar tarea', command=agregar_tarea) # button es como un boton de tkinter
    boton_agregar.pack() # packeamos el boton para ponerlo en la ventana
    
    boton_eliminar = tk.Button(ventana, text='Eliminar tarea', command=eliminar_tarea) # button es como un boton de tkinter
    boton_eliminar.pack() # packeamos el boton para ponerlo en la ventana
    
    return lista_tareas, ingreso_tarea
