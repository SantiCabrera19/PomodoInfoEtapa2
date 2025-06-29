import tkinter as tk

class RelojPomodoro(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack()

        self.tiempo_restante = 0
        self.timer_id = None
        self.activo = False

        self.label = tk.Label(self, font=('Arial', 60), bg='blue', fg='white')
        self.label.pack(pady=20)
        self.label.config(text="00:00:00")

        # Frame para botones
        botones_frame = tk.Frame(self)
        botones_frame.pack()

        btn_iniciar = tk.Button(botones_frame, text="Iniciar", width=10, command=self.iniciar)
        btn_pausar = tk.Button(botones_frame, text="Pausar", width=10, command=self.pausar)
        btn_reiniciar = tk.Button(botones_frame, text="Reiniciar", width=10, command=self.reiniciar)

        btn_iniciar.pack(side=tk.LEFT, padx=5)
        btn_pausar.pack(side=tk.LEFT, padx=5)
        btn_reiniciar.pack(side=tk.LEFT, padx=5)

    def iniciar_cuenta_regresiva(self, segundos):
        self.tiempo_restante = segundos
        self.activo = True
        self._actualizar()

    def _actualizar(self):
        if self.activo and self.tiempo_restante > 0:
            minutos = self.tiempo_restante // 60
            segundos = self.tiempo_restante % 60
            self.label.config(text=f"{minutos:02d}:{segundos:02d}")
            self.tiempo_restante -= 1
            self.timer_id = self.after(1000, self._actualizar)
        elif self.tiempo_restante == 0:
            self.label.config(text="¡Tiempo terminado!")
            self.activo = False
            self.timer_id = None

    def iniciar(self):
        if not self.activo and self.tiempo_restante > 0:
            self.activo = True
            self._actualizar()

    def pausar(self):
        if self.activo:
            self.activo = False
            if self.timer_id:
                self.after_cancel(self.timer_id)
                self.timer_id = None

    def reiniciar(self):
        self.pausar()
        self.tiempo_restante = 0
        self.label.config(text="00:00:00")