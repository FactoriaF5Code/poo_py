"""
📌 ATRIBUTOS Y @property

Normalmente los atributos se usan directamente, tanto para leerlos
como para cambiarlos:

    product.name = "teclado"
    print(product.name)

¿Y cuándo controlamos el acceso a un atributo?
Solo cuando hace falta, por ejemplo:
- para validar el valor antes de guardarlo
- para devolver un valor calculado
- para que un atributo sea de solo lectura

Para eso está @property. Lo bueno es que desde fuera se sigue usando
igual (product.price), así que puedes empezar con un atributo normal
y convertirlo en property más adelante sin romper nada.
"""


"""
========================================================
1. ATRIBUTOS NORMALES (lo más habitual)
========================================================
"""


class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages


book = Book("Rebelión en la granja", "George Orwell", 144)
print(book.title)   # leemos directamente
print(book.author)

book.pages = 160    # y modificamos directamente (una edición con prólogo)
print(book.pages)

other_book = Book("1984", "George Orwell", 352)
print(f"{other_book.title}, de {other_book.author}")


"""
========================================================
2. @property CON VALIDACIÓN
========================================================

Ahora queremos que el precio no pueda ser negativo ni cero.
Con @property controlamos qué pasa al leerlo y al cambiarlo.
"""


class Product:
    def __init__(self, name, price):
        self.name = name
        # aquí ya pasa por el setter de abajo, así que también se valida al crear
        self.price = price

    # se ejecuta cuando hacemos product.price
    @property
    def price(self):
        return self._price

    # se ejecuta cuando hacemos product.price = nuevo_valor
    @price.setter
    def price(self, value):
        # bool es subclase de int en Python, por eso lo descartamos aparte
        if isinstance(value, (int, float)) and not isinstance(value, bool) and value > 0:
            self._price = value  # el _ delante es la convención de "no lo toques desde fuera"
        else:
            raise ValueError("El precio debe ser un número mayor que 0")

    def describe(self):
        return f"{self.name} cuesta {self.price:.2f} €"


# Ejemplo de uso
item = Product("keyboard", 150)

try:
    # intentamos poner un precio que no vale
    item.price = -4
except ValueError as error:
    print(f"Error: {error}")

item.price = 200
print(item.price)
print(item.describe())

# también se valida al crear el objeto
try:
    Product("mouse", 0)
except ValueError as error:
    print(f"Error: {error}")


"""
========================================================
3. PROPIEDADES CALCULADAS Y DE SOLO LECTURA
========================================================

Si una property no tiene setter, es de solo lectura.
Es muy útil para valores que se calculan a partir de otros:
así nunca se quedan desactualizados.
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    @property
    def area(self):
        # no se guarda en ningún sitio, se calcula cada vez que se pide
        return self.width * self.height


r = Rectangle(4, 5)
print(r.area)  # 20, sin paréntesis, como si fuera un atributo

r.width = 10
print(r.area)  # 50, se actualiza solo

try:
    r.area = 100  # no tiene setter
except AttributeError as error:
    print(f"Error: {error}")


"""
========================================================
RESUMEN
========================================================

- Empieza siempre con atributos normales.
- Usa @property solo cuando necesites validar, calcular o proteger.
"""
