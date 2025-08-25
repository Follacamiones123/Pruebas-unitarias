# detalle_pedido.py
class DetallePedido:
    def __init__(self, producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.producto = producto
        self.cantidad = cantidad
        self.subtotal = producto.precio * cantidad