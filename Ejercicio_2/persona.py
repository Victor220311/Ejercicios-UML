# persona.py: Define la clase Persona con atributos básicos del diagrama.
class Persona:
    def __init__(self, nombre, apellido, sexo):
        # Constructor: asigna los atributos basados en los valores del diagrama.
        self.nombre = nombre
        self.apellido = apellido
        self.sexo = sexo
    
    def descripcion(self):
        # Método para mostrar la información de la persona.
        return f"{self.nombre} {self.apellido}, Sexo: {self.sexo}"