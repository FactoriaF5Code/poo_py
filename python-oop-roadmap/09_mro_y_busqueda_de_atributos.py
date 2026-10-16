"""
📌 CÓMO BUSCA PYTHON LOS ATRIBUTOS (MRO)

Cuando una clase hereda de otra, ¿cómo sabe Python dónde buscar
cada atributo o método? La regla es bastante sencilla:

Cuando haces objeto.algo, Python busca "algo" en este orden:
1. En el propio objeto (en su __dict__)
2. En su clase
3. En las clases padre, una detrás de otra

Ese orden se llama MRO (Method Resolution Order) y lo puedes
consultar con Clase.__mro__ o Clase.mro().

Al final de la cadena siempre está object, que es la clase de la que
hereda todo en Python.
"""


# =========================
#   CLASE A (SUPERCLASE)
# =========================
class A:
    # todas las instancias de A (o de quien herede de A) tendrán este método
    def method_a(self):
        print("Método de la clase A")


# =========================
#   CLASE B (SUBCLASE)
# =========================
class B(A):
    # B no define nada, todo lo que tenga lo saca de A
    pass


# =========================
#   CREAMOS INSTANCIAS Y PROBAMOS
# =========================
b = B()

# isinstance comprueba la herencia
print(isinstance(b, B))  # True -> b se creó con B()
print(isinstance(b, A))  # True -> b también hereda de A

# type() te dice la clase exacta, sin tener en cuenta la herencia
print(type(b) is B)  # True
print(type(b) is A)  # False

# podemos llamar al método heredado de A
b.method_a()  # Método de la clase A

# aquí se ve la "cadena" por la que Python va buscando
print(B.__mro__)  # (<class '__main__.B'>, <class '__main__.A'>, <class 'object'>)


"""
========================================================
VIÉNDOLO PASO A PASO
========================================================

method_a no está en el objeto b ni en la clase B,
está en A. Python lo encuentra porque sigue el MRO.
"""
print("method_a" in b.__dict__)  # False -> no está en el objeto
print("method_a" in B.__dict__)  # False -> no está en B
print("method_a" in A.__dict__)  # True  -> está en A


"""
========================================================
DONDE DE VERDAD IMPORTA: HERENCIA MÚLTIPLE
========================================================

Python deja que una clase herede de varias a la vez:
    class Hija(Padre1, Padre2)

Si las dos clases padre tienen un método con el mismo nombre,
¿cuál se usa? El que aparezca antes en el MRO.
Como regla general: de izquierda a derecha, según el orden
en el que pusiste las clases padre.
"""


class Flyer:
    def move(self):
        return "Vuelo"

    def describe(self):
        return "Sé volar"


class Swimmer:
    def move(self):
        return "Nado"

    def swim_deep(self):
        return "Buceo hasta el fondo"


class Duck(Flyer, Swimmer):
    pass


duck = Duck()
print(duck.move())       # Vuelo -> Flyer va antes que Swimmer
print(duck.describe())   # Sé volar (solo está en Flyer)
print(duck.swim_deep())  # Buceo hasta el fondo (solo está en Swimmer)
print([cls.__name__ for cls in Duck.__mro__])  # ['Duck', 'Flyer', 'Swimmer', 'object']


# Si cambiamos el orden de los padres, cambia el resultado
class Seagull(Swimmer, Flyer):
    pass


print(Seagull().move())  # Nado

"""
Úsala con cuidado: con muchas clases padre el código se vuelve
difícil de seguir. Lo más habitual es heredar de una sola clase
y, como mucho, añadir alguna clase pequeña con funcionalidad extra.
"""


"""
========================================================
EXTRA: CREAR UNA CLASE SIN LA PALABRA class
========================================================

En Python las clases también son objetos, así que se pueden crear
sin escribir class, usando type(nombre, padres, atributos).
No se usa casi nunca en el día a día, pero ayuda a entender
que una clase no es más que otro objeto.
"""


def method_c(self):
    print("Método de la clase C")


C = type("C", (A,), {"method_c": method_c})

c = C()
c.method_a()  # Método de la clase A (heredado)
c.method_c()  # Método de la clase C
print(isinstance(c, A))  # True
