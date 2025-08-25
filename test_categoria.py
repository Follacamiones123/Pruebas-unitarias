# test_categoria.py
import unittest
from categoria import Categoria

class TestCategoria(unittest.TestCase):

    def test_creacion_categoria(self):
        categoria = Categoria("Electrónicos", "Artículos de tecnología")
        self.assertEqual(categoria.nombre, "Electrónicos")
        self.assertEqual(categoria.descripcion, "Artículos de tecnología")

    def test_nombre_no_vacio(self):
        with self.assertRaises(ValueError):
            Categoria("", "Una descripción")

if __name__ == "__main__":
    unittest.main(verbosity=2)