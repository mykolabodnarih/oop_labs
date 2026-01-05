class SpatialObject:
    """Abstract spatial object."""
    def draw(self) -> str:
        """Method for polymorphism."""
        return "Drawing base object"

class PointObject(SpatialObject):
    """Point geometry."""
    def draw(self) -> str:
        return "Drawing a point at [x, y]"

class LineObject(SpatialObject):
    """Line geometry."""
    def draw(self) -> str:
        return "Drawing a line between points"

class Annotation:
    """Duck typing example."""
    def draw(self) -> str:
        return "Drawing text annotation"

def render(obj):
    """Dynamic polymorphism handler."""
    print(obj.draw())


geometries = [PointObject(), LineObject()]
for geo in geometries:
    render(geo)


render(Annotation())