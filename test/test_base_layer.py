from pyproj.crs.crs import CRS
import pytest
from pymapper.layer.base import BaseLayer


def test_raises_not_implemented_error():
    """Test that a BaseLayer raises NotImplementedError of LAYER_TYPE is not set."""
    with pytest.raises(NotImplementedError):
        BaseLayer(name="test", crs=None, bbox=(0, 0, 0, 0))


def test_set_crs_raises_not_implemented_error():
    """Test that BaseLayer.set_crs raises NotImplementedError."""
    BaseLayer.LAYER_TYPE = "test"
    crs = CRS.from_epsg(4326)
    lyr = BaseLayer(name="test", crs=crs, bbox=(0, 0, 10, 10))
    with pytest.raises(NotImplementedError):
        lyr.set_crs(CRS.from_epsg(4326))


def test_instantiation():
    """Test instantiating a BaseLayer"""
    BaseLayer.LAYER_TYPE = "test"
    crs = CRS.from_epsg(4326)
    lyr = BaseLayer(name="test", crs=crs, bbox=(0, 0, 10, 10))
    assert lyr.name == "test"
    assert lyr.crs == crs
    assert lyr.bbox == (0, 0, 10, 10)
