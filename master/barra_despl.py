import tkinter as tk

# Función para crear la lista de desplazamiento
def crear_lista_desplazable(ventana): 
    marco = tk.Frame(ventana) # frame es como un contenedor de tkinter
    marco.pack(padx=10, pady=10) # pack es para que el contenedor se muestre en la ventana
    
    scrollbar = tk.Scrollbar(marco) # scrollbar es como una barra de desplazamiento de tkinter
    scrollbar.pack(side=tk.RIGHT, fill=tk.Y)
    
    lista = tk.Listbox(marco, yscrollcommand=scrollbar.set) # listbox es como un select de tkinter
    for i in range(100): # for es para que se agreguen 100 elementos a la lista
        lista.insert(tk.END, f'Elemento {i+1}') # insert es para agregar un elemento a la lista
    lista.pack(side=tk.LEFT, fill=tk.BOTH) # pack es para que el select se muestre en la ventana
    
    scrollbar.config(command=lista.yview)
    return lista
