# circulo.py: Define la clase Circulo con atributos de la figura gris (diámetro 1, color Negro).
class Circulo:
    def __init__(self, diametro=1, color="Negro"):
        # __init__ es el constructor: se llama al crear un objeto, asigna valores iniciales.
        self.diametro = diametro  # Atributo: guarda el diámetro.
        self.color = color        # Atributo: guarda el color.
    
    # Opcional: método para mostrar info (útil para probar).
    def descripcion(self):
        return f"Círculo de diámetro {self.diametro} y color {self.color}."