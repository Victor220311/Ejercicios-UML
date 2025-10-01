class Cuadrado:
    def __init__(self, longitud, color):
        self.longitud = longitud
        self.color = color
    
    def descripcion(self):
        return f"Cuadrado de longitud {self.longitud} y color {self.color}."