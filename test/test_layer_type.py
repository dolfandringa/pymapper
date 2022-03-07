from pymapper.layer import LayerType, GeoPandasLayer


def test_layer_types():
    """Test the LayerType enum."""
    assert list(LayerType.__members__.keys()) == [GeoPandasLayer.LAYER_TYPE]
    assert LayerType[GeoPandasLayer.LAYER_TYPE].value == GeoPandasLayer
