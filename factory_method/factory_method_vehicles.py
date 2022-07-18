from typing import Union


class Vehicle:
    def get_brand(self) -> str:
        pass

    def get_wheels_count(self) -> int:
        pass

    def get_seats_count(self) -> int:
        pass

    def get_vehicle_type(self) -> str:
        """
        Ano of, air, land, water
        :return:
        """
        pass

    def get_engine_type(self) -> str:
        """
        Any of petrol, diesel, gas, electric
        :return:
        """

        pass


class Bike(Vehicle):
    def __init__(
        self,
        brand: str,
        wheel_count: int = 2,
        seats_count: int = 1,
        vehicle_type: str = "land",
    ):
        self._brand = brand
        self._wheel_count = wheel_count
        self._seats_count = seats_count
        self._vehicle_type = vehicle_type

    def get_brand(self) -> str:
        return self._brand

    def get_wheels_count(self) -> int:
        return self._wheel_count

    def get_seats_count(self) -> int:
        return self._seats_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def __str__(self):
        return f"Bike: {self._brand}"


class Airplane(Vehicle):
    def __init__(
        self,
        brand: str,
        engine_type: str = "Turboprop Engine",
        wheel_count: int = 6,
        seats_count: int = 100,
        vehicle_type: str = "air",
    ):
        self._brand = brand
        self._engine_type = engine_type
        self._wheel_count = wheel_count
        self._seats_count = seats_count
        self._vehicle_type = vehicle_type

    def get_brand(self) -> str:
        return self._brand

    def get_engine_type(self) -> str:
        return self._engine_type

    def get_wheels_count(self) -> int:
        return self._wheel_count

    def get_seats_count(self) -> int:
        return self._seats_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def __str__(self):
        return f"Airplane: {self._brand} with {self._engine_type} engine"


class Car(Vehicle):
    def __init__(
        self,
        brand: str,
        engine_type: str,
        wheel_count: int = 4,
        seats_count: int = 5,
        vehicle_type: str = "land",
    ):
        self._brand = brand
        self._engine_type = engine_type
        self._wheel_count = wheel_count
        self._seats_count = seats_count
        self._vehicle_type = vehicle_type

    def get_brand(self) -> str:
        return self._brand

    def get_engine_type(self) -> str:
        return self._engine_type

    def get_wheels_count(self) -> int:
        return self._wheel_count

    def get_seats_count(self) -> int:
        return self._seats_count

    def get_vehicle_type(self) -> str:
        return self._vehicle_type

    def __str__(self):
        return f"Car: {self._brand} with {self._engine_type} engine"


class VehicleFactory:
    def create(self) -> Vehicle:
        pass


class BMWCarCreator(VehicleFactory):
    def create(self) -> Car:
        return Car("BMW", "petrol")


class RometBikeCreator(VehicleFactory):
    def create(self) -> Bike:
        return Bike("Romet")


class BoeingPlaneCreator(VehicleFactory):
    def create(self) -> Vehicle:
        return Airplane("Boeing")


if __name__ == "__main__":
    vehicle_type = input("select vehicle type [bike,car, airplane]: ")
    vehicle_factory: Union[VehicleFactory, None] = None
    if vehicle_type.lower() == "bike":
        vehicle_factory = RometBikeCreator()
    elif vehicle_type.lower() == "car":
        vehicle_factory = BMWCarCreator()
    elif vehicle_type.lower() == "airplane":
        vehicle_factory = BoeingPlaneCreator()
    if vehicle_factory:
        vehicle = vehicle_factory.create()
        print(vehicle)
    else:
        print("Not implemented")
