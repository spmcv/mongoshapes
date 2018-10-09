#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union, Sequence, Dict


PolygonGeometry = Sequence[Sequence[Sequence[float]]]
PolygonValues = Union[str, PolygonGeometry]
PolygonDict = Dict[str, PolygonValues]
