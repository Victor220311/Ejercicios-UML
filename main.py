# ============================================================================
# EJERCICIO 1: FIGURAS GEOMÉTRICAS
# ============================================================================
from Ejercicio_1.circulo import Circulo
from Ejercicio_1.rectangulo import Rectangulo
from Ejercicio_1.cuadrado import Cuadrado
from Ejercicio_1.elipse import Elipse

print("="*70)
print("EJERCICIO 1: FIGURAS GEOMÉTRICAS")
print("="*70)

mi_circulo = Circulo()
mi_rectangulo = Rectangulo()
mi_cuadrado = Cuadrado()
mi_elipse = Elipse()

print(mi_circulo.descripcion())
print(mi_rectangulo.descripcion())
print(mi_cuadrado.descripcion())
print(mi_elipse.descripcion())

# ============================================================================
# EJERCICIO 2: RELACIONES FAMILIARES
# ============================================================================
from Ejercicio_2.persona import Persona

print("\n" + "="*70)
print("EJERCICIO 2: RELACIONES FAMILIARES")
print("="*70)

p1 = Persona("Kate", "Windsor", "Middleton", "Mujer")
p2 = Persona("Guillermo", "Windsor", "Gales", "Hombre")
p3 = Persona("Diana", "Windsor", "Spencer", "Mujer")
p4 = Persona("Carlos", "Windsor", "Gales", "Hombre")

print(p2)
print(p2.casado_con(p1))
print(p2.es_hijo_de(p4, p3))

# ============================================================================
# EJERCICIO 3: LA GIOCONDA Y SU RÉPLICA
# ============================================================================
from Ejercicio_3.cuadro import Cuadro
from Ejercicio_3.lugar import Lugar

print("\n" + "="*70)
print("EJERCICIO 3: LA GIOCONDA Y SU RÉPLICA")
print("="*70)

louvre = Lugar("Museo del Louvre", "París", "Francia")
prado = Lugar("Museo del Prado", "Madrid", "España")

gioconda_original = Cuadro(
    Titulo="La Gioconda (Original)",
    AC="1503 — 1516",
    Tecnica="Óleo",
    Sub_tecnica="Sfumato",
    Soporte="Madera de álamo",
    Autor="Leonardo Da Vinci",
    Estado_Conservacion="Regular"
)
gioconda_original.establecer_lugar(louvre)

gioconda_replica = Cuadro(
    Titulo="La Gioconda (Réplica del Prado)",
    AC="1503 — 1516 (contemporánea)",
    Tecnica="Óleo",
    Sub_tecnica="Pincelada simple",
    Soporte="Madera de nogal",
    Autor="Anónimo (Alumno de Leonardo)",
    Estado_Conservacion="Muy bueno"
)
gioconda_replica.establecer_lugar(prado)
gioconda_replica.establecer_como_replica(gioconda_original)

print(f"Original: {gioconda_original.descripcion()}")
print(f"         Ubicación: {louvre.descripcion()}")
print(f"\nRéplica:  {gioconda_replica.descripcion()}")
print(f"         Ubicación: {prado.descripcion()}")
print(f"         Es réplica de: {gioconda_original.Titulo}")

# ============================================================================
# EJERCICIO 4: CATEDRAL DE SANTIAGO DE COMPOSTELA
# ============================================================================
from Ejercicio_4.edificio import Edificio  

print("\n" + "="*70)
print("EJERCICIO 4: CATEDRAL DE SANTIAGO DE COMPOSTELA")
print("="*70)

catedral_santiago = Edificio(
    "Catedral de Santiago de Compostela",
    "Católico",
    "Santiago de Compostela, Galicia, España",
    1075,
    1122,
    1128,
    1168,
    "3 de abril de 1211",
    1896,
    "Granito",
    "Románico, Gótico, Barroco, Plateresco, Neoclásico"
)

print(catedral_santiago.descripcion())

# ============================================================================
# EJERCICIO 5: FIGURAS GEOMÉTRICAS 2.0
# ============================================================================
from Ejercicio_5 import Circulo, Rectangulo, Cuadrado, Elipse  

print("\n" + "="*70)
print("EJERCICIO 5: FIGURAS GEOMÉTRICAS 2.0")
print("="*70)

circulo = Circulo("Rojo", 5)
rectangulo = Rectangulo(4, 2, "Azul")
cuadrado = Cuadrado(3, "Verde")
elipse = Elipse("Amarillo", 6, 3)

print(circulo.descripcion())
print(rectangulo.descripcion())
print(cuadrado.descripcion())
print(elipse.descripcion())

# ============================================================================
# EJERCICIO 6: ATRIBUTOS PERSONA 2.0
# ============================================================================
print("\n" + "="*70)
print("EJERCICIO 6: ATRIBUTOS PERSONA 2.0")
print("="*70)
from Ejercicio_6.Persona2 import Persona2
persona1 = Persona2("Juan", "Pérez", 30, "Masculino", "12345678A")
print(persona1)