from pytest import approx
from cairo import Matrix
from pymapper import ImageTransformation


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


def test_equality(transformation):
    """Test object equality."""
    _, _, _, bbox, width, height, marginx, marginy = transformation
    trans = ImageTransformation(bbox, width, height, marginx, marginy)
    trans2 = ImageTransformation(bbox, width, height, marginx, marginy)
    assert trans == trans2


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
