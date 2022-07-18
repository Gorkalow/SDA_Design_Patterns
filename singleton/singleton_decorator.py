def singleton(class_):
    __instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in __instances:
            __instances[class_] = class_(*args, **kwargs)
        return __instances[class_]

    return get_instance


@singleton
class FirstClass:
    """First Class"""

    def __init__(self):
        self.val: int = 0


@singleton
class SecondClass:
    """Second Class"""

    def __init__(self):
        self.val: int = 0


if __name__ == "__main__":
    a = FirstClass()
    print(a.val)
    a.val = 13
    b = FirstClass()
    print(b.val)
    print(a.val)

    c = SecondClass()
    print(c.val)
    c.val = 20
    print(c.val)
