# test_detalle_pedido.py
import unittest
from detalle_pedido import DetallePedido
from producto import Producto
from categoria import Categoria

class TestDetallePedido(unittest.TestCase):
    def test_calculo_subtotal(self):
        cat = Categoria("Teclados", "Periféricos")
        prod = Producto("Teclado Mecánico", 120.00, cat)
        detalle = DetallePedido(prod, 3)
        self.assertEqual(detalle.subtotal, 360.00)

    def test_cantidad_positiva(self):
        cat = Categoria("Teclados", "Periféricos")
        prod = Producto("Teclado Mecánico", 120.00, cat)
        with self.assertRaises(ValueError):
            DetallePedido(prod, 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)