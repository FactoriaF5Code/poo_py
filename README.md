# 🐍 python-POO

Guía con ejercicios, conceptos y ejemplos prácticos sobre **Programación Orientada a Objetos (POO)** usando **Python 3**.

El objetivo de este proyecto es aprender de forma clara y progresiva los fundamentos de la programación orientada a objetos (POO), entendiendo cómo Python implementa conceptos como: **Abstracción, Encapsulamiento, Herencia y Polimorfismo**, además de otras herramientas muy propias de Python como **@property**, **métodos mágicos**, **duck typing**, **dataclasses** y **métodos de clase y estáticos**.

---

## 📚 ¿Qué es la Programación Orientada a Objetos?

La Programación Orientada a Objetos (POO) es una forma de organizar y estructurar tu código usando objetos, clases, atributos y métodos.

**La idea central:** modelar cosas del mundo real dentro del código.

En Python, además, **todo es un objeto**: los números, las cadenas, las listas, las funciones e incluso las propias clases.

---


# 🚀 Conceptos clave de la POO
### 🔹 ¿Qué es un objeto?
Un objeto es una colección de atributos (datos) y métodos (funciones que trabajan con esos datos).
<details>
<summary>Ver ejemplo</summary>

En Python lo normal es crear los objetos a partir de una clase. Para hacernos una idea:

```python
class Persona:
    def __init__(self):
        self.nombre = "Pepita"
        self.edad = 25

    def saludar(self):
        print(f"Hola, soy {self.nombre}")


persona = Persona()
persona.saludar()
```
👉 Aquí:
- `nombre` y `edad` son datos (atributos)
- `saludar()` es una acción (método)
- `self.nombre` accede al propio objeto

</details>


### 🔹 ¿Qué es una clase?
Una clase es un molde para crear objetos. Piensa en ella como una receta: con la misma receta puedes hacer muchos pasteles.
<details>
<summary>Ver ejemplo</summary>

```python
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def greet(self):
        print(f"Hola, soy {self.name}")


user1 = Person("Pepita", 25)
user2 = Person("Carlos", 30)

user1.greet()
user2.greet()
```

👉 Aquí:
- La clase define cómo van a ser los objetos
- `__init__` se ejecuta al crear cada objeto y le da sus valores iniciales
- Para crear un objeto se llama a la clase como si fuera una función
- Cada objeto tiene sus propios datos
</details>


### 🔹 ¿Qué es el encapsulamiento?
Agrupar datos y funciones dentro de un mismo objeto para tenerlos organizados y protegidos, controlando cómo se accede a ellos.

Piensa en un mando a distancia:
- Tú puedes pulsar los botones (interfaz pública).
- No puedes tocar los circuitos de dentro (parte privada).

En código:
- Lo **"público"** es lo que puede usar quien utilice el objeto.
- Lo **"privado"** es lo que solo debería tocar la propia clase.

Ojo: en Python no hay privados "de verdad". Se usan convenciones:
- `_atributo` significa "esto es interno, no lo toques".
- `__atributo` hace que Python le cambie el nombre por debajo (*name mangling*) para que no se pueda usar tan fácilmente desde fuera.

<details>
<summary>Ver ejemplo</summary>

```python
class Cuenta:
    def __init__(self):
        self.__saldo = 0  # Parte privada

    def depositar(self, monto):  # Parte pública
        if monto <= 0:
            return
        self.__saldo += monto

    @property
    def saldo(self):  # Parte pública, solo lectura
        return self.__saldo


c = Cuenta()
c.depositar(100)
print(c.saldo)  # 100
c.saldo = 1000  # AttributeError: no se puede cambiar desde fuera
c.__saldo       # AttributeError: no existe con ese nombre desde fuera
```

👉 Aquí:
- El saldo se puede **leer**, pero solo cambia a través de `depositar()`.
- El dato `__saldo` no se puede usar directamente desde fuera con ese nombre.
</details>

