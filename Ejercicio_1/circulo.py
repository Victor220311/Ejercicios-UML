class Circulo:
    def __init__(self, diametro=1, color="Negro"):
        self.diametro = diametro  
        self.color = color       
    
    def descripcion(self):
        return f"Círculo de diámetro {self.diametro} y color {self.color}."