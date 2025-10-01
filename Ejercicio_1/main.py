#Getter: obtienen el valor de un atributo. Ejemplo:
#get_diametro() para obtener el valor de self.diametro

#Setter: modifican el valor de un atributo. Ejemplo:
#set_diametro(nuevo.valor) para cambiar self.diametro

#Comportamiento: metodos que definen acciones del objeto
#ejemplo: girar(), frenar(), cambiar_color()

# main.py: Crea objetos de cada clase y los imprime para verificar.
# Ejecuta con: python main.py en la terminal de Codespaces.
from paquete import Circulo, Rectangulo, Cuadrado, Elipse  # Asume que tu carpeta se llama 'paquete'; ajusta si no.

# Instancia objetos con valores de la imagen.
mi_circulo = Circulo()
mi_rectangulo = Rectangulo()
mi_cuadrado = Cuadrado()
mi_elipse = Elipse()

# Prueba: imprime descripciones.
print(mi_circulo.descripcion())
print(mi_rectangulo.descripcion())
print(mi_cuadrado.descripcion())
print(mi_elipse.descripcion())