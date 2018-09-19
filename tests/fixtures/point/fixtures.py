#!/usr/bin/env python
# -*- coding: utf-8 -*-

import yaml
import pytest

from pathlib import Path

from . import GeoDict


PARENT = Path(__file__).parent


def load(path: Path, name: str) -> GeoDict:
    file = Path(path, name).with_suffix('.yaml')
    text = file.read_text()
    data = yaml.load(text)
    return data


@pytest.fixture
def geojson() -> GeoDict:
    return load(PARENT, 'geojson')


@pytest.fixture
def geointerface() -> GeoDict:
    return load(PARENT, 'geointerface')
