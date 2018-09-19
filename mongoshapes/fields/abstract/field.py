#!/usr/bin/env python
# -*- coding: utf-8 -*-

import abc
import pymongo as pm
import mongoengine as me

from shapely.geometry import shape, mapping

from .pep484 import *


class ShapelyField(me.fields.BaseField, abc.ABC):
    """
    A substitution of :class:`me.fields.GeoJsonBaseField` that, instead of
    using GeoJSON-like dictionary, uses an appropriate Shapely geometry
    instance internally.

    The advantages of this are:

        - validation explicitly handled by Shapely, which conforms to
          `OpenGIS`__ specifications.

        - `__array_interface__`__ for numpy-interoperability

        - `__geo_interface__`__ for GeoJSON-interoperability

    __ http://www.opengeospatial.org/standards/sfa
    __ https://docs.scipy.org/doc/numpy/reference/arrays.interface.html
    __ https://gist.github.com/zzpwelkin/2279867
    """
    _geo_index = pm.GEOSPHERE

    @property
    @abc.abstractmethod
    def shape(self) -> AnyGeoType:
        pass

    def __init__(self, auto_index: bool=True, *args, **kwargs):
        """
        :param bool auto_index: automatically create a '2dsphere' index
        """
        if not auto_index:
            self._geo_index = False
        super(ShapelyField, self).__init__(*args, **kwargs)

    def validate(self, value: AnyGeo):
        """
        Validate the internal Shapely geometry.

        :param value: instance to validate
        """
        n = self.shape.__name__

        if not isinstance(value, self.shape):
            self.error("Value is not a {:s} type".format(n))

        if not value.is_valid:
            self.error("Value is not a valid {:s}".format(n))

    def to_python(self, value: AnyGeoDict) -> AnyGeo:
        """
        Utilize `__geo_interface__`__ protocol to deserialized from BSON.

        __ https://gist.github.com/zzpwelkin/2279867

        :param value: dict deserialized from BSON
        :return: Shapely geometry instance
        """
        return shape(value)

    def to_mongo(self, value: AnyGeo) -> AnyGeoDict:
        """
        Utilize `__geo_interface__`__ protocol to serialize to BSON.

        __ https://gist.github.com/zzpwelkin/2279867

        :param value: Shapely geometry instance
        :return: dict to serialize as BSON
        """
        return mapping(value)
