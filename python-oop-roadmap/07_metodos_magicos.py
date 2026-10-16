"""
📌 MÉTODOS MÁGICOS (DUNDER METHODS)

Son los métodos que empiezan y terminan con doble guion bajo,
como __init__, que ya conoces. También se llaman "dunder"
(de "double underscore").

No se suelen llamar directamente. Python los llama por ti cuando
usas ciertas cosas del lenguaje:

    print(obj)       -> obj.__str__()
    obj              -> obj.__repr__()   (en la consola o dentro de una lista)
    obj1 == obj2     -> obj1.__eq__(obj2)
    len(obj)         -> obj.__len__()
    obj1 + obj2      -> obj1.__add__(obj2)
    algo in obj      -> obj.__contains__(algo)

Gracias a ellos tus clases se pueden usar como si fueran
tipos propios de Python.
"""


"""
========================================================
1. __str__ Y __repr__: CÓMO SE MUESTRA UN OBJETO
========================================================

__str__  -> texto bonito para el usuario (lo usa print)
__repr__ -> texto para el programador, que deje claro qué objeto es.
            Por convención, se parece al código que lo crearía.
"""


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


p = Point(1, 2)
print(p)  # <__main__.Point object at 0x...>  no dice nada útil


class BetterPoint:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __repr__(self):
        return f"BetterPoint({self.x}, {self.y})"


p = BetterPoint(1, 2)
print(p)    # (1, 2)          -> usa __str__
print([p])  # [BetterPoint(1, 2)]  -> dentro de una lista usa __repr__


"""
========================================================
2. __eq__: CUÁNDO DOS OBJETOS SON IGUALES
========================================================

Por defecto, == en tus clases solo es True si es EL MISMO objeto.
Dos puntos con las mismas coordenadas serían "distintos".
Con __eq__ decides tú qué significa ser igual.
"""

print(Point(1, 2) == Point(1, 2))  # False


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __repr__(self):
        return f"Vector({self.x}, {self.y})"

    def __eq__(self, other):
        # si comparamos con algo que no es un Vector, que lo decida Python
        if not isinstance(other, Vector):
            return NotImplemented
        return self.x == other.x and self.y == other.y

    # 3. __add__: QUÉ HACE EL +
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)


print(Vector(1, 2) == Vector(1, 2))  # True
print(Vector(1, 2) + Vector(3, 4))   # Vector(4, 6)


"""
========================================================
4. __len__ Y __contains__: OBJETOS QUE GUARDAN COSAS
========================================================
"""


class Playlist:
    def __init__(self, name):
        self.name = name
        self._songs = []

    def add(self, song):
        self._songs.append(song)

    def __len__(self):
        return len(self._songs)

    def __contains__(self, song):
        return song in self._songs

    def __str__(self):
        return f"Playlist '{self.name}' con {len(self)} canciones"


playlist = Playlist("Para programar")
playlist.add("Lo-fi 1")
playlist.add("Lo-fi 2")

print(len(playlist))            # 2
print("Lo-fi 1" in playlist)    # True
print("Reggaeton" in playlist)  # False
print(playlist)                 # Playlist 'Para programar' con 2 canciones


"""
========================================================
CONSEJO
========================================================

Si solo vas a añadir uno, que sea __repr__ (o __str__).
Hace que depurar sea mucho más fácil, porque al imprimir
el objeto ves lo que tiene dentro.

No te inventes métodos dunder propios (__mi_metodo__):
ese formato está reservado para los que define Python.
"""
