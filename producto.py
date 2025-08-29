# producto.py
class Producto:
    def __init__(self, nombre, precio, categoria, stock=0):
        if precio < 0 or stock < 0:
            raise ValueError("Precio y stock no pueden ser negativos")
        self.nombre = nombre
        self.precio = precio
        self.categoria = categoria
        self.stock = stock

    def obtener_info(self):
        return f"{self.nombre} (${self.precio:.2f}) - Stock: {self.stock}"

    def actualizar_stock(self, cantidad):
        if self.stock + cantidad < 0:
            raise ValueError("El stock no puede ser negativo")
        self.stock += cantidad
        self.stock += cantidad