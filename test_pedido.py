# test_pedido.py
import unittest
from pedido import Pedido
from usuario import Usuario

class TestPedido(unittest.TestCase):
    def test_creacion_pedido(self):
        usuario_test = Usuario("Ana", "Gomez", "ana@email.com", "pw")
        pedido = Pedido(usuario_test)
        self.assertEqual(pedido.usuario.nombre_completo(), "Ana Gomez")
        self.assertEqual(pedido.estado, "Procesando")
        self.assertEqual(len(pedido.detalles), 0)

if __name__ == "__main__":
    unittest.main(verbosity=2)