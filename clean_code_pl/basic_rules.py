"""Używamy samotłumaczących się nazw zmiennych i metod"""
# d=10
elapsed_time_in_days = 10


# def test_test_test(a,b):
#   return a+b


def add(a, b):
    return a + b


"""Nazwy klas powinny być rzeczownikami lub składać się z rzeczowników"""
# class Keybarding:
#   pass


class Keyboard:
    pass


"""Minimalizujemy liczbę argumentów w metodach kiedy się da"""


def path_builder(a, b, c, d, e, f, g, h):
    return f"{a}/{b}/{c}"


def path_builder(*args):
    return f"{'/'.join(args)}"


# Metody powinny robić 1 rzecz i nie powinny być długie
def multiply(a, b):
    suma = a + b
    dif = a - b
    div = a / b
    return a * b


from python_style_guide import multiply

multiply(2, 3)

# DRY - don't repeat yourself
# KISS - keep it stupid simple
# YAGNI - you aren't gonna need it

# SOLID
# S - Single Responsebility Method
# O - open-close principle (kod otwarty na rozszeranie, ale zamknięty na modyfikację)
# L - Liskov substitution principle
# I - Interface segregation principle (nie definiujemy interfejsów dla wielu metod naraz)
# D - Dependency inversion principle (Wysokopoziomowe moduły nie powinny zależeć od modułów niskopoziomowych - zależności między nimi powinny wynikać z abstrakcji.)


# Pylint - narzędzie pokzujące jak refakturyzować kod
