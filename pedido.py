# pedido.py
from datetime import date

class Pedido:
    def __init__(self, usuario, fecha=date.today(), estado="Procesando"):
        self.usuario = usuario
        self.fecha = fecha
        self.estado = estado
        self.total = 0.0

    def actualizar_estado(self, nuevo_estado):
        estados_validos = ["Procesando", "Enviado", "Entregado", "Cancelado"]
        if nuevo_estado in estados_validos:
            self.estado = nuevo_estado
        else:
            raise ValueError("Estado no válido")

    def calcular_total(self, detalles_pedido):
        self.total = sum(item.subtotal for item in detalles_pedido)
        return self.total