#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union
from typing import Dict
from typing import Sequence as Seq

from mongoshapes.fields.abstract import AnyGeoDict

Geometries = Seq[AnyGeoDict]
StrOrGeo = Union[str, Geometries]
GeoDict = Dict[str, StrOrGeo]
