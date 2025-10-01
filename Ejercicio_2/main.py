from Ejercicio_2 import Persona  # Ajusta "paquete" al nombre de tu carpeta.

# Crea instancias de Persona con los valores del diagrama.
kate = Persona("Kate", "Middleton", "Mujer")
guillermo = Persona("Guillermo", "Windsor", "Hombre")
diana = Persona("Diana", "Spencer", "Mujer")
carlos = Persona("Carlos", "Windsor", "Hombre")

# Simula relaciones "Está Casado Con".
guillermo.esta_casado_con = kate
kate.esta_casado_con = guillermo
carlos.esta_casado_con = diana
diana.esta_casado_con = carlos

# Simula relación "Es Hijo De".
guillermo.es_hijo_de = [carlos, diana]  # Guillermo es hijo de Carlos y Diana.

# Imprime para verificar.
print(kate.descripcion())
print(f"Está casado con: {kate.esta_casado_con.descripcion() if hasattr(kate, 'esta_casado_con') else 'Nadie'}")
print(guillermo.descripcion())
print(f"Está casado con: {guillermo.esta_casado_con.descripcion() if hasattr(guillermo, 'esta_casado_con') else 'Nadie'}")
print(f"Es hijo de: {[p.descripcion() for p in guillermo.es_hijo_de] if hasattr(guillermo, 'es_hijo_de') else 'Nadie'}")
print(diana.descripcion())
print(f"Está casada con: {diana.esta_casado_con.descripcion() if hasattr(diana, 'esta_casado_con') else 'Nadie'}")
print(carlos.descripcion())
print(f"Está casado con: {carlos.esta_casado_con.descripcion() if hasattr(carlos, 'esta_casado_con') else 'Nadie'}")