### 🔹 ¿Qué es la herencia?
La herencia permite que una clase coja los atributos y métodos de otra clase, así no repites código.

- La clase **"padre"** tiene atributos y métodos.
- La clase **"hija"** recibe todo eso automáticamente.


<details>
<summary>Ver ejemplo</summary>

```python
class Persona:
    def __init__(self, nombre):
        self.nombre = nombre  # Parte del padre

    def saludar(self):
        print("Hola, soy " + self.nombre)


class Empleado(Persona):
    def __init__(self, nombre, sueldo):
        super().__init__(nombre)  # 1. Llama al __init__ del padre
        self.sueldo = sueldo      # 2. Añade lo propio del hijo


emp = Empleado("Carlos", 3000)
emp.saludar()
```
👉 Aquí:
- Creas un `Empleado`.
- `Empleado(Persona)` indica que `Empleado` hereda de `Persona`.
- **super().\_\_init\_\_(nombre)** ejecuta el `__init__` de `Persona`, que es quien guarda el nombre.
- Después añades lo que es solo del hijo (el sueldo).
- `self` siempre es el objeto final que estás creando (`emp`).
- En Python no es obligatorio llamar a `super()` antes de usar `self`, pero si no lo llamas, la parte del padre no se inicializa.

</details>


### 🔹 ¿Qué es el polimorfismo?
El polimorfismo permite que una clase hija cambie un método de la clase padre por su propia versión. **Mismo método, comportamiento distinto según la clase.**

Piensa que si le dices "haz un sonido" a distintos animales:
- un perro ladra
- un gato maúlla
- un pájaro canta

El método es el mismo **(hacer_sonido())**, pero lo que pasa cambia según la clase.

<details>
<summary>Ver ejemplo</summary>

```python
class Animal:
    def hacer_sonido(self):
        print("Sonido genérico...")


class Perro(Animal):
    def hacer_sonido(self):
        print("Guau!")


class Gato(Animal):
    def hacer_sonido(self):
        print("Miau!")


class Pajaro(Animal):
    def hacer_sonido(self):
        print("Pío pío!")


animales = [Perro(), Gato(), Pajaro()]

for a in animales:
    a.hacer_sonido()
```

👉 Aquí:
- Todas las clases tienen el mismo método: **hacer_sonido()**.
- Cada clase lo **redefine** a su manera.
- Puedes tratar a todos los objetos como "animales", aunque cada uno responda distinto.
</details>


### 🔹 ¿Qué es el duck typing?
*"Si camina como un pato y hace cuac como un pato, entonces es un pato."*

En Python no importa de qué clase sea un objeto, importa **lo que sabe hacer**. Si tiene el método que necesitas, lo puedes usar, aunque no herede de ninguna clase en común. Es polimorfismo sin herencia, y en Python es muy habitual.

<details>
<summary>Ver ejemplo</summary>

```python
class Pato:
    def hablar(self):
        return "Cuac!"


class Robot:
    def hablar(self):
        return "Bip bup."


def hacer_hablar(cosa):
    print(cosa.hablar())


hacer_hablar(Pato())
hacer_hablar(Robot())
```
👉 Aquí:
- `Pato` y `Robot` no tienen nada que ver entre sí.
- `hacer_hablar()` no pregunta de qué clase es cada uno, solo usa `hablar()`.
- Si le pasas algo que no tiene `hablar()`, falla con un `AttributeError`.

</details>


### 🔹 ¿Qué es @property?
Lo normal es usar los atributos directamente, tanto para leerlos como para cambiarlos:

```python
producto.precio = 10
print(producto.precio)
```

Pero a veces queremos controlar un atributo (validarlo, calcularlo o que sea de solo lectura), y para eso está el decorador `@property`. Lo bueno es que desde fuera se sigue usando igual, así que puedes empezar con un atributo normal y convertirlo en property más adelante sin romper nada.

