#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest

from typing import Type
from mongoengine import Document, QuerySet
from mongoshapes import Polygon, PolygonDict
from shapely.geometry import shape, mapping, box

from . import *


DocType = Type[Document]


@pytest.fixture
def geometry(geojson: GeoDict) -> GeoShape:
    """
    Convert the GeoJSON fixture into an appropriate geometry.

    :param geojson: GeoJSON mapping
    :return: geometry instance
    """
    return shape(geojson)


@pytest.fixture
def polygon(radius: float, geometry: GeoShape) -> Polygon:
    """
    Buffer the geometry, find the bounds, and create bounding box.

    :param radius: buffer radius
    :param geometry: geometry to buffer
    :return: bounding box
    """
    buffer = geometry.buffer(radius)
    bounds = buffer.bounds
    return box(*bounds)


@pytest.fixture
def query(polygon: Polygon) -> PolygonDict:
    """
    Convert the :class:`Polygon` to a GeoJSON mapping suitable for MongoDB
    2DSphere polygon query.

    :param polygon: bounding box
    :return: GeoJSON mapping
    """
    return mapping(polygon)


@pytest.fixture(scope='module')
def document() -> DocType:
    """
    Defining the document with module scope ensures that the collection will
    be dropped only when module scope exists; i.e., after all tests finish.

    :return: document class
    """

    class Doc(Document):
        value = GeoField()
        meta = {'collection': GeoShape.__name__.lower()}

    yield Doc
    Doc.drop_collection()


def test_save(document: DocType, geojson: GeoDict):
    """
    Test initializing document with test field and store GeoJSON data.

    :param document: document class
    :param geojson: GeoJSON mapping
    """

    # instance
    doc = document()

    # check field
    assert hasattr(doc, 'value')
    setattr(doc, 'value', geojson)

    # save field
    doc.validate()
    doc.save()


def test_value(document: DocType, geojson: GeoDict):
    """
    Test querying MongoDB with exact GeoJSON value.

    :param document: document class
    :param geojson: GeoJSON mapping
    """

    # do the query
    qry = document.objects(value=geojson)  # type: QuerySet

    # get the first value in cache
    doc = qry.first()

    assert doc is not None


def test_polygon(document: DocType, query: PolygonDict):
    """
    Test querying MongoDB with bounding box polygon.

    :param document: document class
    :param query: GeoJSON mapping
    """

    # query field with box
    qry = document.objects(value__geo_within=query)  # type: QuerySet

    # get the first value in cache
    doc = qry.first()

    assert doc is not None


def test_intersects(document: DocType, geojson: GeoDict):
    """
    Test querying MongoDB with (exact) intersection of GeoJSON mapping.

    :param document: document class
    :param geojson: GeoJSON mapping
    """

    # query field with intersection
    qry = document.objects(value__geo_intersects=geojson)  # type: QuerySet

    # get the first value in cache
    doc = qry.first()

    assert doc is not None
