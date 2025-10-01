class Lugar:
    def __init__(self, nombre, ciudad, pais):
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais

    def descripcion(self):
        return f"{self.nombre}, {self.ciudad}, {self.pais}"