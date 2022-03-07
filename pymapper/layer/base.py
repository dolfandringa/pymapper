"""Defines the BaseLayer."""
from typing import Union, Tuple
from pyproj.crs.crs import CRS


class BaseLayer:  # pylint: disable=R0903
    """Base layer.

    Attributes:
        name (str): The layer name
        crs (pyproj.crs.crs.CRS): The layer coordinate reference system.
        bbox (Type[float, float, float, float]: (minx, miny, maxx, maxy) bounding box
    """
    LAYER_TYPE: Union[str, None] = None

    def __init__(self, name: str, crs: Union[CRS, None],
                 bbox: Tuple[float, float, float, float]):
        """Initialize the class."""
        self.name = name
        self.crs = crs
        self.bbox = bbox

        if self.__class__.LAYER_TYPE is None:
            raise NotImplementedError("Please subclass BaseLayer")

    def set_crs(self, crs: CRS):
        """Set the layer crs."""
        self.crs = crs
        raise NotImplementedError(f"Please implement {self.__class__}.set_crs")
