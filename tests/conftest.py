#!/usr/bin/env python
# -*- coding: utf-8 -*-

import pytest
import mongoengine as me

from pathlib import Path
from pymongo import MongoClient


@pytest.fixture
def root() -> Path:
    return Path(__file__).parent


@pytest.fixture
def fixtures(root: Path) -> Path:
    return Path(root, 'fixtures')


@pytest.fixture
def radius() -> float:
    return 10


@pytest.fixture
def db() -> str:
    return 'tmpdb'


@pytest.fixture
def host() -> str:
    return 'localhost'


@pytest.fixture
def port() -> int:
    return 27017


@pytest.fixture(autouse=True)
def tmpdb(db: str, host: str, port: int) -> MongoClient:
    yield me.connect(db, host=host, port=port)
    # mc.drop_database(name)
