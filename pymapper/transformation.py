import cairo


class ImageTransformation:  # pylint: disable=R0902
    """A class holding the parameters for a transformation matrix for an affine
    transformation with attributes xx, xy, x0, yx, yy and y0 such that
    ::

        x_new = xx * x + xy * y + x0
        y_new = yx * x + yy * y + y0

    Attributes:
        xx (float): cairo `xx` parameter, or shapely `a` parameter
        xy (float): cairo `xy` parameter, or shapely `b` parameter
        x0 (float): cairo `x0` parameter, or shapely `xoff` parameter
        yx (float): cairo `yx` parameter, or shapely `d` parameter
        yy (float): cairo `yy` parameter, or shapely `e` parameter
        y0 (float): cairo `y0` parameter, or shapely `yoff` parameter
        extentx (float): the map x extent in user coordinate space
        extenty (float): the map y extent in user coordinate space
        bbox (tuple): (xmin,ymin,xmax,ymax) tuple for the map extent
            in user coordinate space

    """

    def __init__(  # pylint: disable=C0103,R0913
        self,
        xx: float,
        xy: float,
        x0: float,
        yx: float,
        yy: float,
        y0: float,
        extentx: float,
        extenty: float,
        bbox: tuple,
    ):
        """Initialize the class.

        Args:
            The class attributes to initialize

        """
        self.xx = xx  # pylint: disable=C0103
        self.xy = xy  # pylint: disable=C0103
        self.x0 = x0  # pylint: disable=C0103
        self.yx = yx  # pylint: disable=C0103
        self.yy = yy  # pylint: disable=C0103
        self.y0 = y0  # pylint: disable=C0103
        self.extentx = extentx
        self.extenty = extenty
        self.bbox = bbox

    def get_cairo_matrix(self):
        """Get arguments for :class:`cairo.Matrix`

        Returns:
            cairo.Matrix: keys are xx, xy, x0, yx, yy and y0
        """
        return cairo.Matrix(
            xx=self.xx,
            xy=self.xy,
            x0=self.x0,
            yx=self.yx,
            yy=self.yy,
            y0=self.y0,
        )

    def get_shapely_matrix(self):
        """Get arguments for :func:`shapely.affinity.affine_transform`
        `matrix` argument.

        Returns:
            list: [a, b, d, e, xoff, yoff]
        """
        return [
            self.xx,
            self.xy,
            self.yx,
            self.yy,
            self.x0,
            self.y0,
        ]

    @staticmethod
    # pylint: disable=R0914
    def create_for_map(bbox, width, height, marginx=0.2, marginy=0.2):
        """Create a :class:`ImageTransformation` to map a coordinate system to the
        canonical coordinate system of a target map image. The target image is assumed
        to have the (0,0) origin at the top left.

        Args:
            bbox (tuple): The bounding box in the format (minx, miny, maxx, maxy)
                of the map.
            width (int): The width in pixels of the target image
            height (int): The height in pixels of the target image
            marginx (float): A margin in the x direction (between 0 and 1) to give to
                the image around the data
            marginy (float): A margin in the y direction (between 0 and 1) to give to
                the image around the data

        Returns:
            :class:`ImageTransformation`

        """
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
        return ImageTransformation(
            xx=scalex,
            xy=0,
            x0=-originx * scalex,
            yx=0,
            yy=-scaley,
            y0=originy * scaley + height,
            extentx=extentx,
            extenty=extenty,
            bbox=(originx, originy, originx + extentx, originy + extenty),
        )
