# EJERCICIO #1
from Ejercicio_1.circulo import Circulo
from Ejercicio_1.rectangulo import Rectangulo
from Ejercicio_1.cuadrado import Cuadrado
from Ejercicio_1.elipse import Elipse

mi_circulo = Circulo()
mi_rectangulo = Rectangulo()
mi_cuadrado = Cuadrado()
mi_elipse = Elipse()

print("EJERCICIO 1")
print(mi_circulo.descripcion())
print(mi_rectangulo.descripcion())
print(mi_cuadrado.descripcion())
print(mi_elipse.descripcion())

# EJERCICIO #2
from Ejercicio_2.persona import Persona

print("\nEJERCICIO 2")
p1 = Persona("Kate", "Windsor", "Middleton", "Mujer")
p2 = Persona("Guillermo", "Windsor", "Gales", "Hombre")
p3 = Persona("Diana", "Windsor", "Spencer", "Mujer")
p4 = Persona("Carlos", "Windsor", "Gales", "Hombre")

print(p2)
print(p2.casado_con(p1))
print(p2.es_hijo_de(p4, p3))