Piensa en una casa:
- Al principio la puerta está abierta y entras sin más (atributo normal).
- Si un día hace falta, pones un portero en la puerta (`@property`), pero la puerta sigue siendo la misma.

<details>
<summary>Ver ejemplo</summary>

```python
class Usuario:
    def __init__(self, nombre):
        self.nombre = nombre  # esto ya pasa por el setter de abajo

    @property
    def nombre(self):
        # Se ejecuta cuando lees: u.nombre
        return self._nombre

    @nombre.setter
    def nombre(self, nuevo):
        # Se ejecuta cuando asignas: u.nombre = "..."
        if len(nuevo) < 3:
            raise ValueError("Nombre demasiado corto")
        self._nombre = nuevo

    @property
    def iniciales(self):
        # sin setter: es de solo lectura y se calcula cada vez
        return self._nombre[:2].upper()


u = Usuario("Pepita")
print(u.nombre)      # Pepita
print(u.iniciales)   # PE
u.nombre = "Li"      # ValueError: Nombre demasiado corto
```
👉 Aquí:
- **_nombre** es el atributo interno donde se guarda el valor de verdad.
- El **setter** (`@nombre.setter`) comprueba que el nombre tenga al menos 3 letras, también al crear el objeto.
- **iniciales** no tiene setter, así que es de solo lectura.
- Cuando usas **u.nombre** parece un atributo normal, pero en realidad estás llamando a un método.

</details>

### 🔹 ¿Qué son los métodos de clase y los estáticos?
Además de los métodos normales (que reciben `self`, el objeto), una clase puede tener:

- **Métodos de clase** (`@classmethod`): reciben la propia clase (`cls`) en vez del objeto. Se usan para trabajar con datos de la clase y, sobre todo, para crear objetos de otra forma (constructores alternativos).
- **Métodos estáticos** (`@staticmethod`): no reciben ni el objeto ni la clase. Son funciones normales que viven dentro de la clase porque tiene sentido que estén ahí. Se usan poco: si no necesitan nada de la clase, muchas veces quedan mejor como función suelta.

Ninguno de los dos necesita crear un objeto para usarse: se llaman directamente desde la clase.

<details>
<summary>Ver ejemplo</summary>

```python
class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    @classmethod
    def desde_texto(cls, texto):
        nombre, edad = texto.split(",")
        return cls(nombre, int(edad))

    @staticmethod
    def es_mayor_de_edad(edad):
        return edad >= 18


p = Persona.desde_texto("Pepita,25")
print(p.nombre)                       # Pepita
print(Persona.es_mayor_de_edad(15))   # False
```
👉 Aquí:
- `desde_texto()` crea una `Persona` a partir de un texto. Usa `cls(...)` para que también funcione en clases hijas.
- `es_mayor_de_edad()` no usa nada del objeto ni de la clase, solo comprueba un número.

</details>

### 🔹 ¿Qué son los métodos mágicos?
Son los métodos que empiezan y terminan con doble guion bajo, como `__init__`. No se suelen llamar directamente: Python los llama por ti cuando usas ciertas cosas del lenguaje.

| Lo que escribes | Lo que llama Python |
|-----------------|---------------------|
| `print(obj)`    | `obj.__str__()`     |
| `obj1 == obj2`  | `obj1.__eq__(obj2)` |
| `len(obj)`      | `obj.__len__()`     |
| `obj1 + obj2`   | `obj1.__add__(obj2)`|
| `x in obj`      | `obj.__contains__(x)` |

Gracias a ellos tus clases se pueden usar como si fueran tipos propios de Python.

<details>
<summary>Ver ejemplo</summary>

```python
class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y


print(Punto(1, 2))                 # (1, 2)
print(Punto(1, 2) == Punto(1, 2))  # True
```
👉 Aquí:
- Sin `__str__`, `print` mostraría algo como `<__main__.Punto object at 0x...>`.
- Sin `__eq__`, dos puntos con las mismas coordenadas no serían iguales.

