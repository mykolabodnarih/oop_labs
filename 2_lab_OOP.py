class City:
    """A class representing a city.

    Attributes:
        name (str): The name of the city.
        population (int): The population of the city.
        coordinates (tuple): Coordinates (latitude, longitude).

    Class Attributes:
        country (str): The country name (shared by all cities).
    """

    country = "Ukraine"

    def __init__(self, name = str, population = int, coordinates = tuple):
        """Initializes a City instance.

        Args:
            name (str): The city name.
            population (int): The number of inhabitants.
            coordinates (tuple): Coordinates (latitude, longitude).
        """
        self.name = name
        self.population = population
        self.coordinates = coordinates

    def info(self):
        """Displays information about the city."""
        print(f"City: {self.name}")
        print(f"Country: {City.country}")
        print(f"Population: {self.population}")
        print(f"Coordinates: latitude {self.coordinates[0]}, longitude {self.coordinates[1]}")
        print("-" * 40)

    def move(self, dlat, dlon):
        """Changes the coordinates of the city by a given offset.

        Args:
            dlat (float): Latitude shift.
            dlon (float): Longitude shift.
        """
        lat, lon = self.coordinates
        self.coordinates = (lat + dlat, lon + dlon)



kyiv = City("Kyiv", 2950000, (50.45, 30.52))
lviv = City("Lviv", 721000, (49.84, 24.03))


kyiv.info()
lviv.info()



lviv.move(0.05, -0.03)
lviv.info()



class LandPlot:
    """A class representing a land plot.

    Attributes:
        cadastral_number (str): The cadastral number.
        area_ha (float): The plot area in hectares.
        category (str): The purpose of the land (residential, agricultural, etc.).

    Class Attributes:
        base_rate_uah_per_ha (float): Base land tax rate (UAH per hectare).
    """

    base_rate_uah_per_ha = 1500.0  

    def __init__(self, cadastral_number = str, area_ha = float, category = str):
        """Initializes a LandPlot instance.

        Args:
            cadastral_number (str): Cadastral number.
            area_ha (float): Area in hectares.
            category (str): Land category.
        """
        self.cadastral_number = cadastral_number
        self.area_ha = area_ha
        self.category = category

    def info(self):
        """Displays information about the land plot."""
        print(f"Land Plot No.: {self.cadastral_number}")
        print(f"Area: {self.area_ha} ha")
        print(f"Category: {self.category}")
        print(f"Base rate: {LandPlot.base_rate_uah_per_ha} UAH/ha")
        print("-" * 40)

    def calculate_tax(self, category_coeff):
        """Calculates land tax.

        Formula:
            tax = area * base_rate * coefficient

        Args:
            category_coeff (float): Coefficient depending on the land category.

        Returns:
            float: The land tax in UAH.
        """
        tax = self.area_ha * LandPlot.base_rate_uah_per_ha * category_coeff
        return tax



plot1 = LandPlot("1234567890:01:001", 2.5, "Residential")
plot2 = LandPlot("9876543210:02:002", 5.0, "Agricultural")


plot1.info()
plot2.info()


print(f"land tax: {plot1.calculate_tax(1.2):.2f} UAH")
print(f"land tax: {plot2.calculate_tax(0.8):.2f} UAH")




help(LandPlot)
