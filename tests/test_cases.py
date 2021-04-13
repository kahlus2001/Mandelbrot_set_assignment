"""Unit tests for the Mandelbrot software.

Author: Tom Verhoeff

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.

* Contributor 1: ...
* TU/e ID number 1: ...
* Contributor 2: ...
* TU/e ID number 2: ...
* Date: ...

This software is made available under the terms of the MIT License.
"""

from mandel import *
import random


def test_random_numbers() -> None:
    """Tests if we add random numbers, the bounds are still respected.
    """
    for i in range(0, 100):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        assert -2.0 <= x + y <= 2.0
