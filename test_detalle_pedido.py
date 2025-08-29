# test_detalle_pedido.py
import unittest
from detalle_pedido import DetallePedido
from producto import Producto
from categoria import Categoria

class TestDetallePedido(unittest.TestCase):
    def setUp(self):
        categoria_test = Categoria("Teclados", "Periféricos")
        producto_test = Producto("Teclado Mecánico", 120.00, categoria_test, 20)
        self.detalle = DetallePedido(producto_test, 3)

    def test_creacion_detalle(self):
        self.assertEqual(self.detalle.producto.nombre, "Teclado Mecánico")
        self.assertEqual(self.detalle.cantidad, 3)

    def test_calculo_subtotal(self):
        # 120.00 (precio) * 3 (cantidad)
        self.assertEqual(self.detalle.subtotal, 360.00)

    def test_cantidad_no_positiva(self):
        with self.assertRaises(ValueError):
            DetallePedido(self.detalle.producto, 0)
        with self.assertRaises(ValueError):
            DetallePedido(self.detalle.producto, -1)

if __name__ == "__main__":
    unittest.main(verbosity=2)