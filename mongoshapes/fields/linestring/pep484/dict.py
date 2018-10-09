#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union, Sequence, Dict


LineStringGeometry = Sequence[Sequence[float]]
LineStringValues = Union[str, LineStringGeometry]
LineStringDict = Dict[str, LineStringValues]
