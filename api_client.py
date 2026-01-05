import requests

class ApiClient:
    """Base API client for geospatial services."""

    def __init__(self, base_url: str):
        """Initializes the client with a base URL.

        Args:
            base_url (str): The root URL of the API.
        """
        self.base_url = base_url

    def fetch(self, params: dict) -> list:
        """Abstract method to fetch data.

        Args:
            params (dict): Query parameters.

        Raises:
            NotImplementedError: Subclasses must implement this method.
        """
        raise NotImplementedError("Subclasses must implement fetch()")


class GuestClient(ApiClient):
    """Anonymous client with standard access."""

    def fetch(self, params: dict) -> list:
        """Performs a simple request with a required User-Agent.

        Args:
            params (dict): Query parameters.

        Returns:
            list: List of results from Nominatim.
        """
        headers = {"User-Agent": "GuestClient/1.0"}
        response = requests.get(self.base_url, params=params, headers=headers)
        return response.json()


class AdminClient(ApiClient):
    """Admin client with private API key encapsulation."""

    def __init__(self, base_url: str, api_key: str):
        """Initializes admin with a private key.

        Args:
            base_url (str): The root URL of the API.
            api_key (str): Private access key.
        """
        super().__init__(base_url)
        self.__api_key = api_key

    def fetch(self, params: dict) -> list:
        """Performs an authorized request.

        Args:
            params (dict): Query parameters.

        Returns:
            list: List of results from Nominatim.
        """
        headers = {"User-Agent": "AdminClient/1.0", "Auth-Key": self.__api_key}
        response = requests.get(self.base_url, params=params, headers=headers)
        return response.json()