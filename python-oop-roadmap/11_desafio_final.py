"""
############################################################
  🏦 Desafío Final: Sistema Bancario con Python POO
############################################################

Objetivo:
Crear un sistema bancario sencillo usando solo Python
(sin librerías externas), aplicando lo visto en los ejercicios:

- Clases y objetos
- Atributos y @property
- Encapsulamiento
- Herencia y polimorfismo
- Métodos mágicos
- Métodos de clase y estáticos
- Dataclasses


############################################################
  Requisitos del Sistema
############################################################

1. Transaction (dataclass)
--------------------------------------------------------

Una dataclass inmutable (frozen=True) que representa un movimiento.

Campos:
- kind: tipo de movimiento ("deposit", "withdraw", "transfer"...)
- amount: cantidad
- balance_after: saldo que queda después del movimiento


2. Clase Account (clase base)
--------------------------------------------------------

Atributos:
- owner: titular de la cuenta (atributo normal, público)
- _balance: saldo de la cuenta (por defecto 0)
- __password: contraseña de la cuenta (con doble guion bajo)
- _transactions: lista de Transaction

Métodos:
- deposit(amount): añade dinero al saldo
- withdraw(amount): retira dinero del saldo (con validaciones)
- balance: @property de SOLO LECTURA que devuelve el saldo.
  El saldo solo puede cambiar con deposit() y withdraw().
- check_password(attempt): devuelve True o False
- change_password(old, new): cambia la contraseña si la antigua es
  correcta y la nueva tiene al menos 6 caracteres
- get_statement(): devuelve el extracto (la lista de movimientos)

Métodos mágicos:
- __str__: algo como "Cuenta de Pepita - Saldo: 150.00 €"
- __repr__: algo como "Account(owner='Pepita', balance=150.0)"


3. SavingsAccount (Cuenta Ahorro)
----------------------------------

Hereda de: Account

Atributo extra:
- interest_rate: tasa de interés

Método extra:
- apply_interest(): aplica la tasa de interés al saldo


4. CurrentAccount (Cuenta Corriente)
----------------------------------

Hereda de: Account

Atributo extra:
- overdraft_limit: límite de descubierto

Sobrescribe:
- withdraw(): permite saldo negativo hasta el límite de descubierto


5. Clase Bank
--------------

Atributos de clase:
- name: nombre inventado del banco
- founded: año de fundación

Atributo:
- accounts: lista de cuentas registradas en el banco

Métodos:
- add_account(account): añade una cuenta a la lista
- find_account_by_owner(name): busca una cuenta por el nombre del titular
- transfer(from_account, to_account, amount): pasa dinero de una cuenta a otra

Métodos de clase:
- bank_info(): devuelve el nombre del banco y su año de fundación

Métodos mágicos:
- __len__: len(bank) devuelve cuántas cuentas tiene
- __contains__: "Pepita" in bank dice si hay alguna cuenta de ese titular


############################################################
  Extras (opcional, para complicarlo un poco más)
############################################################

- Bloquear la cuenta después de 3 intentos de contraseña incorrecta
- Hacer Account abstracta con abc y que solo se puedan crear
  SavingsAccount y CurrentAccount
- Crear tus propias excepciones (por ejemplo InsufficientFundsError)
- Añadir un @classmethod en Account para crear cuentas desde un texto,
  por ejemplo Account.from_string("Pepita,150")
- Hacer que transfer() funcione con cualquier objeto que tenga
  deposit() y withdraw() (duck typing), sea o no una Account


############################################################
  Qué se tiene que evaluar / comprobar
############################################################

1. POO básica:
- Creación de clases y objetos
- Uso de __init__ y self

2. Atributos y @property:
- owner es un atributo normal, sin @property (no le hace falta)
- balance se lee con una @property de solo lectura
- cuenta.balance = 1000 desde fuera tiene que dar error

3. Encapsulamiento:
- __password no se puede leer desde fuera
- No hay ningún método que devuelva la contraseña

4. Herencia y polimorfismo:
- SavingsAccount y CurrentAccount heredan de Account
- Se usa super() en lugar de repetir código del padre
- CurrentAccount.withdraw() se comporta distinto (permite descubierto)

5. Métodos mágicos:
- print(cuenta) muestra algo legible
- len(bank) y "nombre" in bank funcionan

6. Métodos de clase:
- Bank.bank_info() funciona sin crear ninguna instancia

7. Dataclasses:
- Transaction es una dataclass y no se puede modificar una vez creada

8. Comportamiento real:
- depositar, retirar, transferir y aplicar intereses funcionan bien
- Los errores se gestionan bien (saldo insuficiente, contraseña no válida,
  cantidades negativas o cero)
"""
