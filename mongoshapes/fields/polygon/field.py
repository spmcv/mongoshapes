#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import ShapelyField
from .pep484 import *


class PolygonField(ShapelyField):
    """
    Substitution for :class:`mongoengine.PolygonField`
    utilizing :class:`Polygon` geometry type.

    Instead of storing GeoJSON-like mapping as a value, a
    `shapely`__ geometry instance is used instead via
    the `__geo_interface__`__ protocol.

    __ https://shapely.readthedocs.io/en/stable/
    __ https://gist.github.com/zzpwelkin/2279867
    """

    @property
    def shape(self) -> PolygonType:
        return Polygon

    def validate(self, value: Polygon):
        super(PolygonField, self).validate(value)

    def to_mongo(self, value: Polygon) -> PolygonDict:
        return super(PolygonField, self).to_mongo(value)

    def to_python(self, value: PolygonDict) -> Polygon:
        return super(PolygonField, self).to_python(value)
