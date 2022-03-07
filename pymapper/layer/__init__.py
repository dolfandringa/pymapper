from enum import Enum
from .geopandas import GeoPandasLayer


LayerType = Enum(
        "LayerType",
        {GeoPandasLayer.LAYER_TYPE: GeoPandasLayer})
