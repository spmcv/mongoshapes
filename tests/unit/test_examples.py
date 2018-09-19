#!/usr/bin/env python
# -*- coding: utf-8 -*


import pytest
import shapely.geometry as geo


GEOMETRIES = [
    pytest.param(
        geo.LineString(
            [(0, 0), (1, 1), (0, 2), (2, 2), (3, 1), (1, 0)]
        ),
        id="a simple line"
    ),
    pytest.param(
        geo.LineString(
            [(0, 0), (1, 1), (0, 2), (2, 2), (-1, 1), (1, 0)]
        ),
        id="a complex line"
    ),
    pytest.param(
        geo.LineString(
            [(0, 0, 0), (0, 0, 1)]
        ),
        id="a LineString of unit length in z-axis",
        marks=pytest.mark.xfail(
            AssertionError,
            reason="LineString needs non-zero length in xy"
        )
    ),
    pytest.param(
        geo.LinearRing(
            [(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (1, 0.8), (0, 0)]
        ),
        id="a valid LinearRing",
    ),
    pytest.param(
        geo.LinearRing(
            [(0, 0), (0, 2), (1, 1), (2, 2), (2, 0), (1, 1), (0, 0)]
        ),
        id="a self-touching LinearRing",
        marks=pytest.mark.xfail(
            AssertionError,
            reason="LinearRing touches itself at a point"
        )
    ),
    pytest.param(
        geo.Polygon(
            [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)],
            [[(1, 0), (0.5, 0.5), (1, 1), (1.5, 0.5), (1, 0)][::-1]]
        ),
        id="a Polygon touching exterior ring at single point"
    ),
    pytest.param(
        geo.Polygon(
            [(0, 0), (0, 2), (2, 2), (2, 0), (0, 0)],
            [[(1, 0), (0, 1), (0.5, 1.5), (1.5, 0.5), (1, 0)][::-1]]
        ),
        id="a Polygon touching exterior ring at two points",
        marks=pytest.mark.xfail(
            AssertionError,
            reason="Polygon may touch at a single point only"
        )
    ),
    pytest.param(
        geo.Polygon(
            [(0, 0, 0), (0, 0, 1), (1, 1, 1)]
        ),
        id="a Polygon not bounded by a closed ring",
        marks=pytest.mark.xfail(
            AssertionError,
            reason="Polygon needs closed ring boundary"
        )
    ),
    pytest.param(
        geo.MultiPolygon(
            [
                [[(0, 0), (0, 1), (1, 1), (1, 0), (0, 0)], []],
                [[(1, 1), (1, 2), (2, 2), (2, 1), (1, 1)], []]
            ]
        ),
        id="a MultiPolygon sharing a point",
    ),
    pytest.param(
        geo.MultiPolygon(
            [
                [[(0, 0), (0, 1.5), (1, 1.5), (1, 0), (0, 0)], []],
                [[(1, 0.5), (1, 2), (2, 2), (2, 0.5), (1, 0.5)], []]
            ]
        ),
        id="a MultiPolygon sharing a side",
        marks=pytest.mark.xfail(
            AssertionError,
            reason="MultiPolygon may intersect only at points"
        )
    )
]


@pytest.mark.parametrize('value', GEOMETRIES)
def test_geometry_is_valid(value: geo.base.BaseGeometry):
    assert value.is_valid, "shape failed OpenGIS validation"
