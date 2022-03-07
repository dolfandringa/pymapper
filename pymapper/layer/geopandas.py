"""
Define the GeoPandasLayer.
"""
from geopandas import GeoDataFrame
from pyproj.crs.crs import CRS
from .base import BaseLayer


class GeoPandasLayer(BaseLayer):  # pylint: disable=R0903
    """Vector layer based on :class:`geopandas.GeoDataFrame`.

    Args:
        name (str): "The layer name."
        data (:class:`geopandas.GeoDataFrame`): The data to use.

    Attributes:
        name (str): "The layer name."
        data (:class:`geopandas.GeoDataFrame`): The data for the layer. The data
            may be modified in-place, so pass a copy if you don't want that.
    """

    LAYER_TYPE = "GeoPandasLayer"

    def __init__(self, name: str, data: GeoDataFrame):
        """Initilize the class."""
        self.data: GeoDataFrame = data
        minx, miny, maxx, maxy = data.total_bounds
        super().__init__(name, crs=data.crs, bbox=(minx, miny, maxx, maxy))

    def set_crs(self, crs: CRS):
        """Reproject the dataframe to a new CRS."""
        self.crs = crs
        self.data.to_crs(crs, inplace=True)
        minx, miny, maxx, maxy = self.data.total_bounds
        self.bbox = (minx, miny, maxx, maxy)

    def render(self):
        """Render the layer."""
