from pytest import fixture, approx
from cairo import Matrix
from pymapper import ImageTransformation


@fixture(name="transformation")
def fixture_transformation():  # pylint: disable=R0914
    """Transformation fixture providing calculated matrix, extentx and extenty based on
    bbox, width, height, marginx and marginy.

    Returns:
        tuple: matrix, extentx, extenty, bbox, width, height, marginx, marginy
    """
    bbox = (2150, 2015, 5000, 3500)
    minx, miny, maxx, maxy = bbox
    width = 1000
    height = 500
    marginx = marginy = 0.2
    extenty = (maxy - miny)*(1+marginx*2)
    extentx = extenty*2
    orig_extentx = (maxx - minx)*(1+marginx*2)
    offsetx = (maxx-minx)*marginx+(extentx-orig_extentx)/2
    scalex = width/extentx
    scaley = height/extenty
    x0 = -(minx - offsetx)*scalex  # pylint: disable=C0103
    y0 = (miny-(maxy-miny)*marginy) * scaley+height  # pylint: disable=C0103
    matrix = (width/extentx, 0, x0, 0, -height/extenty, y0)
    return (matrix, extentx, extenty, bbox, width, height, marginx, marginy)


@fixture(name="transformation_port")
def fixture_transformation_port():  # pylint: disable=R0914
    """Transformation fixture providing calculated matrix, extentx and extenty based on
    bbox, width, height, marginx and marginy. This is a portrait image.

    Returns:
        tuple: matrix, extentx, extenty, bbox, width, height, marginx, marginy
    """
    bbox = (2150, 2015, 5000, 3500)
    minx, miny, maxx, maxy = bbox
    width = 500
    height = 1000
    marginx = marginy = 0.2
    extentx = (maxx - minx)*(1+marginx*2)
    extenty = extentx*2
    orig_extenty = (maxy - miny)*(1+marginy*2)
    offsety = (maxy-miny)*marginy+(extenty-orig_extenty)/2
    scalex = width/extentx
    scaley = height/extenty
    y0 = (miny - offsety)*scaley+height  # pylint: disable=C0103
    x0 = -(minx-(maxx-minx)*marginx) * scalex  # pylint: disable=C0103
    matrix = (width/extentx, 0, x0, 0, -height/extenty, y0)
    return (matrix, extentx, extenty, bbox, width, height, marginx, marginy)


def test_create_transformation(transformation):  # pylint: disable=R0914
    """Test ImageTransformation.get_cairo_matrix."""
    matrix, extentx, extenty, bbox, width, height, marginx, marginy = transformation
    xx, xy, x0, yx, yy, y0 = matrix  # pylint: disable=C0103
    trans = ImageTransformation(bbox, width, height, marginx, marginy)
    assert trans.xx == xx
    assert trans.xy == xy
    assert trans.x0 == approx(x0)
    assert trans.yx == yx
    assert trans.yy == yy
    assert trans.y0 == y0
    assert trans.extentx == extentx
    assert trans.extenty == extenty


def test_create_transformation_portrait(transformation_port):  # pylint: disable=R0914
    """Test ImageTransformation.get_cairo_matrix."""
    (matrix, extentx, extenty, bbox, width, height,
     marginx, marginy) = transformation_port
    xx, xy, x0, yx, yy, y0 = matrix  # pylint: disable=C0103
    trans = ImageTransformation(bbox, width, height, marginx, marginy)
    assert trans.xx == approx(xx)
    assert trans.xy == xy
    assert trans.x0 == approx(x0)
    assert trans.yx == yx
    assert trans.yy == approx(yy)
    assert trans.y0 == approx(y0)
    assert trans.extentx == approx(extentx)
    assert trans.extenty == approx(extenty)


def test_get_cairo_matrix(transformation):  # pylint: disable=R0914
    """Test ImageTransformation.get_cairo_matrix."""
    matrix, _, _, bbox, width, height, marginx , marginy = transformation
    xx, xy, x0, yx, yy, y0 = matrix  # pylint: disable=C0103
    trans = ImageTransformation(bbox, width, height, marginx, marginy)
    actual = trans.get_cairo_matrix()
    expected = Matrix(xx=xx, xy=xy, x0=x0, yx=yx, yy=yy, y0=y0)
    assert expected.xx == actual.xx
    assert expected.xy == actual.xy
    assert expected.x0 == approx(actual.x0)
    assert expected.yx == actual.yx
    assert expected.yy == actual.yy
    assert expected.y0 == approx(actual.y0)


def test_shapely_matrix(transformation):  # pylint: disable=R0914
    """Test ImageTransformation.get_shapely_matrix."""
    matrix, _, _, bbox, width, height, marginx , marginy = transformation
    xx, xy, x0, yx, yy, y0 = matrix  # pylint: disable=C0103
    trans = ImageTransformation(bbox, width, height, marginx, marginy)
    actual = trans.get_shapely_matrix()
    assert actual == [xx, xy, yx, yy, approx(x0), approx(y0)]
