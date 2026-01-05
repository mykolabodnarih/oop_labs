
"""
saveecobot_to_geojson.py
------------------------

This script downloads air quality monitoring data from the SaveEcoBot API
(https://api.saveecobot.com/output.json), converts it into a GeoJSON
FeatureCollection, and saves the result to a local file.

Each station is represented as a GeoJSON Point with attributes such as:
- id, cityName, stationName, localName
- platformName, timezone
- pollutants (a list of measured parameters: PM2.5, PM10, temperature, etc.)

Usage:
    python saveecobot_to_geojson.py

Author: Volodymyr Nikulishyn
License: MIT
"""

import json
import requests
from typing import Any, Dict, List, Optional
from decorators import measure_time, log_action

URL: str = "https://api.saveecobot.com/output.json"
OUTPUT: str = r"saveecobot.geojson"


def to_float(v: Any) -> Optional[float]:
    """Convert a value to float if possible.

    Args:
        v: Any input value (usually string or number).

    Returns:
        Float value if conversion succeeds, otherwise None.
    """
    try:
        return float(v)
    except (TypeError, ValueError):
        return None


@measure_time
@log_action
def fetch_data(url: str) -> List[Dict[str, Any]]:
    """Fetch JSON data from the SaveEcoBot API.

    Args:
        url: API endpoint URL.

    Returns:
        A list of dictionaries representing station data.
    """
    resp = requests.get(url, timeout=15)
    resp.raise_for_status()
    return resp.json()


def to_feature(item: Dict[str, Any]) -> Optional[Dict[str, Any]]:
    """Convert a station dictionary into a GeoJSON Feature.

    Args:
        item: A dictionary with station data.

    Returns:
        A GeoJSON Feature dictionary or None if coordinates are invalid.
    """
    lon = to_float(item.get("longitude"))
    lat = to_float(item.get("latitude"))
    if lon is None or lat is None:
        return None

    return {
        "type": "Feature",
        "geometry": {"type": "Point", "coordinates": [lon, lat]},
        "properties": {
            "id": item.get("id"),
            "cityName": item.get("cityName"),
            "stationName": item.get("stationName"),
            "localName": item.get("localName"),
            "platformName": item.get("platformName"),
            "timezone": item.get("timezone"),
            "pollutants": item.get("pollutants", []),
        },
    }


def to_geojson(data: List[Dict[str, Any]]) -> Dict[str, Any]:
    """Convert a list of station records to a GeoJSON FeatureCollection.

    Args:
        data: A list of station data dictionaries.

    Returns:
        A GeoJSON FeatureCollection dictionary.
    """
    features = list(filter(None, map(to_feature, data)))
    return {"type": "FeatureCollection", "features": features}


def save_geojson(geojson_data: Dict[str, Any], path: str) -> None:
    """Save a GeoJSON object to a file.

    Args:
        geojson_data: GeoJSON dictionary to save.
        path: Path to output file.
    """
    with open(path, "w", encoding="utf-8") as f:
        json.dump(geojson_data, f, ensure_ascii=False, indent=2)
    print(f"GeoJSON saved to {path}")


if __name__ == "__main__":
    data = fetch_data(URL)
    geojson = to_geojson(data)
    save_geojson(geojson, OUTPUT)
