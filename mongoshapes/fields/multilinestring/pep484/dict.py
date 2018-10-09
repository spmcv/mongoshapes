#!/usr/bin/env python
# -*- coding: utf-8 -*-

from typing import Union, Sequence, Dict


MultiLineStringGeometry = Sequence[Sequence[Sequence[float]]]
MultiLineStringValues = Union[str, MultiLineStringGeometry]
MultiLineStringDict = Dict[str, MultiLineStringValues]
