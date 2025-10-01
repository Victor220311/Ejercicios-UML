# institucion.py: Define la clase Institucion con atributos del diagrama.
class Lugar:
    def __init__(self, nombre, ciudad, pais):
        self.nombre = nombre
        self.ciudad = ciudad
        self.pais = pais

    def descripcion(self):
        # Método para mostrar la información del lugar.
        return f"{self.nombre}, {self.ciudad}, {self.pais}"