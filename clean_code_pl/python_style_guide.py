# Zmienne i metody -> snake_case
is_open = True


def open_window():
    pass


# Nazwy klas - > CamelCase
class Kyboard:
    pass


# Stałe -> SNAKE_CASE
MAX_VALUE = 10000
PI = 3.1415
# Moduły - snake_case
# proxy_image.py

"""Układ kodu"""
# pomiędzy funkcjami powinny być dwie puste linie odstępu
# pomiędzy metodami w klasie, jedna pusta linia odstępu


def function_1():
    pass


def function_2():
    pass


"""Używamy komentarzy i docstrinót (dokumentowania) tam, gdzie jest to konieczne"""


class Keyboard:
    """Implements method handling keyboard interactions."""

    pass


def multiply(a: int, b: int) -> int:
    """
    Multiplies two numbers

    :param: a :First parameter for multiplication
    :param b: Second parameter for multiplication
    :return: a*b (Product of two numbers)
    """
    return a * b
