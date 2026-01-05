from api_client import GuestClient
from validator import ApiResponseValidator
from geojson_converter import GeoJsonConverter

def main():
    """Integrates all modules to perform geocoding and conversion."""
    base_url = "https://nominatim.openstreetmap.org/search"
    search_params = {"q": "Kyiv", "format": "json", "limit": 1}

    client = GuestClient(base_url)
    raw_results = client.fetch(search_params)

    validator = ApiResponseValidator()
    validator.data = raw_results

    if validator.is_valid():
        converter = GeoJsonConverter(validator.data)
        converter.save("result.geojson")
        
        print("Success!")
        print(f"Location: {raw_results[0]['display_name']}")
        print("File 'result.geojson' created.")
    else:
        print("Validation failed: No results found.")

if __name__ == "__main__":
    main()