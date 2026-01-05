import json

class GeoJsonConverter:
    """Converts Nominatim search results to GeoJSON format."""

    def __init__(self, data: list):
        """Initializes the converter with validated data.

        Args:
            data (list): Validated list of results.
        """
        self.data = data

    def to_feature(self) -> dict:
        """Converts the first result to a GeoJSON Feature.

        Returns:
            dict: GeoJSON Feature dictionary.
        """
        res = self.data[0]
        return {
            "type": "Feature",
            "geometry": {
                "type": "Point",
                "coordinates": [float(res["lon"]), float(res["lat"])]
            },
            "properties": {
                "name": res["display_name"]
            }
        }

    def save(self, filename: str) -> None:
        """Saves the Feature to a .geojson file.

        Args:
            filename (str): Target filename.
        """
        feature = self.to_feature()
        with open(filename, "w", encoding="utf-8") as f:
            json.dump(feature, f, indent=4, ensure_ascii=False)