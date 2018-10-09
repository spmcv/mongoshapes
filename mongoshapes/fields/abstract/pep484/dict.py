#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union, Sequence, Dict


AnyGeometryGeometry = Union[
    # Note Point
    Sequence[float],
    Sequence[Sequence[float]],  # LineString, MultiPoint
    Sequence[Sequence[Sequence[float]]],  # MultiLineString, Polygon
    Sequence[Sequence[Sequence[Sequence[float]]]]  # MultiPolygon
]

AnyGeometryValues = Union[str, AnyGeometryGeometry]
AnyGeometryDict = Dict[str, AnyGeometryValues]
