class Car:
    """A class representing a car.

    Attributes:
        brand (str): The brand of the car.
        model (str): The model of the car.
        mileage (float): The mileage of the car in kilometers.

    Class Attributes:
        vehicle_type (str): A shared attribute for all cars.
    """

    vehicle_type: str = "Automobile"

    def __init__(self, brand: str, model: str, mileage: float) -> None:
        """Initializes a Car instance.

        Args:
            brand (str): The car brand.
            model (str): The car model.
            mileage (float): The car mileage in kilometers.
        """
        self.brand: str = brand
        self.model: str = model
        self.mileage: float = mileage

    def drive(self, distance: float) -> float:
        """Increases the car's mileage after driving.

        Args:
            distance (float): The distance driven in kilometers.

        Returns:
            float: Updated mileage.
        """
        self.mileage += distance
        return self.mileage

    def __str__(self) -> str:
        """User-friendly string representation."""
        return f"{self.brand} {self.model} — {self.mileage} km"

    def __repr__(self) -> str:
        """Official representation of the object."""
        return f"Car(brand='{self.brand}', model='{self.model}', mileage={self.mileage})"

    def __eq__(self, other: object) -> bool:
        """Compares two cars by mileage."""
        if not isinstance(other, Car):
            return NotImplemented
        return self.mileage == other.mileage




car1 = Car("Toyota", "Corolla", 50000)
car2 = Car("Volkswagen", "Passat", 50000)
car3 = Car("Toyota", "Skyline", 65000)

print("user-friendly")
print(car1)
print(car2)

print("\ndeveloper view")
print(repr(car1))
print(repr(car3))


print(f"Initial mileage of {car1.model}: {car1.mileage} km")

print(f"After driving 250 km: {car1.drive(250)} km")


print(f"car1 == car2: {car1 == car2}")
print(f"car1 == car3: {car1 == car3}")


print(dir(car1))


print(f"Class name: {Car.__name__}")
print(f"Documentation string: {Car.__doc__}")
print(f"Object class: {car1.__class__}")
