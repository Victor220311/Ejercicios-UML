class Cuadro:
    def __init__(self, Titulo, AC, Tecnica, Sub_tecnica, Soporte, Autor, Estado_Conservacion):
        self.Titulo = Titulo
        self.AC = AC
        self.Tecnica = Tecnica
        self.Sub_tecnica = Sub_tecnica
        self.Soporte = Soporte
        self.Autor = Autor
        self.Estado_Conservacion = Estado_Conservacion
        self.lugar = None  # Relación con Lugar (dónde se expone)
        self.es_replica_de = None  # Relación con otro Cuadro (si es réplica)

    def establecer_lugar(self, lugar):
        self.lugar = lugar
    
    def establecer_como_replica(self, cuadro_original):
        self.es_replica_de = cuadro_original

    def descripcion(self):
        return f"'{self.Titulo}' - {self.Autor} ({self.AC}) - {self.Tecnica}/{self.Sub_tecnica} sobre {self.Soporte}"