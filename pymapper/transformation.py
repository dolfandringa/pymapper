import cairo


class ImageTransformation:  # pylint: disable=R0902
    """A class holding the parameters for a transformation matrix for an affine
    transformation with attributes xx, xy, x0, yx, yy and y0 such that
    ::

        x_new = xx * x + xy * y + x0
        y_new = yx * x + yy * y + y0

    The transformation is used to transform any coordinate system into the canonical
    coordinate system for a target map image. The target image has ``width`` and
    ``height`` in pixels, and is assumed to have its origin (0,0) at the top left.

    The ``extentx`` and ``extenty`` are calculated to first add respectively ``marginx``
    and ``marginy`` and then one of the extents is expanded so the final extents match
    the ``width/height`` ratio of the image. The actual bounding box (``bbox``) is then
    based on these extents.

    Args:
        bbox (tuple): The bounding box in the format (minx, miny, maxx, maxy)
            of the input data.
        width (int): The width in pixels of the target image
        height (int): The height in pixels of the target image
        marginx (float): A margin in the x direction (between 0 and 1) to give to
            the image around the data (default 0.2)
        marginy (float): A margin in the y direction (between 0 and 1) to give to
            the image around the data (default 0.2)

    Attributes:
        xx (float): cairo `xx` parameter, or shapely `a` parameter
        xy (float): cairo `xy` parameter, or shapely `b` parameter
        x0 (float): cairo `x0` parameter, or shapely `xoff` parameter
        yx (float): cairo `yx` parameter, or shapely `d` parameter
        yy (float): cairo `yy` parameter, or shapely `e` parameter
        y0 (float): cairo `y0` parameter, or shapely `yoff` parameter
        extentx (float): the map x extent in user coordinate space after adding
            ``marginx`` and adjusting for the width/height ratio of the image.
        extenty (float): the map y extent in user coordinate space after adding
            ``marginy`` and adjusting for the width/height ratio of the image.
        bbox (tuple): (xmin,ymin,xmax,ymax) tuple for the map extent
            in user coordinate space. This is the actual bbox based on ``extentx`` and
            ``extenty``
        width (int): Image width in pixels
        height (int): Image height in pixels

    """

    def __init__(  # pylint: disable=C0103,R0913,R0914
        self, bbox, width, height, marginx=0.2, marginy=0.2
    ):
        """Initialize the class."""
        minx, miny, maxx, maxy = bbox

        hratio = height / width
        vratio = width / height
        offsetx = (maxx - minx) * marginx
        offsety = (maxy - miny) * marginy
        extentx = maxx - minx + offsetx * 2
        extenty = maxy - miny + offsety * 2
        if extentx * hratio > extenty:
            new_extenty = extentx * hratio
            offsety += (new_extenty - extenty) / 2
            extenty = new_extenty
        else:
            new_extentx = extenty * vratio
            offsetx += (new_extentx - extentx) / 2
            extentx = new_extentx
        scalex = width / extentx
        scaley = height / extenty
        originx = minx - offsetx
        originy = miny - offsety
        bbox = ((originx, originy, originx + extentx, originy + extenty),)

        xx = scalex
        xy = 0
        x0 = -originx * scalex
        yx = 0
        yy = -scaley
        y0 = originy * scaley + height

        self.xx = xx  # pylint: disable=C0103
        self.xy = xy  # pylint: disable=C0103
        self.x0 = x0  # pylint: disable=C0103
        self.yx = yx  # pylint: disable=C0103
        self.yy = yy  # pylint: disable=C0103
        self.y0 = y0  # pylint: disable=C0103
        self.extentx = extentx
        self.extenty = extenty
        self.bbox = bbox
        self.width = width
        self.height = height

    def get_cairo_matrix(self):
        """Get :class:`cairo.Matrix` version of this transformation.

        Returns:
            cairo.Matrix: keys are ``xx``, ``xy``, ``x0``, ``yx``, ``yy`` and ``y0``
        """
        return cairo.Matrix(
            xx=self.xx,
            xy=self.xy,
            x0=self.x0,
            yx=self.yx,
            yy=self.yy,
            y0=self.y0,
        )

    def __eq__(self, other):
        """Test equality."""
        keys = {
            "xx", "xy", "x0", "yx", "yy", "y0", "extentx", "extenty", "width", "height"
            }
        return all(getattr(self, key) == getattr(other, key) for key in keys)

    def get_shapely_matrix(self):
        """Get arguments for :func:`shapely.affinity.affine_transform`
        `matrix` argument.

        Returns:
            list: [``self.xx``, ``self.xy``, ``self.yx``, ``self.yy``, ``self.x0``,
            ``self.y0``]
        """
        return [
            self.xx,
            self.xy,
            self.yx,
            self.yy,
            self.x0,
            self.y0,
        ]
