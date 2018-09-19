#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import ShapelyField
from .pep484 import *


class LineStringField(ShapelyField):
    """
    Substitution for :class:`mongoengine.LineStringField`
    utilizing :class:`LineString` geometry type.

    Instead of storing GeoJSON-like mapping as a value, a
    `shapely`__ geometry instance is used instead via
    the `__geo_interface__`__ protocol.

    __ https://shapely.readthedocs.io/en/stable/
    __ https://gist.github.com/zzpwelkin/2279867
    """

    @property
    def shape(self) -> LineStringType:
        return LineString

    def validate(self, value: LineString):
        super(LineStringField, self).validate(value)

    def to_mongo(self, value: LineString) -> LineStringDict:
        return super(LineStringField, self).to_mongo(value)

    def to_python(self, value: LineStringDict) -> LineString:
        return super(LineStringField, self).to_python(value)
