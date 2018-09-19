#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union
from typing import Sequence as Seq
from typing import Dict


Any = Union[
    # Note Point
    Seq[float],
    Seq[Seq[float]],  # LineString, MultiPoint
    Seq[Seq[Seq[float]]],  # MultiLineString, Polygon
    Seq[Seq[Seq[Seq[float]]]]  # MultiPolygon
]

StrOrAny = Union[str, Any]
GeoDict = Dict[str, StrOrAny]
