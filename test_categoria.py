# test_categoria.py
import unittest
from categoria import Categoria

class TestCategoria(unittest.TestCase):

    def setUp(self):
        self.categoria = Categoria("Electrónicos", "Artículos de tecnología y gadgets")

    def test_creacion_categoria(self):
        self.assertEqual(self.categoria.nombre, "Electrónicos")
        self.assertEqual(self.categoria.descripcion, "Artículos de tecnología y gadgets")

    def test_representacion_string(self):
        self.assertEqual(str(self.categoria), "Electrónicos")

    def test_actualizar_descripcion(self):
        self.categoria.actualizar_descripcion("Nueva descripción de electrónicos")
        self.assertEqual(self.categoria.descripcion, "Nueva descripción de electrónicos")

    def test_nombre_no_vacio(self):
        with self.assertRaises(ValueError):
            Categoria("", "Una descripción")

if __name__ == "__main__":
    unittest.main(verbosity=2)