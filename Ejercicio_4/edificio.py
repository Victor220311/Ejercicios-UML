class Edificio:
    def __init__(self, nombre, culto, lugar, fecha_inicio_construccion, fecha_fin_construccion,
                 fecha_primera_consagracion, fecha_inicio_segunda_etapa_construccion,
                 fecha_segunda_consagracion, fecha_declaracion_bic, material, estilo):
        self.nombre = nombre
        self.culto = culto
        self.lugar = lugar
        self.fecha_inicio_construccion = fecha_inicio_construccion
        self.fecha_fin_construccion = fecha_fin_construccion
        self.fecha_primera_consagracion = fecha_primera_consagracion
        self.fecha_inicio_segunda_etapa_construccion = fecha_inicio_segunda_etapa_construccion
        self.fecha_segunda_consagracion = fecha_segunda_consagracion
        self.fecha_declaracion_bic = fecha_declaracion_bic
        self.material = material
        self.estilo = estilo

    def descripcion(self):
        return (f"{self.nombre}\n"
                f"Culto: {self.culto}\n"
                f"Ubicación: {self.lugar}\n"
                f"Construcción: {self.fecha_inicio_construccion} - {self.fecha_fin_construccion}\n"
                f"Primera consagración: {self.fecha_primera_consagracion}\n"
                f"Segunda etapa: {self.fecha_inicio_segunda_etapa_construccion} - {self.fecha_segunda_consagracion}\n"
                f"Declaración BIC: {self.fecha_declaracion_bic}\n"
                f"Material: {self.material}\n"
                f"Estilo: {self.estilo}")