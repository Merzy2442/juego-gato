import tkinter as tk

class Gato:
    def __init__(self, root):
        self.root = root
        self.root.title("Juego de Gato")
        self.turno = "X"
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        self.botones = [[None for _ in range(3)] for _ in range(3)]
        self.jugando = False
        self.historial = {"X": 0, "O": 0}

        self.label_turno = tk.Label(root, text="Presiona 'Iniciar Juego' para comenzar", font=("Arial", 14))
        self.label_turno.grid(row=0, column=0, columnspan=3)

        for i in range(3):
            for j in range(3):
                btn = tk.Button(root, text="", width=8, height=4, font=("Arial", 24),
                                command=lambda x=i, y=j: self.jugar(x, y), state=tk.DISABLED)
                btn.grid(row=i+1, column=j)
                self.botones[i][j] = btn

        self.btn_iniciar = tk.Button(root, text="Iniciar Juego", command=self.iniciar_juego, width=12)
        self.btn_iniciar.grid(row=4, column=0)

        self.btn_reiniciar = tk.Button(root, text="Reiniciar", command=self.reiniciar, width=12, state=tk.DISABLED)
        self.btn_reiniciar.grid(row=4, column=2)

        self.label_historial = tk.Label(root, text=self.formatear_historial(), font=("Arial", 12))
        self.label_historial.grid(row=5, column=0, columnspan=3)

    def formatear_historial(self):
        return f"Victorias - X: {self.historial['X']} | O: {self.historial['O']}"

    def actualizar_historial(self):
        self.label_historial.config(text=self.formatear_historial())

    def iniciar_juego(self):
        self.jugando = True
        self.turno = "X"
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botones[i][j].config(text="", state=tk.NORMAL)
        self.label_turno.config(text="Turno de X")
        self.btn_iniciar.config(state=tk.DISABLED)
        self.btn_reiniciar.config(state=tk.NORMAL)

    def jugar(self, x, y):
        if not self.jugando or self.tablero[x][y] != "":
            return
        self.tablero[x][y] = self.turno
        self.botones[x][y].config(text=self.turno, state=tk.DISABLED)
        if self.verificar_ganador(self.turno):
            self.label_turno.config(text=f"Gana {self.turno}")
            self.historial[self.turno] += 1
            self.actualizar_historial()
            self.finalizar_juego()
        elif self.empate():
            self.label_turno.config(text="Empate")
            self.finalizar_juego()
        else:
            self.turno = "O" if self.turno == "X" else "X"
            self.label_turno.config(text=f"Turno de {self.turno}")

    def verificar_ganador(self, jugador):
        for i in range(3):
            if all(self.tablero[i][j] == jugador for j in range(3)) or all(self.tablero[j][i] == jugador for j in range(3)):
                return True
        if all(self.tablero[i][i] == jugador for i in range(3)) or all(self.tablero[i][2-i] == jugador for i in range(3)):
            return True
        return False

    def empate(self):
        return all(self.tablero[i][j] != "" for i in range(3) for j in range(3))

    def finalizar_juego(self):
        self.jugando = False
        for i in range(3):
            for j in range(3):
                self.botones[i][j].config(state=tk.DISABLED)
        self.btn_iniciar.config(state=tk.NORMAL)
        self.btn_reiniciar.config(state=tk.NORMAL)

    def reiniciar(self):
        self.jugando = False
        self.tablero = [["" for _ in range(3)] for _ in range(3)]
        for i in range(3):
            for j in range(3):
                self.botones[i][j].config(text="", state=tk.DISABLED)
        self.label_turno.config(text="Presiona 'Iniciar Juego' para comenzar")
        self.btn_iniciar.config(state=tk.NORMAL)
        self.btn_reiniciar.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = Gato(root)
    root.mainloop()
