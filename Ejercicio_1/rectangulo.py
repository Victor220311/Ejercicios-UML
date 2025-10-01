# rectangulo.py: Define la clase Rectangulo con atributos de la figura naranja (longitud 3, anchura 1, color Naranja).
class Rectangulo:
    def __init__(self, longitud=3, anchura=1, color="Naranja"):
        # Constructor: asigna valores por defecto basados en la imagen.
        self.longitud = longitud
        self.anchura = anchura
        self.color = color
    
    # Método para mostrar info.
    def descripcion(self):
        return f"Rectángulo de longitud {self.longitud}, anchura {self.anchura} y color {self.color}."