import unittest
import os
import sys

script_dir = os.path.dirname(os.path.abspath(__file__))
sys.path.insert(0, script_dir)

from usuario import Usuario

class TestUsuario(unittest.TestCase):
    
    def setUp(self):
        # Se ejecuta antes de cada prueba, útil para preparar objetos
        self.usuario = Usuario("Juan", "Perez")
    
    def test_nombre_completo(self):
        # Método de prueba para nombre_completo
        self.assertEqual(self.usuario.nombre_completo(), "Juan Perez")
    
    def test_nombre_inicial(self):
        # Método de prueba ejemplo para otro atributo o método
        self.assertEqual(self.usuario.nombre[0], "J")

if __name__ == "__main__":
    unittest.main()
