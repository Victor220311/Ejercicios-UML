class Rectangulo:
    def __init__(self, longitud=3, anchura=1, color="Naranja"):
        self.longitud = longitud
        self.anchura = anchura
        self.color = color
    
    def descripcion(self):
        return f"Rectángulo de longitud {self.longitud}, anchura {self.anchura} y color {self.color}."