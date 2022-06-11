class Singleton:
    class __Singleton:
        def __init__(self):
            self.val: int = 0

        def __str__(self):
            return repr(self) +' '+ str(self.val)

    __instance = None
    #jest wywoływane pierwsze (przed __init__) przy tworzenie obiektu, init tylko nadaje/przypisuje wartości
    def __new__(cls):
        if not Singleton.__instance:
            Singleton.__instance = Singleton.__Singleton()
        return Singleton.__instance

if __name__=='__main__':
    x = Singleton()
    x.val = 11
    print(x)
    y = Singleton()
    print(y)
    y.val = 12
    print(y)