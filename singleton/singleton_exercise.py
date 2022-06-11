#from singleton.singleton_metaclass import SingletonMeta
#metaclass=SingletonMeta

class Cake:
    class __CakeSingleton:
        def __init__(self):
            self._name: str = ""

        def set_name(self, name: str):
            self._name = name

        def get_name(self) -> str:
            return  self._name

        def print_name(self):
            print(self._name)
    __instance = None

    def __new__(cls):
        if not Cake.__instance:
            Cake.__instance = Cake.__CakeSingleton()
        return Cake.__instance

if __name__=='__main__':
    cake_1 = Cake()
    cake_1.print_name()
    cake_1.set_name("Poppy")
    cake_2 = Cake()
    cake_2.print_name()
    cake_1.print_name()
    cake_2.set_name("Apple")
    if cake_1.get_name() == cake_2.get_name():
        print("I'm a Singleton")
    else:
        print("I'm not Singleton")
    cake_2.print_name()
    cake_1.print_name()