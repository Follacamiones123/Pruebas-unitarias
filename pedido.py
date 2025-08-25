# pedido.py
from datetime import date

class Pedido:
    def __init__(self, usuario, fecha=date.today(), estado="Procesando"):
        self.usuario = usuario
        self.fecha = fecha
        self.estado = estado
        self.detalles = []

    def agregar_detalle(self, detalle):
        self.detalles.append(detalle)

    def calcular_total(self):
        return sum(detalle.subtotal for detalle in self.detalles)