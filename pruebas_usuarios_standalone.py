import unittest

# Clase Usuario independiente (sin Django)
class Usuario:
    def __init__(self, email, first_name, last_name, password=None):
        self.email = email
        self.first_name = first_name
        self.last_name = last_name
        self.password = password
    
    def nombre_completo(self):
        return f"{self.first_name} {self.last_name}"
    
    def __str__(self):
        return self.email
    
    def check_password(self, password):
        return self.password == password

class TestUsuario(unittest.TestCase):
    
    def setUp(self):
        # Se ejecuta antes de cada prueba, útil para preparar objetos
        self.usuario_data = {
            'email': 'test@example.com',
            'first_name': 'Juan',
            'last_name': 'Perez',
            'password': 'testpassword123'
        }
        self.usuario = Usuario(**self.usuario_data)
    
    def test_crear_usuario(self):
        # Método de prueba para creación de usuario
        self.assertEqual(self.usuario.email, 'test@example.com')
        self.assertEqual(self.usuario.first_name, 'Juan')
        self.assertEqual(self.usuario.last_name, 'Perez')
        self.assertTrue(self.usuario.check_password('testpassword123'))
    
    def test_representacion_string(self):
        # Método de prueba para __str__
        self.assertEqual(str(self.usuario), 'test@example.com')
    
    def test_nombre_completo(self):
        # Método de prueba para nombre completo
        nombre_completo = self.usuario.nombre_completo()
        self.assertEqual(nombre_completo, 'Juan Perez')

if __name__ == "__main__":
    print("🧪 EJECUTANDO PRUEBAS DE USUARIO")
    print("=" * 50)
    unittest.main(verbosity=2)
