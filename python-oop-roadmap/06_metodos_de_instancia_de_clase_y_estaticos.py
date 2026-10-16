"""
📌 MÉTODOS DE INSTANCIA, DE CLASE Y ESTÁTICOS

Métodos de instancia (los normales):
- Reciben self (el objeto) como primer parámetro.
- Trabajan con los datos de ESE objeto.
- Son con diferencia los que más vas a escribir.

Métodos de clase (@classmethod):
- Reciben cls (la clase) como primer parámetro en vez del objeto.
- Sirven para trabajar con datos de la clase.
- Su uso más típico: crear objetos de otra forma (constructores alternativos).

Métodos estáticos (@staticmethod):
- No reciben ni self ni cls. Son funciones normales metidas
  dentro de la clase porque tiene sentido que vivan ahí.
- Se usan poco. Si una función no necesita nada de la clase,
  muchas veces queda mejor como función suelta en el módulo.

Pregunta rápida para elegir:
- ¿Necesita datos del objeto?         -> método de instancia
- ¿Necesita la clase pero no un objeto? -> @classmethod
- ¿No necesita ninguna de las dos?     -> @staticmethod (o función suelta)
"""


class Person:
    # Atributos de clase: se definen fuera del __init__ y son de la clase
    species = "Homo sapiens"
    count = 0  # cuántas personas se han creado

    def __init__(self, name, age):
        if not Person.is_valid_age(age):
            raise ValueError("La edad no es válida")

        # Atributos de instancia: cada objeto tiene los suyos
        self.name = name
        self.age = age

        Person.count += 1  # sumamos uno cada vez que se crea alguien

    # Método de instancia: usa los datos del objeto
    def greet(self):
        return f"Hola, mi nombre es {self.name}"

    # Método de clase: usa datos de la clase, no de un objeto concreto
    @classmethod
    def describe_species(cls):
        return f"Los humanos pertenecen a la especie {cls.species}"

    @classmethod
    def get_count(cls):
        return cls.count

    # Constructor alternativo: crea una persona a partir de un texto "nombre,edad".
    # Usamos cls(...) en vez de Person(...) para que si una clase hija
    # lo hereda, se cree un objeto de la clase hija y no un Person.
    @classmethod
    def from_string(cls, text):
        name, age = text.split(",")
        return cls(name.strip(), int(age))

    # Método estático: no usa ni self ni cls, solo comprueba un valor
    @staticmethod
    def is_valid_age(age):
        return 0 <= age <= 150


# Uso de métodos y atributos de clase, sin crear ningún objeto
print(Person.species)             # Homo sapiens
print(Person.describe_species())  # Los humanos pertenecen a la especie Homo sapiens
print(Person.is_valid_age(200))   # False

# Creamos instancias de las dos formas
p1 = Person("Pepita", 25)
p2 = Person.from_string("Maria, 30")

# Métodos de instancia (a través de los objetos)
print(p1.greet())  # Hola, mi nombre es Pepita
print(p2.greet())  # Hola, mi nombre es Maria

# Intentar usar un método de instancia desde la clase NO funciona,
# porque le falta el self:
# print(Person.greet())  # TypeError: missing 1 required positional argument: 'self'

try:
    Person("Matusalén", 969)
except ValueError as error:
    print(f"Error: {error}")

"""
Ojo con esto: p1.species también funciona.

Si el objeto no tiene ese atributo, Python lo busca en la clase.
Por eso p1.species devuelve "Homo sapiens".

Leerlo así está bien, pero cuidado con ASIGNARLO desde el objeto:
p1.species = "otra" no cambia la clase, crea un atributo nuevo solo en p1.
"""
print(p1.species)  # Homo sapiens

p1.species = "Marciano"
print(p1.species)      # Marciano (solo p1)
print(p2.species)      # Homo sapiens
print(Person.species)  # Homo sapiens

# Contador de instancias
print(Person.get_count())  # 2
