class Elipse:
    def __init__(self, eje_mayor=3, eje_menor=1, color="Amarillo"):
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
        self.color = color
    
    def descripcion(self):
        return f"Elipse con eje mayor {self.eje_mayor}, eje menor {self.eje_menor} y color {self.color}."