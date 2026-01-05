class Car:
    """Represents a car with encapsulated data."""

    def __init__(self, brand: str, year: int, vin: str):
        """Initializes the car with different access levels."""
        self.brand = brand
        self._year = year
        self.__vin = vin

    @property
    def vin(self) -> str:
        """Returns the hidden VIN information."""
        return "Private VIN info"

    @vin.setter
    def vin(self, value: str):
        """Sets a new VIN if it has 17 characters."""
        if len(value) == 17:
            self.__vin = value
        else:
            print("Invalid VIN length")

    @vin.deleter
    def vin(self):
        """Clears the VIN data."""
        print("Deleting VIN...")
        self.__vin = None

my_car = Car("Tesla", 2023, "12345678901234567")
print(f"Brand: {my_car.brand}")
print(f"Protected year: {my_car._year}")
print(f"VIN property: {my_car.vin}")
print(f"All attributes: {dir(my_car)}")