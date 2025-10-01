class Cuadrado:
    def __init__(self, lado=1.5, color="Azul"):
        self.lado = lado
        self.color = color
    
    def descripcion(self):
        return f"Cuadrado de lado {self.lado} y color {self.color}."