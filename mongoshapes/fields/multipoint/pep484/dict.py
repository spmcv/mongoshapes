#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union, Sequence, Dict


MultiPointGeometry = Sequence[Sequence[float]]
MultiPointValues = Union[str, MultiPointGeometry]
MultiPointDict = Dict[str, MultiPointValues]
