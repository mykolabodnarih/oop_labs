class River:
    """A class representing a river with its geographic characteristics.

    Attributes:
        name (str): The name of the river.
        length_km (float): The total length of the river in kilometers.
        source_lat (float): Latitude of the river source.
        source_lon (float): Longitude of the river source.
        mouth_lat (float): Latitude of the river mouth.
        mouth_lon (float): Longitude of the river mouth.

    Class Attributes:
        water_type (str): Type of water body (common for all rivers).
    """

    water_type: str = "freshwater"

    def __init__(
        self,
        name: str,
        length_km: float,
        source_lat: float,
        source_lon: float,
        mouth_lat: float,
        mouth_lon: float,
    ) -> None:
        """Initializes a River instance.

        Args:
            name (str): River name.
            length_km (float): River length in kilometers.
            source_lat (float): Latitude of the river source.
            source_lon (float): Longitude of the river source.
            mouth_lat (float): Latitude of the river mouth.
            mouth_lon (float): Longitude of the river mouth.
        """
        self.name = name
        self.length_km = length_km
        self.source_lat = source_lat
        self.source_lon = source_lon
        self.mouth_lat = mouth_lat
        self.mouth_lon = mouth_lon

    def flow_direction(self) -> str:
        """Determines the general flow direction of the river.

        Returns:
            str: Description of the river’s flow direction.
        """
        lat_diff = self.mouth_lat - self.source_lat
        lon_diff = self.mouth_lon - self.source_lon

        if abs(lat_diff) > abs(lon_diff):
            if lat_diff > 0:
                return "flows north"
            else:
                return "flows south"
        else:
            if lon_diff > 0:
                return "flows east"
            else:
                return "flows west"

    def info(self) -> None:
        """Prints detailed information about the river."""
        print(f"River name: {self.name}")
        print(f"Length: {self.length_km} km")
        print(f"Source coordinates: ({self.source_lat}, {self.source_lon})")
        print(f"Mouth coordinates: ({self.mouth_lat}, {self.mouth_lon})")
        print(f"Water type: {River.water_type}")
        print(f"Flow direction: {self.flow_direction()}")
        print("-" * 50)

    def __str__(self) -> str:
        """User-friendly string representation of the river."""
        return f"{self.name} — {self.length_km} km, {self.flow_direction()}"

    def __repr__(self) -> str:
        """Official representation of the river object."""
        return (
            f"River(name='{self.name}', length_km={self.length_km}, "
            f"source=({self.source_lat}, {self.source_lon}), "
            f"mouth=({self.mouth_lat}, {self.mouth_lon}))"
        )

    def __eq__(self, other: object) -> bool:
        """Compares two rivers by their length."""
        if not isinstance(other, River):
            return NotImplemented
        return self.length_km == other.length_km


dnipro = River("Dnipro", 2201, 55.33, 31.20, 46.50, 30.75)
nile = River("Nile", 6650, -2.0, 29.5, 31.1, 30.0)
amazon = River("Amazon", 6400, -10.0, -75.0, -1.5, -50.0)


dnipro.info()
nile.info()
amazon.info()


print(f"\n Is Nile same length as Amazon? {nile == amazon}")


print("\n", str(dnipro))
print("\n", repr(amazon))


print("\n", dir(dnipro))


print(f"Class name: {River.__name__}")
print(f"Documentation: {River.__doc__}")
print(f"Object class: {dnipro.__class__}")
print(f"Attributes dictionary: {dnipro.__dict__}")
