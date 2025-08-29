# detalle_pedido.py
class DetallePedido:
    def __init__(self, producto, cantidad):
        if cantidad <= 0:
            raise ValueError("La cantidad debe ser positiva")
        self.producto = producto
        self.cantidad = cantidad


    def __str__(self):
        return f"{self.cantidad} x {self.producto.nombre}"
>>>>>>> 657b5456f15faee7f40f73cfa361a8b525282106
