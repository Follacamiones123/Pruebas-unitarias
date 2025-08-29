<<<<<<< HEAD
# usuario.py
class Usuario:
    def __init__(self, first_name, last_name, email, password):
        if not first_name or not last_name or not email:
            raise ValueError("El nombre, apellido y email no pueden estar vacíos")
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.__password = password  # Atributo privado

    def nombre_completo(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.email

    def check_password(self, password):
        return self.__password == password
=======
class Usuario:
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido
    
    def nombre_completo(self):
        return f"{self.nombre} {self.apellido}"
>>>>>>> 657b5456f15faee7f40f73cfa361a8b525282106
