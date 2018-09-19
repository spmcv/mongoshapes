#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import ShapelyField
from .pep484 import *


class MultiPolygonField(ShapelyField):
    """
    Substitution for :class:`mongoengine.MultiPolygonField`
    utilizing :class:`MultiPolygon` geometry type.

    Instead of storing GeoJSON-like mapping as a value, a
    `shapely`__ geometry instance is used instead via
    the `__geo_interface__`__ protocol.

    __ https://shapely.readthedocs.io/en/stable/
    __ https://gist.github.com/zzpwelkin/2279867
    """

    @property
    def shape(self) -> MultiPolygonType:
        return MultiPolygon

    def validate(self, value: MultiPolygon):
        super(MultiPolygonField, self).validate(value)

    def to_mongo(self, value: MultiPolygon) -> MultiPolygonDict:
        return super(MultiPolygonField, self).to_mongo(value)

    def to_python(self, value: MultiPolygonDict) -> MultiPolygon:
        return super(MultiPolygonField, self).to_python(value)
