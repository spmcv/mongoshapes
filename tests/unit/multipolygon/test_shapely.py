#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from shapely.geometry import shape, mapping

from . import *


@pytest.fixture
def geometry(geointerface: GeoDict) -> GeoShape:
    """
    Convert the GeoJSON fixture into an appropriate geometry.

    :param geointerface: GeoJSON mapping
    :return: geometry instance
    """
    return shape(geointerface)


def test_mapping(geointerface: GeoDict, geometry: GeoShape):
    """
    Test that mapped value matches original

    :param geointerface: GeoJSON mapping
    :param geometry:  geometry instance
    """
    mapped = mapping(geometry)
    assert mapped == geointerface, "{:s} failed".format(GeoShape.__name__)


@pytest.mark.xfail(
    raises=AssertionError,
    reason="non-zero area intersection of polygons"
)
def test_validation(geometry: GeoShape):
    """
    Test that mapped value matches original

    :param geometry:  geometry instance
    """
    assert geometry.is_valid, "failed OpenGIS validation"
