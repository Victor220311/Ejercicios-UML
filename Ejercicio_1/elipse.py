# elipse.py: Define la clase Elipse con atributos de la figura amarilla (eje mayor 3, eje menor 1, color Amarillo).
class Elipse:
    def __init__(self, eje_mayor=3, eje_menor=1, color="Amarillo"):
        self.eje_mayor = eje_mayor
        self.eje_menor = eje_menor
        self.color = color
    
    # Método para mostrar info.
    def descripcion(self):
        return f"Elipse con eje mayor {self.eje_mayor}, eje menor {self.eje_menor} y color {self.color}."