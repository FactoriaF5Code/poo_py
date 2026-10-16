"""
📌 DUCK TYPING

"Si camina como un pato y hace cuac como un pato, entonces es un pato."

En Python no importa de qué clase sea un objeto, importa lo que sabe hacer.
Si un objeto tiene el método que necesitas, lo puedes usar y punto.
No hace falta que herede de ninguna clase en común.

Esto es polimorfismo igual que en el ejercicio anterior,
pero SIN herencia. En Python es muy habitual.
"""


# Tres clases que no tienen nada que ver entre sí:
# ninguna hereda de otra, pero todas tienen un método speak()

class Duck:
    def speak(self):
        return "Cuac!"


class Robot:
    def speak(self):
        return "Bip bup."


class Person:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"Hola, soy {self.name}."


# Esta función no comprueba de qué clase es cada cosa.
# Solo da por hecho que tiene speak(), y con eso le basta.
def make_it_speak(thing):
    print(thing.speak())


for thing in [Duck(), Robot(), Person("Pepita")]:
    make_it_speak(thing)


"""
========================================================
¿Y SI NO TIENE EL MÉTODO?
========================================================

Pues falla cuando se intenta llamar, con un AttributeError.
En Python se suele preferir intentarlo y gestionar el error
antes que ir comprobando el tipo con if isinstance(...) por todas partes.
"""


class Stone:
    pass


try:
    make_it_speak(Stone())
except AttributeError:
    print("Una piedra no sabe hablar")


"""
========================================================
DUCK TYPING EN COSAS QUE YA USAS
========================================================

Python lo usa todo el rato. Por ejemplo, un bucle for funciona
con listas, cadenas, diccionarios, ficheros... porque todos
saben "dar sus elementos uno a uno", no porque hereden de lo mismo.

Y lo mismo pasa con len(): funciona con cualquier objeto que
tenga el método __len__. Esto lo vemos en el ejercicio de métodos mágicos.
"""

for item in [1, 2, 3]:
    print(item)

for letter in "hola":
    print(letter)
