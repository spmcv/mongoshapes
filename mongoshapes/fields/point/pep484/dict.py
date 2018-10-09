#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union, Sequence, Dict


PointGeometry = Sequence[float]
PointValues = Union[str, PointGeometry]
PointDict = Dict[str, PointValues]
