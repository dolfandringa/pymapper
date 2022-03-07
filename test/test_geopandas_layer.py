from pyproj.crs.crs import CRS
from pyproj.transformer import Transformer
from shapely.ops import transform
from pymapper.layer import GeoPandasLayer


def test_create_geopandas_layer(gpdata):
    """Test instantiating a GeoPandasLayer."""
    lyr = GeoPandasLayer(name="test", data=gpdata)
    assert lyr.name == "test"
    assert lyr.crs == gpdata.crs
    assert lyr.data is gpdata
    assert all(lyr.bbox[i] == val for i, val in enumerate(gpdata.total_bounds))


def test_set_crs(gpdata):
    """Test reprojecting the layer."""
    lyr: GeoPandasLayer = GeoPandasLayer(name="test", data=gpdata)
    new_crs = CRS.from_epsg(3857)
    old_crs = lyr.crs
    old_geom = gpdata.iloc[0].geometry
    if old_crs == new_crs:
        new_crs = CRS.from_epsg(4326)
    transformer: Transformer = Transformer.from_crs(old_crs, new_crs)
    lyr.set_crs(new_crs)
    new_geom = lyr.data.iloc[0].geometry
    assert (
        transform(lambda x, y: transformer.transform(y, x), old_geom).wkt
        == new_geom.wkt
    )
    assert all(lyr.bbox[i] == val for i, val in enumerate(lyr.data.total_bounds))
