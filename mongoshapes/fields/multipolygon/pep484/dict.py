#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union, Sequence, Dict


MultiPolygonGeometry = Sequence[Sequence[Sequence[Sequence[float]]]]
MultiPolygonValues = Union[str, MultiPolygonGeometry]
MultiPolygonDict = Dict[str, MultiPolygonValues]
