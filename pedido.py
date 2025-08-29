# pedido.py
from datetime import date

class Pedido:
    def __init__(self, usuario, fecha=date.today(), estado="Procesando"):
        self.usuario = usuario
        self.fecha = fecha
        self.estado = estado
        self.detalles = []
        self.total = 0.0

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)

    def actualizar_estado(self, nuevo_estado):
        estados_validos = ["Procesando", "Enviado", "Entregado", "Cancelado"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado no válido")

    def calcular_total(self):
        self.total = sum(detalle.subtotal for detalle in self.detalles)
        return self.total
