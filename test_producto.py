# test_producto.py
import unittest
from producto import Producto
from categoria import Categoria

class TestProducto(unittest.TestCase):

    def setUp(self):
        categoria_test = Categoria("Portátiles", "Computadoras portátiles")
        self.producto = Producto("Laptop Pro", 1500.00, categoria_test, stock=10)

    def test_creacion_producto(self):
        self.assertEqual(self.producto.nombre, "Laptop Pro")
        self.assertEqual(self.producto.precio, 1500.00)
        self.assertEqual(self.producto.stock, 10)
        self.assertEqual(str(self.producto.categoria), "Portátiles")

    def test_obtener_info(self):
        info_esperada = "Laptop Pro ($1500.00) - Stock: 10"
        self.assertEqual(self.producto.obtener_info(), info_esperada)

    def test_actualizar_stock(self):
        self.producto.actualizar_stock(5)
        self.assertEqual(self.producto.stock, 15)
        self.producto.actualizar_stock(-3)
        self.assertEqual(self.producto.stock, 12)

    def test_valores_negativos(self):
        with self.assertRaises(ValueError):
            Producto("Invalido", -100, self.producto.categoria)
        with self.assertRaises(ValueError):
            Producto("Invalido", 100, self.producto.categoria, stock=-5)

if __name__ == "__main__":
    unittest.main(verbosity=2)