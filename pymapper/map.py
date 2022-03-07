"""
Contains the base map class.
"""
from .transformation import ImageTransformation


class Map:
    """The map is the basic class governing map generation.

    Args:
        width (int): The width of the map in pixels/
        height (int): The height of the map in pixels.
        crs (pyproj.crs.crs.CRS): The map coordinate reference system.

    Attributes:
        width (int): The width of the map in pixels.
        height (int): The height of the map in pixels.
        transformation (ImageTransformation): The image transformation instrance.
        crs (pyproj.crs.crs.CRS): The map coordinate reference system.
        layers (list): Layers for the map.

    """
    def __init__(self, width, height, crs, bbox=None):
        """Initialize the class."""
        self.crs = crs
        self.width = width
        self.height = height
        self.bbox = bbox
        self.transformation = None
        self.layers = []
        if self.bbox is not None:
            self._update_transformation()

    def _update_transformation(self):
        """Updates the image transformation."""
        self.transformation = ImageTransformation(self.bbox, self.width, self.height)

    def add_layer(self, layer):
        """Add a layert to the map."""
        layer.set_crs(self.crs)
        self.layers.append(layer)
        bbox = layer.bbox
        if self.bbox is not None:
            minx, miny, maxx, maxy = self.bbox
            lminx, lminy, lmaxx, lmaxy = layer.bbox
            bbox = (min(minx, lminx), min(miny, lminy),
                    max(maxx, lmaxx), max(maxy, lmaxy))
        self.bbox = bbox

    def render(self, file):
        """Render the map."""
