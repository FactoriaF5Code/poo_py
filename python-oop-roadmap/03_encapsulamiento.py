"""
📌 ENCAPSULAMIENTO EN PYTHON

El encapsulamiento consiste en proteger los datos internos de un objeto.
La idea es que no se toquen directamente ciertos datos, sino solo
a través de métodos que controlamos nosotros.

Aquí viene la parte curiosa: Python NO tiene atributos privados de verdad.
Lo que tiene son dos convenciones:

    _atributo   -> "esto es interno, porfa no lo uses desde fuera".
                   Es solo un aviso entre programadores, no bloquea nada.

    __atributo  -> Python le cambia el nombre por debajo (name mangling)
                   a _NombreClase__atributo. Así desde fuera no lo encuentras
                   con el nombre normal y tampoco lo pisa una clase hija sin querer.

En Python se suele decir "aquí todos somos adultos": se confía en que
la gente respete las convenciones.

En el día a día se usa mucho más _atributo que __atributo.
El doble guion bajo se reserva para cuando de verdad quieres evitar
choques de nombres con clases hijas.
"""


class User:
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.__password = password  # "privado" con doble guion bajo

    # Fíjate que NO hay un método que devuelva la contraseña.
    # Encapsular es decidir qué se puede hacer con el dato desde fuera.
    # Aquí lo único que necesitamos es comprobarla y cambiarla.

    def check_password(self, attempt):
        return self.__password == attempt

    def change_password(self, old_password, new_password):
        if not self.check_password(old_password):
            raise ValueError("La contraseña antigua no es correcta")

        if len(new_password) < 6:
            raise ValueError("La contraseña nueva debe tener al menos 6 caracteres")

        self.__password = new_password


# Ejemplo de uso
user = User("Kauan", "email@test.com", "123456")

print(user.check_password("123456"))  # True
print(user.check_password("hola"))    # False

user.change_password("123456", "nuevaClave123")
print(user.check_password("nuevaClave123"))  # True

try:
    user.change_password("loquesea", "otraClave")
except ValueError as error:
    print(f"Error: {error}")


"""
========================================================
IMPORTANTE
========================================================

Esto NO funciona:
    user.__password   -> AttributeError

Porque Python le ha cambiado el nombre al atributo.

Pero esto SÍ funciona (y por eso decimos que no es privado de verdad):
    user._User__password

Se puede, pero si lo haces te estás saltando el diseño de la clase
a propósito. No lo hagas en código real.
"""

try:
    print(user.__password)
except AttributeError:
    print("No se puede acceder a user.__password desde fuera")

print(user._User__password)  # la "trampa", solo para que veas que existe
