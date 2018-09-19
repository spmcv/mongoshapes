#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union
from typing import Dict
from typing import Sequence as Seq

Geometry = Seq[float]
StrOrGeo = Union[str, Geometry]
GeoDict = Dict[str, StrOrGeo]
