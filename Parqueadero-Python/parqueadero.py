
import tkinter as tk
from tkinter import messagebox, simpledialog
from datetime import datetime

class Parqueadero:
    def __init__(self):
        self.mapa = [
    ['ENT', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-','|','-', '-','-'],
    ['|', 'D', 'D', 'D', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P','|','E','E', '|'],
    ['|', 'D', 'D', 'D', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P','|','E','E', '|'],
    ['|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-','|', '-', '-','|'],
    ['|', 'P', 'P', 'P', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P','|','P','P', '|'],
    ['|', 'P', 'P', 'P', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P','|','P','P', '|'],
    ['|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-','|', '-', '-','|'],
    ['|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-','|', '-', '-','|'],
    ['|', 'P', 'P', 'P', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P','|','P','P', '|'],
    ['|', 'P', 'P', 'P', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P', '|', 'P', 'P', 'P','|','P','P', '|'],
    ['|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-', '|', '-', '-', '-','|', '-', '-','|'],
    ['|', 'M', 'M', 'M', '|', 'M', 'M', 'M', '|', 'M', 'M', 'M', '|', 'M', 'M', 'M','|','M', 'M', '|'],
    ['|', 'M', 'M', 'M', '|', 'M', 'M', 'M', '|', 'M', 'M', 'M', '|', 'M', 'M', 'M','|','M', 'M', '|'],
    ['-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-', '-','-', '-', '-','SAL'],
]
        self.vehiculos = {}  # Placa: (fila, col, tipo, hora_entrada)
        self.tarifas = {"carro": 1500, "moto": 1000, "discapacitado": 500, "electrico": 700}

    def cargar_estado(self):
        pass  # No implementado para esta versión

    def registrar_entrada(self, placa, tipo):
        for i, fila in enumerate(self.mapa):
            for j, celda in enumerate(fila):
                if (tipo == "carro" and celda == 'P') or (tipo == "moto" and celda == 'M') or (tipo == "discapacitado" and celda == 'D') or (tipo == "electrico" and celda == 'E'):
                    self.mapa[i][j] = 'O'
                    self.vehiculos[placa] = (i, j, tipo, datetime.now())
                    return True
        messagebox.showwarning("Error", f"No hay espacio disponible para tipo: {tipo}")
        return False

    def registrar_salida(self, placa):
        if placa not in self.vehiculos:
            messagebox.showwarning("Error", f"No se encontró vehículo con placa {placa}")
            return False
        i, j, tipo, entrada = self.vehiculos.pop(placa)
        self.mapa[i][j] = 'P' if tipo == "carro" else 'M' if tipo == "moto" else 'D' if tipo == "discapacitado" else 'E'
        tiempo = (datetime.now() - entrada).seconds // 60
        costo = max(1, tiempo) * self.tarifas.get(tipo, 1000)
        messagebox.showinfo("Pago", f"Tiempo: {tiempo} minutos\nTotal a pagar: ${costo}")
        return True

    def obtener_disponibilidad(self):
        disponibles = {"carro": 0, "moto": 0, "discapacitado": 0, "electrico": 0}
        for fila in self.mapa:
            for celda in fila:
                if celda == 'P':
                    disponibles["carro"] += 1
                elif celda == 'M':
                    disponibles["moto"] += 1
                elif celda == 'D':
                    disponibles["discapacitado"] += 1
                elif celda == 'E':
                    disponibles["electrico"] += 1
        return disponibles

    def buscar_vehiculo(self, placa):
        if placa in self.vehiculos:
            i, j, tipo, hora = self.vehiculos[placa]
            return f"Placa {placa} tipo {tipo} está en posición ({i},{j}) desde {hora.strftime('%H:%M:%S')}"
        return f"No se encontró vehículo con placa {placa}"

    def reporte_diario(self):
        return f"Total vehículos hoy: {len(self.vehiculos)}"

class Parking(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Sistema de Parqueadero")
        self.geometry("950x700")
        self.parqueadero = Parqueadero()

        self.crear_widgets()
        self.dibujar_mapa()

    def crear_widgets(self):
        frame_botones = tk.Frame(self)
        frame_botones.pack(pady=10)

        botones = [
            ("Registrar Entrada", self.registrar_entrada),
            ("Registrar Salida", self.registrar_salida),
            ("Mostrar Disponibilidad", self.mostrar_disponibilidad),
            ("Buscar Vehículo", self.buscar_vehiculo),
            ("Reporte Diario", self.reporte_diario),
        ]

        for i, (texto, comando) in enumerate(botones):
            btn = tk.Button(frame_botones, text=texto, command=comando)
            btn.grid(row=0, column=i, padx=5)

        self.canvas = tk.Canvas(self, bg="white", width=900, height=550)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.clic_en_mapa)

    def dibujar_mapa(self):
        self.canvas.delete("all")
        size = 40
        self.celdas = {}

        for i, fila in enumerate(self.parqueadero.mapa):
            for j, celda in enumerate(fila):
                x0 = j * size
                y0 = i * size
                x1 = x0 + size
                y1 = y0 + size

                color = {
                    ' ': 'white', '-': 'gray', '|': 'gray', 'P': 'lightgreen',
                    'O': 'red', 'D': 'blue', 'E': 'orange', 'SAL': 'purple', 
                    'ENT': 'yellow'
                }.get(celda, 'white')

                rect = self.canvas.create_rectangle(x0, y0, x1, y1, fill=color, outline='black')
                self.canvas.create_text((x0 + x1) // 2, (y0 + y1) // 2, text=celda, font=('Arial', 10))
                self.celdas[rect] = (i, j)

    def registrar_entrada(self):
        placa = simpledialog.askstring("Entrada", "Placa del vehículo:")
        if not placa:
            return
        tipo = simpledialog.askstring("Tipo de vehículo", "Tipo (carro, moto, discapacitado, electrico):", initialvalue="carro")
        if tipo and self.parqueadero.registrar_entrada(placa, tipo.lower()):
            self.dibujar_mapa()

    def registrar_salida(self):
        placa = simpledialog.askstring("Salida", "Placa del vehículo:")
        if not placa:
            return
        if self.parqueadero.registrar_salida(placa):
            self.dibujar_mapa()

    def mostrar_disponibilidad(self):
        info = self.parqueadero.obtener_disponibilidad()
        mensaje = "\n".join([f"{k}: {v}" for k, v in info.items()])
        messagebox.showinfo("Disponibilidad", mensaje)
        self.dibujar_mapa()

    def buscar_vehiculo(self):
        placa = simpledialog.askstring("Buscar", "Placa del vehículo:")
        if not placa:
            return
        encontrado = self.parqueadero.buscar_vehiculo(placa)
        messagebox.showinfo("Resultado de búsqueda", encontrado)

    def reporte_diario(self):
        reporte = self.parqueadero.reporte_diario()
        messagebox.showinfo("Reporte Diario", reporte)

    def clic_en_mapa(self, evento):
        for rect, (i, j) in self.celdas.items():
            coords = self.canvas.coords(rect)
            if coords[0] <= evento.x <= coords[2] and coords[1] <= evento.y <= coords[3]:
                celda = self.parqueadero.mapa[i][j]
                messagebox.showinfo("Información", f"Celda: ({i},{j})\nContenido: {celda}")
                break

if __name__ == "__main__":
    app = Parking()
    app.mainloop()
