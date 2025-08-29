<<<<<<< HEAD
# test_usuario.py
import unittest
from usuario import Usuario

class TestUsuario(unittest.TestCase):

    def setUp(self):
        # Se ejecuta antes de cada prueba para preparar el objeto
        self.usuario = Usuario("Juan", "Perez", "juan.perez@email.com", "testpassword123")

    def test_creacion_usuario(self):
        self.assertEqual(self.usuario.first_name, "Juan")
        self.assertEqual(self.usuario.last_name, "Perez")
        self.assertEqual(self.usuario.email, "juan.perez@email.com")

    def test_nombre_completo(self):
        self.assertEqual(self.usuario.nombre_completo(), "Juan Perez")

    def test_string_representation(self):
        self.assertEqual(str(self.usuario), "juan.perez@email.com")

    def test_check_password(self):
        self.assertTrue(self.usuario.check_password("testpassword123"))
        self.assertFalse(self.usuario.check_password("wrongpassword"))

    def test_creacion_usuario_invalido(self):
        # Comprueba que se lanza un error si faltan datos
        with self.assertRaises(ValueError):
            Usuario("", "Perez", "test@email.com", "pw123")
        with self.assertRaises(ValueError):
            Usuario("Juan", "", "test@email.com", "pw123")
        with self.assertRaises(ValueError):
            Usuario("Juan", "Perez", "", "pw123")

if __name__ == "__main__":
    unittest.main(verbosity=2)
=======
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
>>>>>>> 657b5456f15faee7f40f73cfa361a8b525282106
