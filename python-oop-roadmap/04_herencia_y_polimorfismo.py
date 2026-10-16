"""
📌 HERENCIA Y POLIMORFISMO EN PYTHON

Herencia:
Permite que una clase "hija" reutilice atributos y métodos de una clase "padre",
así no repetimos código y es más fácil mantener y ampliar el programa.
En Python se indica poniendo la clase padre entre paréntesis: class Dog(Animal)

Polimorfismo:
Un mismo método se comporta distinto según la clase que lo implemente.
"""


class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        return f"{self.name} hace un sonido."


class Dog(Animal):
    # Polimorfismo: cambiamos speak solo para Dog
    def speak(self):
        return f"{self.name} ladra."


class Cat(Animal):
    def __init__(self, name, breed):
        super().__init__(name)  # llamamos al __init__ del padre (Animal)
        self.breed = breed

    # Sobrescribimos speak, pero aprovechamos lo que ya hace el padre
    # con super() y le añadimos algo nuevo
    def speak(self):
        return f"{super().speak()} Es de raza {self.breed}."


class Rabbit(Animal):
    # No tiene __init__ propio, así que usa el de Animal.
    # Tampoco sobrescribe speak(), se queda con el comportamiento de Animal.
    pass


# ==========================
# Creamos los objetos y probamos

dog = Dog("Rex")
print(dog.speak())  # Rex ladra.

cat = Cat("Firulais", "SRD")
print(cat.speak())  # Firulais hace un sonido. Es de raza SRD.

rabbit = Rabbit("Conejito")
print(rabbit.speak())  # Conejito hace un sonido.


# Lo bonito del polimorfismo: podemos tratarlos a todos igual
# sin preocuparnos de qué clase es cada uno
for animal in [dog, cat, rabbit]:
    print(animal.speak())
