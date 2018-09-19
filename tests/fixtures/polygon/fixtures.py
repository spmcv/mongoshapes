#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import pytest

from pathlib import Path

from mongoshapes import PolygonDict


PARENT = Path(__file__).parent


def params():
    keys = ('single', 'multiple')
    values = ('ring', 'rings')
    for k, v in zip(keys, values):
        i = " ".join((k, v))
        j = Path(PARENT, v)
        yield i, j


def load(path: Path, name: str) -> PolygonDict:
    file = Path(path, name).with_suffix('.yaml')
    text = file.read_text()
    data = yaml.load(text)
    return data


PARAMS = dict(params())


@pytest.fixture(params=PARAMS.values(), ids=PARAMS.keys())
def geojson(request) -> PolygonDict:
    return load(request.param, 'geojson')


@pytest.fixture(params=PARAMS.values(), ids=PARAMS.keys())
def geointerface(request) -> PolygonDict:
    return load(request.param, 'geointerface')
