class ApiResponseValidator:
    """Validates the structure of the Nominatim API response."""

    def __init__(self):
        """Initializes the validator with no data."""
        self._data = None

    @property
    def data(self) -> list:
        """Gets or sets the data for validation.

        Returns:
            list: The data to be validated.
        """
        return self._data

    @data.setter
    def data(self, value: list):
        """Sets the data if it is a list.

        Args:
            value (list): Data from the API.

        Raises:
            ValueError: If the input is not a list.
        """
        if not isinstance(value, list):
            raise ValueError("Data must be a list of results")
        self._data = value

    def is_valid(self) -> bool:
        """Checks if the result list contains required keys.

        Returns:
            bool: True if the first result has lat and lon.
        """
        if not self._data or len(self._data) == 0:
            return False
        first = self._data[0]
        return "lat" in first and "lon" in first and "display_name" in first