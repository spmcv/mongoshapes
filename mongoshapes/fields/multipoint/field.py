#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import ShapelyField
from .pep484 import *


class MultiPointField(ShapelyField):
    """
    Substitution for :class:`mongoengine.MultiPointField`
    utilizing :class:`MultiPoint` geometry type.

    Instead of storing GeoJSON-like mapping as a value, a
    `shapely`__ geometry instance is used instead via
    the `__geo_interface__`__ protocol.

    __ https://shapely.readthedocs.io/en/stable/
    __ https://gist.github.com/zzpwelkin/2279867
    """

    @property
    def shape(self) -> MultiPointType:
        return MultiPoint

    def validate(self, value: MultiPoint):
        super(MultiPointField, self).validate(value)

    def to_mongo(self, value: MultiPoint) -> MultiPointDict:
        return super(MultiPointField, self).to_mongo(value)

    def to_python(self, value: MultiPointDict) -> MultiPoint:
        return super(MultiPointField, self).to_python(value)