</details>

### 🔹 ¿Qué es la abstracción?
Consiste en esconder los detalles internos y enseñar solo lo necesario. Conduces un coche sin saber cómo funciona el motor: solo necesitas acelerar, frenar y girar.

En Python se hace con **clases abstractas** (módulo `abc`): una clase base que dice qué métodos tienen que tener sus hijas, pero que no se puede usar directamente.

<details>
<summary>Ver ejemplo</summary>

```python
from abc import ABC, abstractmethod


class Figura(ABC):
    @abstractmethod
    def area(self):
        pass


class Cuadrado(Figura):
    def __init__(self, lado):
        self.lado = lado

    def area(self):
        return self.lado * self.lado


print(Cuadrado(5).area())  # 25
Figura()  # TypeError: no se puede crear una clase abstracta
```
👉 Aquí:
- `Figura` obliga a que todas sus hijas tengan `area()`.
- Si una hija no la implementa, Python no deja crear objetos de ella.

</details>

### 🔹 ¿Qué es una dataclass?
Muchas clases sirven sobre todo para guardar datos, y siempre acabas escribiendo lo mismo: un `__init__` que copia los parámetros, un `__repr__` para verlas y un `__eq__` para compararlas. `@dataclass` escribe todo eso por ti.

<details>
<summary>Ver ejemplo</summary>

```python
from dataclasses import dataclass


@dataclass
class Alumno:
    nombre: str
    edad: int
    nota: float = 0.0


a = Alumno("Pepita", 20, 8.5)
print(a)                                # Alumno(nombre='Pepita', edad=20, nota=8.5)
print(a == Alumno("Pepita", 20, 8.5))   # True
```
👉 Aquí:
- Solo se escriben los campos y su tipo, el `__init__` lo crea Python.
- Con `@dataclass(frozen=True)` los campos no se pueden cambiar después de crear el objeto.

</details>


---

## 📁 Estructura de los archivos

Todos los ejercicios están en la carpeta `python-oop-roadmap/` y se pueden ejecutar uno a uno con `python3 nombre_del_archivo.py`.

| Archivo                         | Contenido                                                                 |
|---------------------------------|--------------------------------------------------------------------------|
| `01_creando_clases.py`         | Introducción a la sintaxis de clases, `__init__`, `self` y creación de objetos. |
| `02_atributos_y_property.py`       | Atributos normales y cuándo usar `@property` (validación, valores calculados y solo lectura). |
| `03_encapsulamiento.py`     | Encapsulamiento con `_` y `__` (name mangling) y sus limitaciones en Python. |
| `04_herencia_y_polimorfismo.py`  | Herencia entre clases, `super()` y sobrescritura de métodos.          |
| `05_duck_typing.py`  | Polimorfismo sin herencia: lo que importa es lo que sabe hacer el objeto. |
| `06_metodos_de_instancia_de_clase_y_estaticos.py` | Métodos de instancia, `@classmethod` (constructores alternativos), `@staticmethod` y atributos de clase. |
| `07_metodos_magicos.py`  | `__str__`, `__repr__`, `__eq__`, `__add__`, `__len__` y `__contains__`. |
| `08_abstraccion.py`               | Clases abstractas con el módulo `abc` y la alternativa con `NotImplementedError`. |
| `09_mro_y_busqueda_de_atributos.py` | Cómo busca Python los atributos (MRO) y herencia múltiple. |
| `10_dataclasses.py`  | Clases de datos con `@dataclass`, valores por defecto y `frozen=True`. |
| `11_desafio_final.py`           | Desafío práctico para aplicar todos los conceptos de POO vistos.          |

---

## 💡 Observaciones

- Este repositorio se ha creado con fines **educativos**.
- Todo el código está escrito en **Python 3** sin librerías externas.
- Python tiene sus propias particularidades en la POO: no tiene atributos privados reales, pero sí clases abstractas de verdad. En cada archivo se explica cómo funciona.
