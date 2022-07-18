# do zrobienia ładnej kopii obiektu
# shallow_copy / deep_copy
# konstruuje obiekt i umieszcza w nim referencję innych obiektów
# deep_copy kopiuje wszystko
import copy


class Car:
    def __init__(
        self,
        wheels_count: int,
        doors_count: int,
        brand: str = "",
        color: str = "",
        model: str = "",
    ):
        self._wheels_count = wheels_count
        self._doors_count = doors_count
        self._brand = brand
        self._color = color
        self._model = model

    @property
    def wheels_count(self) -> int:
        return self._wheels_count

    @wheels_count.setter
    def wheels_count(self, value: int):
        self._wheels_count = value

    @property
    def model(self) -> int:
        return self._wheels_count

    @model.setter
    def model(self, value: int):
        self._model = value

    @property
    def doors_count(self) -> int:
        return self._doors_count

    @doors_count.setter
    def doors_count(self, value: int) -> None:
        self._doors_count = value

    @property
    def brand(self) -> str:
        return self._brand

    @brand.setter
    def brand(self, value: int) -> None:
        self._brand = value

    @property
    def color(self) -> str:
        return self._color

    @color.setter
    def color(self, value: int) -> None:
        self._color = value

    def clone(self):
        return copy.copy(self)

    def __str__(self):
        return (
            f"Car: {self._color} {self._brand} {self._model} with"
            f" {self._doors_count} doors and {self._wheels_count} wheels"
        )


class CarManager:
    _base_car = Car(4, 5)

    @staticmethod
    def create_car_with_color(brand: str, color: str, model: str) -> Car:
        base_car_clone = CarManager._base_car.clone()
        base_car_clone.brand = brand
        base_car_clone.color = color
        base_car_clone.model = model
        return base_car_clone


if __name__ == "__main__":
    car_1 = CarManager.create_car_with_color("Audi", "A4", "Pink")
    car_2 = CarManager.create_car_with_color("Skoda", "Fabia", "Aquamarine")
    print(car_1)
    print(car_2)
