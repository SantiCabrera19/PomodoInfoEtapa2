import tkinter as tk
import time

# Función para crear el reloj con botones
def crear_reloj(ventana):
    # Label del reloj
    reloj = tk.Label(ventana, font=('Arial', 60), bg='blue', fg='white')
    reloj.pack(anchor='center', pady=20)

    # Estado del reloj
    estado = {'activo': False, 'after_id': None}

    # Función que actualiza la hora
    def hora():
        if estado['activo']:
            tiempo_actual = time.strftime('%H:%M:%S')
            reloj.config(text=tiempo_actual)
            estado['after_id'] = ventana.after(1000, hora)

    # Iniciar reloj
    def iniciar():
        if not estado['activo']:
            estado['activo'] = True
            hora()

    # Pausar reloj
    def pausar():
        if estado['activo']:
            estado['activo'] = False
            if estado['after_id']:
                ventana.after_cancel(estado['after_id'])
                estado['after_id'] = None

    # Resetear reloj
    def resetear():
        pausar()
        reloj.config(text='00:00:00')

    # Crear botones
    frame_botones = tk.Frame(ventana)
    frame_botones.pack(pady=10)

    btn_iniciar = tk.Button(frame_botones, text="Iniciar", font=('Arial', 12), width=10, command=iniciar)
    btn_pausar = tk.Button(frame_botones, text="Pausar", font=('Arial', 12), width=10, command=pausar)
    btn_reset = tk.Button(frame_botones, text="Resetear", font=('Arial', 12), width=10, command=resetear)

    btn_iniciar.pack(side=tk.LEFT, padx=5)
    btn_pausar.pack(side=tk.LEFT, padx=5)
    btn_reset.pack(side=tk.LEFT, padx=5)

    # Mostrar reloj en cero al inicio
    reloj.config(text='00:00:00')

    return reloj