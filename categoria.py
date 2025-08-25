# categoria.py
class Categoria:
    def __init__(self, nombre, descripcion):
        if not nombre:
            raise ValueError("El nombre no puede estar vacío")
        self.nombre = nombre
        self.descripcion = descripcion

    def __str__(self):
        return self.nombre

    def actualizar_descripcion(self, nueva_descripcion):
        self.descripcion = nueva_descripcion
        return True