class Persona:
    def __init__(self, nombre, apellido, lugar_nacimiento, sexo):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__lugar_nacimiento = lugar_nacimiento
        self.__sexo = sexo
        self.__pareja = None
        self.__padre = None
        self.__madre = None

    # Relaciones Familiares
    def casado_con(self, pareja):
        self.__pareja = pareja
        return f"{self.__nombre} está casado/a con {pareja.__nombre}"
    
    def es_hijo_de(self, padre, madre):
        self.__padre = padre
        self.__madre = madre
        return f"{self.__nombre} es hijo/a de {padre.__nombre} y de {madre.__nombre}"

    def __str__(self):
        return f"Persona(nombre={self.__nombre}, apellido={self.__apellido}, lugar_nacimiento={self.__lugar_nacimiento}, sexo={self.__sexo})"