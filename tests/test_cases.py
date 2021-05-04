"""Unit tests for the Mandelbrot software.

Author: Lars van den Haak and Tom Verhoeff

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.
"""

from mandel import *
import random

import doctest

def test_random_numbers() -> None:
    """Tests if we add random numbers, the bounds are still respected.
    """
    for i in range(0, 100):
        x, y = random.uniform(-1, 1), random.uniform(-1, 1)
        assert -2.0 <= x + y <= 2.0

def test_mandel_seq() -> None:
    """Tests mandel_seq function for chosen values.
    """
    doctest.run_docstring_examples(mandel_seq, globals(), verbose=True, name='mandel_seq')

def test_mandel_number() -> None:
    """Tests mandel_seq function for chosen values.
    """
    doctest.run_docstring_examples(mandel_number, globals(), verbose=True, name='mandel_number')

def test_convert_pixel() -> None:
    """Tests mandel_seq function for chosen values.
    """
    doctest.run_docstring_examples(convert_pixel, globals(), verbose=True, name='convert_pixel')

def test_color_mandel() -> None:
    """Tests mandel_seq function for chosen values.
    """
    doctest.run_docstring_examples(color_mandel, globals(), verbose=True, name='color_mandel')



