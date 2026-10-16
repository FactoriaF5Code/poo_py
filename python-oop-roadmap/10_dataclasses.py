"""
📌 DATACLASSES

Muchas clases sirven sobre todo para guardar datos. Para esas
acabas escribiendo siempre lo mismo: un __init__ que copia los
parámetros a self, un __repr__ para poder verlas y un __eq__ para
compararlas.

@dataclass (del módulo dataclasses) escribe todo eso por ti.
Solo tienes que decir qué campos tiene la clase y de qué tipo son.

Los tipos (str, int, float...) aquí son obligatorios para que
dataclass sepa cuáles son los campos, pero Python no los comprueba:
son solo información.
"""

from dataclasses import dataclass, field


"""
========================================================
1. SIN DATACLASS VS CON DATACLASS
========================================================
"""


class StudentManual:
    def __init__(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade

    def __repr__(self):
        return f"StudentManual(name={self.name!r}, age={self.age}, grade={self.grade})"

    def __eq__(self, other):
        if not isinstance(other, StudentManual):
            return NotImplemented
        return (self.name, self.age, self.grade) == (other.name, other.age, other.grade)


# Esto hace exactamente lo mismo que la clase de arriba
@dataclass
class Student:
    name: str
    age: int
    grade: float


s1 = Student("Pepita", 20, 8.5)
s2 = Student("Pepita", 20, 8.5)

print(s1)        # Student(name='Pepita', age=20, grade=8.5)
print(s1 == s2)  # True


"""
========================================================
2. VALORES POR DEFECTO Y MÉTODOS PROPIOS
========================================================

Una dataclass sigue siendo una clase normal: puedes añadirle
métodos, properties, herencia...

Ojo con las listas: no se puede poner "students: list = []"
(Python da error) porque todos los objetos compartirían la misma lista.
Para eso se usa field(default_factory=list), que crea una nueva cada vez.
"""


@dataclass
class Course:
    name: str
    hours: int = 20
    students: list = field(default_factory=list)

    def enroll(self, student):
        self.students.append(student)

    @property
    def total_students(self):
        return len(self.students)


course = Course("Python")
course.enroll(s1)
print(course.hours)           # 20
print(course.total_students)  # 1

other = Course("Bases de datos")
print(other.total_students)   # 0 -> cada curso tiene su propia lista


"""
========================================================
3. DATACLASSES INMUTABLES (frozen=True)
========================================================

Con frozen=True no se pueden cambiar los campos después de crear
el objeto. Viene bien para datos que no deberían cambiar nunca,
como una fecha de nacimiento o un movimiento bancario.
"""


@dataclass(frozen=True)
class Coordinate:
    lat: float
    lon: float


madrid = Coordinate(40.4168, -3.7038)

try:
    madrid.lat = 0
except AttributeError as error:  # FrozenInstanceError es un AttributeError
    print(f"Error: {error}")


"""
========================================================
¿CUÁNDO USARLA?
========================================================

- La clase es sobre todo un "contenedor" de datos -> @dataclass
- La clase tiene mucha lógica, validaciones o un __init__ complicado
  -> clase normal

Tampoco es todo o nada: puedes empezar con una dataclass
e ir añadiéndole métodos según los necesites.
"""
