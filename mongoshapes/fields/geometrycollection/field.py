#!/usr/bin/env python
# -*- coding: utf-8 -*-

from .. import ShapelyField

from .pep484 import *


class GeometryCollectionField(ShapelyField):
    """
    No equivalent subclass of :class:`mongoengine.GeoJsonBaseField`
    exits for :class:`GeometryCollection` geometry type.

    Instead of storing GeoJSON-like mapping as a value, a
    `shapely`__ geometry instance is used instead via
    the `__geo_interface__`__ protocol.

    __ https://shapely.readthedocs.io/en/stable/
    __ https://gist.github.com/zzpwelkin/2279867
    """

    @property
    def shape(self) -> GeometryCollectionType:
        return GeometryCollection

    def validate(self, value: GeometryCollection):
        super(GeometryCollectionField, self).validate(value)

    def to_mongo(self, value: GeometryCollection) -> GeometryCollectionDict:
        return super(GeometryCollectionField, self).to_mongo(value)

    def to_python(self, value: GeometryCollectionDict) -> GeometryCollection:
        return super(GeometryCollectionField, self).to_python(value)
