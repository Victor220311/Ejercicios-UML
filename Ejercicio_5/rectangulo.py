class Rectangulo:
    def __init__(self, longitud, anchura, color):
        self.longitud = longitud
        self.anchura = anchura
        self.color = color

    def descripcion(self):
        return f"Rectángulo - Longitud: {self.longitud}, Anchura: {self.anchura}, Color: {self.color}"