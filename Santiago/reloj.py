import tkinter as tk
import time

class PomodoroTimer(tk.Frame):
    """
    Temporizador Pomodoro completo con controles y modos
    """
    def __init__(self, parent, minutos_iniciales=10, on_finish=None):
        super().__init__(parent)
        # Variables privadas
        self._tiempo_restante = minutos_iniciales * 60
        self._corriendo = False
        self._modo = 'trabajo'
        self._min_trabajo = 10
        self._min_descanso = 5
        self._on_finish = on_finish
        
        # Configurar estilo
        self.config(bg='#2b2b2b', bd=2, relief="ridge", padx=10, pady=10)
        
        # Crear widgets
        self._crear_widgets()
        self._configurar_layout()

    def _crear_widgets(self):
        """Crea todos los widgets del temporizador"""
        # Display principal del tiempo
        self.label_tiempo = tk.Label(
            self, 
            font=('Arial', 48, 'bold'), 
            bg='#3c4043', 
            fg='white',
            pady=15,
            padx=20,
            bd=2,
            relief="raised"
        )
        
        # Frame para botones de control
        self.frame_controles = tk.Frame(self, bg='#2b2b2b')
        
        # Botones de control principales
        self.btn_play = tk.Button(
            self.frame_controles, text="▶", font=('Arial', 14), 
            bg='#4a90e2', fg='white', width=3, command=self.iniciar
        )
        self.btn_pause = tk.Button(
            self.frame_controles, text="⏸", font=('Arial', 14),
            bg='#f39c12', fg='white', width=3, command=self.pausar
        )
        self.btn_reset = tk.Button(
            self.frame_controles, text="⟳", font=('Arial', 14),
            bg='#e74c3c', fg='white', width=3, command=self.resetear
        )
        self.btn_5min = tk.Button(
            self.frame_controles, text="+5 min", font=('Arial', 10),
            bg='#27ae60', fg='white', width=6, command=lambda: self.agregar_tiempo(5)
        )
        self.btn_10min = tk.Button(
            self.frame_controles, text="+10 min", font=('Arial', 10),
            bg='#27ae60', fg='white', width=6, command=lambda: self.agregar_tiempo(10)
        )
        
        # Frame para botones de modo
        self.frame_modos = tk.Frame(self, bg='#2b2b2b')
        
        self.btn_trabajo = tk.Button(
            self.frame_modos, text="Trabajo", font=('Arial', 12),
            bg='#2980b9', fg='white', width=10, command=self.set_trabajo
        )
        self.btn_descanso = tk.Button(
            self.frame_modos, text="Descanso", font=('Arial', 12),
            bg='#8e44ad', fg='white', width=10, command=self.set_descanso
        )
        
        # Frame para configuración
        self.frame_config = tk.Frame(self, bg='#2b2b2b')
        
        self.btn_mas_trabajo = tk.Button(
            self.frame_config, text="+1 trabajo", font=('Arial', 9),
            bg='#34495e', fg='white', width=10, command=lambda: self.configurar_trabajo(1)
        )
        self.btn_menos_trabajo = tk.Button(
            self.frame_config, text="-1 trabajo", font=('Arial', 9),
            bg='#34495e', fg='white', width=10, command=lambda: self.configurar_trabajo(-1)
        )
        self.btn_mas_descanso = tk.Button(
            self.frame_config, text="+1 desc", font=('Arial', 9),
            bg='#34495e', fg='white', width=8, command=lambda: self.configurar_descanso(1)
        )
        self.btn_menos_descanso = tk.Button(
            self.frame_config, text="-1 desc", font=('Arial', 9),
            bg='#34495e', fg='white', width=8, command=lambda: self.configurar_descanso(-1)
        )
        
        # Label de estado
        self.label_estado = tk.Label(
            self, text=self.get_texto_estado(),
            bg='#2b2b2b', fg='#bdc3c7', font=('Arial', 10)
        )

    def _configurar_layout(self):
        """Configura el layout de todos los widgets"""
        # Display principal
        self.label_tiempo.pack(pady=(0, 15))
        
        # Frame de controles
        self.frame_controles.pack(pady=5)
        self.btn_play.pack(side=tk.LEFT, padx=5)
        self.btn_pause.pack(side=tk.LEFT, padx=5)
        self.btn_reset.pack(side=tk.LEFT, padx=5)
        self.btn_5min.pack(side=tk.LEFT, padx=5)
        self.btn_10min.pack(side=tk.LEFT, padx=5)
        
        # Frame de modos
        self.frame_modos.pack(pady=10)
        self.btn_trabajo.pack(side=tk.LEFT, padx=10)
        self.btn_descanso.pack(side=tk.LEFT, padx=10)
        
        # Frame de configuración
        self.frame_config.pack(pady=5)
        self.btn_mas_trabajo.pack(side=tk.LEFT, padx=5)
        self.btn_menos_trabajo.pack(side=tk.LEFT, padx=5)
        self.btn_mas_descanso.pack(side=tk.LEFT, padx=5)
        self.btn_menos_descanso.pack(side=tk.LEFT, padx=5)
        
        # Label de estado
        self.label_estado.pack(pady=(10, 0))
        
        # Actualizar display inicial
        self.actualizar_display()

    def actualizar_display(self):
        """Actualiza el display del tiempo"""
        minutos = self._tiempo_restante // 60
        segundos = self._tiempo_restante % 60
        self.label_tiempo.config(text=f"{minutos:02}:{segundos:02}")

    def actualizar_estado(self):
        """Actualiza el texto de estado"""
        self.label_estado.config(text=self.get_texto_estado())

    def get_texto_estado(self):
        """Genera el texto de estado actual"""
        return f"Modo: {self._modo.capitalize()} | Trabajo: {self._min_trabajo} min | Descanso: {self._min_descanso} min"

    def tick(self):
        """Función que se ejecuta cada segundo"""
        if self._corriendo and self._tiempo_restante > 0:
            self._tiempo_restante -= 1
            self.actualizar_display()
            self.after(1000, self.tick)
        elif self._tiempo_restante == 0:
            self._corriendo = False
            self.label_tiempo.config(text="¡Tiempo!")
            if self._on_finish:
                self._on_finish()

    def iniciar(self):
        """Inicia el temporizador"""
        if not self._corriendo and self._tiempo_restante > 0:
            self._corriendo = True
            self.tick()

    def pausar(self):
        """Pausa el temporizador"""
        self._corriendo = False

    def resetear(self):
        """Resetea el temporizador al tiempo del modo actual"""
        if self._modo == 'trabajo':
            self._tiempo_restante = self._min_trabajo * 60
        else:
            self._tiempo_restante = self._min_descanso * 60
        self.actualizar_display()
        self._corriendo = False

    def agregar_tiempo(self, minutos):
        """Agrega minutos al tiempo restante"""
        self._tiempo_restante += minutos * 60
        self.actualizar_display()

    def set_trabajo(self):
        """Cambia al modo trabajo"""
        self._modo = 'trabajo'
        self._tiempo_restante = self._min_trabajo * 60
        self.actualizar_display()
        self.actualizar_estado()
        self._corriendo = False

    def set_descanso(self):
        """Cambia al modo descanso"""
        self._modo = 'descanso'
        self._tiempo_restante = self._min_descanso * 60
        self.actualizar_display()
        self.actualizar_estado()
        self._corriendo = False

    def configurar_trabajo(self, delta):
        """Ajusta el tiempo de trabajo"""
        self._min_trabajo = max(1, self._min_trabajo + delta)
        if self._modo == 'trabajo':
            self._tiempo_restante = self._min_trabajo * 60
            self.actualizar_display()
        self.actualizar_estado()

    def configurar_descanso(self, delta):
        """Ajusta el tiempo de descanso"""
        self._min_descanso = max(1, self._min_descanso + delta)
        if self._modo == 'descanso':
            self._tiempo_restante = self._min_descanso * 60
            self.actualizar_display()
        self.actualizar_estado()


def crear_reloj(ventana):
    """
    Función para crear el temporizador Pomodoro
    Mantiene la interfaz original pero devuelve el nuevo temporizador
    """
    pomodoro = PomodoroTimer(ventana, minutos_iniciales=10)
    pomodoro.pack(anchor='center', expand=True, fill='both', padx=20, pady=20)
    return pomodoro
