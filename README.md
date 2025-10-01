# Ejercicios-UML
EJERCICIO 1: Para cada figura, define el objeto y los valores correspondientes.

EJERCICIO 2: Define un diagrama de objetos a partir del siguiente texto. Kate Windsor (nacida Middleton) y Guillermo (Windsor) de Gales están casados. Guillermo de Gales es hijo de Carlos (Windsor) de Gales y de Diana de Gales (nacida Spencer).

# 📚 Ejercicios UML - Programación Orientada a Objetos

> Colección de ejercicios prácticos sobre diagramas UML y modelado de objetos en Python

[![Python](https://img.shields.io/badge/Python-3.12-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

---

## 🚀 Ejecución

Para ejecutar todos los ejercicios:

```bash
python main.py
```

Para ejecutar un ejercicio específico:

```bash
python Ejercicio_X/main.py
```

---

## 📋 Índice de Ejercicios

### 🔷 Ejercicio 1: Figuras Geométricas
**Objetivo:** Para cada figura, define el objeto y los valores correspondientes.

**Clases:** `Circulo`, `Rectangulo`, `Cuadrado`, `Elipse`

---

### 👨‍👩‍👦 Ejercicio 2: Relaciones Familiares
**Objetivo:** Define un diagrama de objetos a partir del siguiente texto.

**Descripción:** Kate Windsor (nacida Middleton) y Guillermo (Windsor) de Gales están casados. Guillermo de Gales es hijo de Carlos (Windsor) de Gales y de Diana de Gales (nacida Spencer).

**Clases:** `Persona`

---

### 🎨 Ejercicio 3: La Gioconda y su Réplica
**Objetivo:** Dibuja un diagrama de objetos a partir del siguiente texto, que describe una réplica conocida y estudiada de "La Gioconda".

**Detalles:**
- **Autor:** Anónimo (la original es de Leonardo Da Vinci)
- **Adscripción cronológica:** 1503 — 1516 (contemporánea a la original)
- **Técnica:** Óleo (al igual que la original)
- **Sub-técnica:** Pincelada simple (la original emplea "sfumato")
- **Material de soporte:** Madera de nogal (la original utiliza madera de álamo)

**Descripción:** Existen muchas réplicas o copias de La Gioconda (expuesta en el Museo Louvre de París), aunque ésta, que se encontraba en el Museo del Prado (Madrid) desde su inauguración, procedente de las Colecciones Reales, es la más antigua que se conoce. La conclusión del estudio efectuado en el Prado es que la réplica de Madrid fue realizada por un alumno de la escuela de Leonardo al mismo tiempo que el artista italiano pintaba su obra maestra.

**Clases:** `Cuadro`, `Lugar`

---

### ⛪ Ejercicio 4: Catedral de Santiago de Compostela
**Objetivo:** Define un diagrama de objetos que recoja las descripciones del templo.

**Descripción:** La Catedral de Santiago de Compostela es un templo de culto católico situado en la ciudad homónima, en el centro de la provincia de La Coruña, en Galicia (España). La construcción de la actual catedral se inició en 1075. El templo fue construido fundamentalmente en granito. La última piedra fue colocada en 1122 y la catedral fue consagrada en 1128. Sus múltiples ampliaciones han aunado en el edificio diversos estilos arquitectónicos (románico, gótico, barroco, plateresco y neoclásico). Fue declarada Bien de Interés Cultural en 1896.

---

### 🔶 Ejercicio 5: Clases de Figuras
**Objetivo:** A partir de las figuras del Ejercicio 1, define sus clases y atributos. Asegúrate de que las relaciones de instanciación entre los objetos y las clases están claras.

---

### 👤 Ejercicio 6: Modelo de Persona
**Objetivo:** Una persona tiene un nombre, dos apellidos, una fecha de nacimiento, un sexo y un número de identificación. Define las clases y los atributos correspondientes.

---

### 💼 Ejercicio 7: Proyectos Profesionales
**Objetivo:** Describe las características de los proyectos en los que habitualmente participas, según tu experiencia y profesión, utilizando tantas clases como sea necesario.

---

### 🏺 Ejercicio 8: Actuación Arqueológica
**Objetivo:** Una actuación arqueológica tiene una fecha de inicio, una fecha de fin y un tipo (sondeo, excavación o seguimiento). Define la clase correspondiente.

---

### 🖼️ Ejercicio 9: Análisis de Obra de Arte
**Objetivo:** Define una clase a partir del objeto representado usando tipos enumerados y elementos enumerados. ¿Qué cuadro es? ¿A quién representa? ¿Quién lo pintó? ¿Dónde? ¿Existen copias? ¿Qué técnica se usó? ¿De qué material es su soporte? ¿Dónde está ahora? ¿Cómo de bien se conserva?

---

### 🔗 Ejercicio 10: Asociaciones de Proyectos
**Objetivo:** A partir de las clases definidas en el Ejercicio 7, define las asociaciones necesarias para conectarlas.

---

### 🎭 Ejercicio 11: Diagrama de Clases de La Gioconda
**Objetivo:** A partir del diagrama de objetos obtenido en el Ejercicio 3, propón un diagrama de clases correspondiente con asociaciones, cardinalidades y roles.

---

### 🏛️ Ejercicio 12: Estructura Arqueológica
**Objetivo:** Una estructura arqueológica se identifica mediante un código, tiene una datación, esta compuesta de ciertos materiales y puede estar compuesta por otras estructuras. Define el diagrama de clases correspondiente.

---

### ◼️ Ejercicio 13: Polígonos
**Objetivo:** Un polígono es una porción de plano definida por al menos tres puntos. Define el diagrama correspondiente.

---

### 🔺 Ejercicio 14: Triángulos con Lado Común
**Objetivo:** Define un diagrama de objetos coherente con el diagrama de clases construido en el Ejercicio 13 para representar dos triángulos que tengan un lado común.

---

### 🔄 Ejercicio 15: Puntos Compartidos
**Objetivo:** Modifica el diagrama de clases del Ejercicio 13 para acomodar las situaciones en las que un punto pertenezca a varios polígonos a la vez.

---

### 👪 Ejercicio 16: Relaciones Familiares Completas
**Objetivo:** A partir de la clase Persona definida en el Ejercicio 6 y del diagrama de objetos definido en el Ejercicio 2, añade asociaciones, cardinalidades y roles para modelar las relaciones familiares pertinentes.

---

### 📚 Ejercicio 17: Sistema de Biblioteca Municipal
**Objetivo:** Modelar el funcionamiento de una biblioteca municipal con tres plantas, gestión de libros, lectores y empleados.

**Requisitos:**
- Control de capacidad de estanterías
- Organización por temática
- Sistema de préstamos (máximo 30 días)
- Gestión de penalizaciones
- Diferenciación entre lectores y empleados

---

## 📁 Estructura del Proyecto

```
Ejercicios-UML/
├── main.py                 # Ejecuta todos los ejercicios
├── README.md              # Este archivo
├── Ejercicio_1/           # Figuras geométricas
├── Ejercicio_2/           # Relaciones familiares
├── Ejercicio_3/           # La Gioconda
├── Ejercicio_4/           # Catedral
└── ...
```

---

## 🛠️ Tecnologías

- **Python 3.12**
- Programación Orientada a Objetos
- Diagramas UML

---

## 👨‍💻 Autor

**Victor220311**

---

## 📝 Licencia

Este proyecto está bajo la Licencia MIT.

---

**⭐ Si te ha sido útil, no olvides darle una estrella al repositorio!**

EJERCICIO 4: Considera la siguiente descripción. La Catedral de Santiago de Compostela es un templo de culto católico situado en la ciudad homónima, en el centro de la provincia de La Coruña, en Galicia (España). La construcción de la actual catedral se inició en 1075. El templo fue construido fundamentalmente en granito. La última piedra fue colocada en 1122 y la catedral fue consagrada en 1128. La última etapa de construcción comienza en 1168, y la catedral es definitivamente consagrada el 3 de abril de 1211. Sus múltiples ampliaciones han aunado en el edificio diversos estilos arquitectónicos (románico, gótico, barroco, plateresco y neoclásico). Fue declarada Bien de Interés Cultural en 1896. Define un diagrama de objetos que recoja las descripciones anteriores.

EJERCICIO 5: A partir de las figuras del Ejercicio 1 (que se muestran de nuevo a continuación), define sus clases y atributos. Asegúrate de que las relaciones de instanciación entre los objetos y las clases están claras.

EJERCICIO 6: Una persona tiene un nombre, dos apellidos, una fecha de nacimiento, un sexo y un número de identificación. Define las clases y los atributos correspondientes.

EJERCICIO 7: Describe las características de los proyectos en los que habitualmente participas, según tu experiencia y profesión, utilizando tantas clases como sea necesario. Para facilitar la comprensión de tu modelo, incluye la definición textual de las clases.

EJERCICIO 8: Una actuación arqueológica tiene una fecha de inicio, una fecha de fin y un tipo (sondeo, excavación o seguimiento). Define la clase correspondiente.

EJERCICIO 9: Define una clase a partir del objeto representado en la foto que se muestra a continuación, usando tipos enumerados y elementos enumerados. ¿Qué cuadro es? ¿A quién representa? ¿Quién lo pintó? ¿Dónde? ¿Existen copias? ¿Qué técnica se usó? ¿De qué material es su soporte? ¿Dónde está ahora? ¿Cómo de bien se conserva?

EJERCICIO 10: A partir de las clases definidas en el Ejercicio 7, define las asociaciones necesarias para conectarlas.

EJERCICIO 11: A partir del diagrama de objetos obtenido en el Ejercicio 3, propón un diagrama de clases correspondiente con asociaciones, cardinalidades y roles.

EJERCICIO 12: Una estructura arqueológica se identifica mediante un código, tiene una datación, esta compuesta de ciertos materiales y puede estar compuesta por otras estructuras. Define el diagrama de clases correspondiente.

EJRCICIO 13: Un polígono es una porción de plano definida por al menos tres puntos. El diagrama de objetos que se muestra a continuación representa un ejemplo de polígono (un cuadrado en este caso).

EJERCICIO 14: Define un diagrama de objetos coherente con el diagrama de clases construido en el Ejercicio 13 para representar dos triángulos que tengan un lado común.

EJERCICIO 15: Modifica el diagrama de clases del Ejercicio 13 para acomodar las situaciones en las que un punto pertenezca a varios polígonos a la vez, y ajustar el diagrama de objetos del Ejercicio 14 consecuentemente.

EJERCICIO 16: A partir de la clase Persona definida en el Ejercicio 6 y del diagrama de objetos definido en el Ejercicio 2, añade asociaciones, cardinalidades y roles para modelar las relaciones familiares pertinentes.

EJERCICIO 17: Se desea modelar el funcionamiento de una biblioteca municipal, la cual consta de tres plantas, de las que necesitamos saber la capacidad de sus estanterías (es decir, el número de libros que pueden albergar) para así realizar las reordenaciones oportunas cuando se reciben nuevos ejemplares. Los libros se organizan según la temática: libros infantiles, narrativa, ensayo, poesía, etc. Para ello, se deben registrar los libros que se encuentran en la biblioteca, teniendo en cuenta que puede haber más de un ejemplar de cada libro. Cada libro contará al menos con un identificador único, una fecha de préstamo y otra de entrega. El préstamo máximo será de 30 días. Los lectores que no entreguen el libro a tiempo tendrán penalización. Para aplicar esa penalización, la biblioteca cuenta con una ficha por cada lector, con su número de identificación o pasaporte, su nombre y su dirección postal. Para fomentar la lectura, los empleados de la biblioteca, que poseen su propia identificación como tales, pueden llevar libros a casa por un plazo mayor que los usuarios convencionales. Crea el modelo de clases correspondiente.