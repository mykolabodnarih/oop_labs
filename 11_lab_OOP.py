class Geometry:
    """Part of a Feature (Composition)."""
    def __init__(self, coords: list):
        self.coords = coords

class Feature:
    """Contains Geometry (Strong HAS-A)."""
    def __init__(self, fid: int, coords: list):
        self.fid = fid
        self.geometry = Geometry(coords) 

class Layer:
    """Collection of Features."""
    def __init__(self, name: str):
        self.name = name
        self.features = []

    def add_feature(self, feat: Feature):
        self.features.append(feat)

class MapProject:
    """Contains Layers (Weak HAS-A)."""
    def __init__(self, title: str):
        self.title = title
        self.layers = [] 

    def add_layer(self, layer: Layer):
        self.layers.append(layer)


my_map = MapProject("City Map")
road_layer = Layer("Roads")
road_layer.add_feature(Feature(1, [[0, 0], [1, 1]]))

my_map.add_layer(road_layer)
print(f"Project '{my_map.title}' has {len(my_map.layers)} layer(s).")