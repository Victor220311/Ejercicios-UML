# cuadrado.py: Define la clase Cuadrado con atributos de la figura azul (lado 1.5, color Azul).
# Usamos 'lado' en lugar de longitud/anchura, ya que es cuadrado.
class Cuadrado:
    def __init__(self, lado=1.5, color="Azul"):
        self.lado = lado
        self.color = color
    
    # Método para mostrar info.
    def descripcion(self):
        return f"Cuadrado de lado {self.lado} y color {self.color}."