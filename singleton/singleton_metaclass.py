class SingletonMeta(type):
    __instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls.__instances:
            instance = super().__call__(*args, **kwargs)
            cls.__instances[cls] = instance
        return cls.__instances[cls]


class Singleton(metaclass=SingletonMeta):
    def __init__(self):
        self.val: int = 0

    def print_val(self):
        print(self.val)


if __name__ == "__main__":
    a = Singleton()
    a.print_val()
    a.val = 30

    a.print_val()

    b = Singleton()
    b.print_val()
