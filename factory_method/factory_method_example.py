from abc import ABC, abstractmethod


class Creator(ABC):
    @abstractmethod
    def factory_method(self):
        pass

    def some_operation(self) -> str:
        product = self.factory_method()
        result = f"Creator code used with {product.operation()}"
        return result


class Product(ABC):
    @abstractmethod
    def operation(self) -> str:
        pass


class ConcreteProduct1(Product):
    def operation(self) -> str:
        return "Result of the ConcreteProduct1"


class ConcreteProduct2(Product):
    def operation(self) -> str:
        return "Result of the ConcreteProduct2"


class ConcreteCreator1(Creator):
    def factory_method(self):
        return ConcreteProduct1()


class ConcreteCreator2(Creator):
    def factory_method(self):
        return ConcreteProduct2()


def client_code(creator: Creator) -> None:
    print(
        f"Not aware of creator's class, but it doesn't matter \n{creator.some_operation()}"
    )


if __name__ == "__main__":
    print("Launch with ConcreteCreator1")
    client_code(ConcreteCreator1())
    print("Launch with ConcreteCreator2")
    client_code(ConcreteCreator2())
