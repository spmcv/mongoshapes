#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import ShapelyField
from .pep484 import *


class MultiLineStringField(ShapelyField):
    """
    Substitution for :class:`mongoengine.MultiLineStringField`
    utilizing :class:`MultiLineString` geometry type.

    Instead of storing GeoJSON-like mapping as a value, a
    `shapely`__ geometry instance is used instead via
    the `__geo_interface__`__ protocol.

    __ https://shapely.readthedocs.io/en/stable/
    __ https://gist.github.com/zzpwelkin/2279867
    """

    @property
    def shape(self) -> MultiLineStringType:
        return MultiLineString

    def validate(self, value: MultiLineString):
        super(MultiLineStringField, self).validate(value)

    def to_mongo(self, value: MultiLineString) -> MultiLineStringDict:
        return super(MultiLineStringField, self).to_mongo(value)

    def to_python(self, value: MultiLineStringDict) -> MultiLineString:
        return super(MultiLineStringField, self).to_python(value)
