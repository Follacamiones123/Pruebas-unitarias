import unittest

# Clase Usuario simplificada para pruebas (sin Django)
class Usuario:
    def __init__(self, email, first_name, last_name):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
    
    def nombre_completo(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.email

class TestUsuario(unittest.TestCase):
    
    def setUp(self):
        # Se ejecuta antes de cada prueba, útil para preparar objetos
        self.usuario = Usuario("juan.perez@email.com", "Juan", "Perez")
    
    def test_nombre_completo(self):
        # Método de prueba para nombre_completo
        self.assertEqual(self.usuario.nombre_completo(), "Juan Perez")
    
    def test_email_usuario(self):
        # Método de prueba para verificar email
        self.assertEqual(self.usuario.email, "juan.perez@email.com")
    
    def test_string_representation(self):
        # Método de prueba para __str__
        self.assertEqual(str(self.usuario), "juan.perez@email.com")

if __name__ == "__main__":
    unittest.main()