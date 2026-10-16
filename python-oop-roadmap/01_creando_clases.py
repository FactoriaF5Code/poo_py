"""
📌 Una clase es un "molde" o plantilla que usamos para crear objetos.

Piénsalo así:
- La clase define cómo va a ser una persona
- El objeto es una persona concreta creada con ese molde

En este ejemplo:

class Person
    define el molde (la estructura de la persona)

__init__(self, name, age)
    es lo que se ejecuta cuando creamos el objeto.
    sirve para darle los valores iniciales.
    (es lo que normalmente se llama "constructor")

self
    es el propio objeto que se está creando. En Python hay que
    ponerlo siempre como primer parámetro de los métodos, no es magia,
    es simplemente cómo se pasa el objeto al método.

self.name / self.age
    guardan los datos dentro del objeto

greet()
    es una función que pertenece al objeto y puede usar sus datos

Resultado:
- Person es el molde
- user es una persona real creada con ese molde
- cada objeto tiene sus propios valores
"""


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        return f"Hola, mi nombre es {self.name}"


# Creamos un objeto (una instancia) a partir de la clase Person.
# Para crear el objeto llamamos a la clase como si fuera una función
user = Person("Kauan Rodrigues", 17)

print(user.greet())
