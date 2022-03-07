from pyproj.crs.crs import CRS
from pymapper import Map, ImageTransformation, GeoPandasLayer


def test_has_transformation(transformation):
    """Test that the map has a transformation after instantiating."""
    _, _, _, bbox, width, height, _, _ = transformation
    _map = Map(width, height, "epsg:3857", bbox=bbox)
    expected = ImageTransformation(bbox, width, height)
    assert _map.transformation == expected


def test_map_crs():
    """Test that the map has a pyproj crs."""
    _map = Map(1024, 768, crs="epsg:3857")
    assert _map.crs == CRS.from_epsg(3857)


def test_add_layer_resets_bbox(gpdata):
    """Test that adding a layer, by default resets the bounding box."""
    _map = Map(1024, 768, crs=gpdata.crs)
    assert _map.bbox is None
    lyr = GeoPandasLayer(name="test{", data=gpdata)
    minx, miny, maxx, maxy = gpdata.total_bounds
    _map.bbox = (minx+5, miny+5, maxx-5, maxy+10)
    _map.add_layer(lyr)
    expected_bbox = list(gpdata.total_bounds)
    expected_bbox[3] = maxy+10
    assert all(_map.bbox[i] == val for i, val in enumerate(expected_bbox))
