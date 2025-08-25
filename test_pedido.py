# test_pedido.py
import unittest
from datetime import date
from pedido import Pedido
from usuario import Usuario # Asegúrate de tener tu clase Usuario

class TestPedido(unittest.TestCase):

    def setUp(self):
        usuario_test = Usuario("Ana", "Gomez")
        self.pedido = Pedido(usuario_test)

    def test_creacion_pedido(self):
        self.assertEqual(self.pedido.usuario.nombre_completo(), "Ana Gomez")
        self.assertEqual(self.pedido.fecha, date.today())
        self.assertEqual(self.pedido.estado, "Procesando")
        self.assertEqual(self.pedido.total, 0.0)

    def test_actualizar_estado(self):
        self.pedido.actualizar_estado("Enviado")
        self.assertEqual(self.pedido.estado, "Enviado")

    def test_actualizar_estado_invalido(self):
        with self.assertRaises(ValueError):
            self.pedido.actualizar_estado("Perdido")

if __name__ == "__main__":
    unittest.main(verbosity=2)