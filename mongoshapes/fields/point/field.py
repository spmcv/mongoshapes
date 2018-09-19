#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import ShapelyField
from .pep484 import *


class PointField(ShapelyField):
    """
    Substitution for :class:`mongoengine.PointField`
    utilizing :class:`Point` geometry type.

    Instead of storing GeoJSON-like mapping as a value, a
    `shapely`__ geometry instance is used instead via
    the `__geo_interface__`__ protocol.

    __ https://shapely.readthedocs.io/en/stable/
    __ https://gist.github.com/zzpwelkin/2279867
    """

    @property
    def shape(self) -> PointType:
        return Point

    def validate(self, value: Point):
        super(PointField, self).validate(value)

    def to_mongo(self, value: Point) -> PointDict:
        return super(PointField, self).to_mongo(value)

    def to_python(self, value: PointDict) -> Point:
        return super(PointField, self).to_python(value)
