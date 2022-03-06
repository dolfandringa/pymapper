# noqa
# pylint: disable=W0622,C0114,C0103
# Configuration file for the Sphinx documentation builder.
#
# This file only contains a selection of the most common options. For a full
# list see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Path setup --------------------------------------------------------------

# If extensions (or modules to document with autodoc) are in another directory,
# add these directories to sys.path here. If the directory is relative to the
# documentation root, use os.path.abspath to make it absolute, like shown here.
#
import os

# import sys
# sys.path.insert(0, os.path.abspath('.'))
on_rtd = os.environ.get("READTHEDOCS") == "True"

# -- Project information -----------------------------------------------------

project = "pymapper"
copyright = "2022, Dolf Andringa"
author = "Dolf Andringa"

napoleon_google_docstring = True
napoleon_numpy_docstring = True
napoleon_include_private_with_doc = True
napoleon_include_special_with_doc = True
autoclass_content = "class"
autodoc_member_order = "bysource"
autodoc_default_flags = ["members"]
extensions = [
    "sphinx.ext.autodoc",
    "sphinx.ext.intersphinx",
    "sphinx.ext.viewcode",
    "sphinx.ext.napoleon",
    "myst_parser",
]
html_context = {}
html_sidebars = {
    "**": ["localtoc.html", "relations.html", "searchbox.html"],
}

intersphinx_mapping = {
    "cairo": (
        "https://pycairo.readthedocs.io/en/stable",
        "https://pycairo.readthedocs.io/en/stable/objects.inv",
    ),
    "geopandas": (
        "https://geopandas.org/en/stable",
        "https://geopandas.org/en/stable/objects.inv",
    ),
    "geopy": (
        "https://geopy.readthedocs.io/en/stable/",
        "https://geopy.readthedocs.io/en/stable/objects.inv",
    ),
    "mapclassify": (
        "https://pysal.org/mapclassify/",
        "https://pysal.org/mapclassify/objects.inv",
    ),
    "matplotlib": (
        "https://matplotlib.org/stable/",
        "https://matplotlib.org/stable/objects.inv",
    ),
    "owslib": (
        "https://geopython.github.io/OWSLib/",
        "https://geopython.github.io/OWSLib/objects.inv",
    ),
    "pyepsg": (
        "https://pyepsg.readthedocs.io/en/stable/",
        "https://pyepsg.readthedocs.io/en/stable/objects.inv",
    ),
    "pygeos": (
        "https://pygeos.readthedocs.io/en/latest/",
        "https://pygeos.readthedocs.io/en/latest/objects.inv",
    ),
    "pyproj": (
        "https://pyproj4.github.io/pyproj/stable/",
        "https://pyproj4.github.io/pyproj/stable/objects.inv",
    ),
    "python": (
        "https://docs.python.org/3",
        "https://docs.python.org/3/objects.inv",
    ),
    "rtree": (
        "https://rtree.readthedocs.io/en/stable/",
        "https://rtree.readthedocs.io/en/stable/objects.inv",
    ),
    "rasterio": (
        "https://rasterio.readthedocs.io/en/stable/",
        "https://rasterio.readthedocs.io/en/stable/objects.inv",
    ),
    "shapely": (
        "https://shapely.readthedocs.io/en/stable/",
        "https://shapely.readthedocs.io/en/stable/objects.inv",
    ),
}

# Add any paths that contain templates here, relative to this directory.
templates_path = ["_templates"]

# List of patterns, relative to source directory, that match files and
# directories to ignore when looking for source files.
# This pattern also affects html_static_path and html_extra_path.
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]


# -- Options for HTML output -------------------------------------------------

# The theme to use for HTML and HTML Help pages.  See the documentation for
# a list of builtin themes.
#
if on_rtd:
    html_theme = "default"
else:
    html_theme = "sphinx_rtd_theme"

# Add any paths that contain custom static files (such as style sheets) here,
# relative to this directory. They are copied after the builtin static files,
# so a file named "default.css" will overwrite the builtin "default.css".
html_static_path = ["_static"]
