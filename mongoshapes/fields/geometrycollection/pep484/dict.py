#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union, Sequence, Dict


from mongoshapes.fields.abstract import AnyGeometryDict

GeometryCollectionGeometry = Sequence[AnyGeometryDict]
GeometryCollectionValues = Union[str, GeometryCollectionGeometry]
GeometryCollectionDict = Dict[str, GeometryCollectionValues]
