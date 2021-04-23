"""Unit tests for the Mandelbrot software.

Author: Lars van den Haak and Tom Verhoeff

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

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
