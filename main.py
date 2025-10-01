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
# EJERCICIO 4: LA GIOCONDA Y SU RÉPLICA
# ============================================================================
# main.py: Crea una instancia de Edificio con los datos de la Catedral de Santiago.
from Ejercicio_4.edificio import Edificio  # Ajusta "paquete" al nombre de tu carpeta.

# Crea la instancia de la Catedral de Santiago.
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

# Imprime para verificar.
print(catedral_santiago.descripcion())