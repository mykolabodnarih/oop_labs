class Calculator:
    """A simple calculator with various method types."""

    def __init__(self, owner: str):
        """Initializes the calculator."""
        self.owner = owner
        self._last_result: float = 0.0

    @property
    def last_result(self) -> float:
        """Returns the last calculated result."""
        return self._last_result

    @last_result.setter
    def last_result(self, value: float):
        """Sets the last result with validation."""
        self._last_result = value

    def add(self, a: float, b: float) -> float:
        """Adds two numbers and saves the result."""
        self._last_result = a + b
        return self._last_result

    @classmethod
    def from_string(cls, owner_name: str) -> "Calculator":
        """Creates a calculator instance from a string."""
        return cls(owner_name)

    @staticmethod
    def is_even(number: int) -> bool:
        """Checks if a number is even."""
        return number % 2 == 0

calc = Calculator("User1")
print(f"Add result: {calc.add(10, 5)}")
print(f"Is 10 even? {Calculator.is_even(10)}")