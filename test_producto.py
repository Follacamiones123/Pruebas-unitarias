# test_producto.py
import unittest
from producto import Producto
from categoria import Categoria

class TestProducto(unittest.TestCase):

    def setUp(self):
        self.categoria_test = Categoria("Portátiles", "Computadoras")
        self.producto = Producto("Laptop Pro", 1500.00, self.categoria_test, stock=10)

    def test_creacion_producto(self):
        self.assertEqual(self.producto.nombre, "Laptop Pro")
        self.assertEqual(self.producto.precio, 1500.00)
        self.assertEqual(self.producto.stock, 10)

    def test_actualizar_stock(self):
        self.producto.actualizar_stock(5)
        self.assertEqual(self.producto.stock, 15)
        self.producto.actualizar_stock(-10)
        self.assertEqual(self.producto.stock, 5)

    def test_stock_no_negativo(self):
        with self.assertRaises(ValueError):
            self.producto.actualizar_stock(-11)

if __name__ == "__main__":
    unittest.main(verbosity=2)