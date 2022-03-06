from pytest import fixture


@fixture
def transformation():  # pylint: disable=R0914
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


@fixture
def transformation_port():  # pylint: disable=R0914
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
