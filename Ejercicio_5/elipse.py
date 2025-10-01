class Elipse:
    def __init__(self, color, eje_mayor, eje_menor):
        self.color = color
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor

    def descripcion(self):
        return f"Elipse - Color: {self.color}, Eje Mayor: {self.eje_mayor}, Eje Menor: {self.eje_menor}"