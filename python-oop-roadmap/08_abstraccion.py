"""
📌 ABSTRACCIÓN EN PYTHON

La abstracción consiste en esconder los detalles internos y enseñar
solo lo necesario de un objeto o sistema.

Ejemplo de la vida real:
- Conduces un coche sin saber cómo funciona el motor por dentro.
- Solo necesitas saber que puedes acelerar(), frenar() y girar().

Python tiene clases abstractas "de verdad"
gracias al módulo abc (Abstract Base Classes):
- La clase base hereda de ABC.
- Los métodos obligatorios se marcan con @abstractmethod.
- No se puede crear un objeto de una clase abstracta.
- Si una hija no implementa todos los métodos abstractos, tampoco
  se puede instanciar. Python te avisa al crear el objeto, no más tarde.
"""

from abc import ABC, abstractmethod


class Shape(ABC):
    # cualquier figura tiene que saber calcular su área
    @abstractmethod
    def area(self):
        pass


class Square(Shape):
    def __init__(self, side):
        self.side = side

    def area(self):
        return self.side * self.side


# Ejemplo de uso
s = Square(5)
print(s.area())  # 25


# Si intentamos crear la clase base directamente, falla
try:
    broken = Shape()
except TypeError as error:
    print(f"Error: {error}")


# Y si una hija se olvida de implementar area(), también falla
class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius
    # aquí falta area()


try:
    c = Circle(3)
except TypeError as error:
    print(f"Error: {error}")


"""
========================================================
LA FORMA "A MANO"
========================================================

También puedes ver código que no usa abc y simplemente lanza
NotImplementedError en el método base. Funciona, pero el error
solo salta cuando llamas al método, no cuando creas el objeto.
"""


class ShapeManual:
    def area(self):
        raise NotImplementedError("El método area() debe implementarlo la subclase.")


broken2 = ShapeManual()  # esto deja crearlo sin problema...

try:
    broken2.area()  # ...y el fallo llega aquí
except NotImplementedError as error:
    print(f"Error: {error}")
