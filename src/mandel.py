"""Program to draw Mandelbrot fractals: the Mandelbrot algorithm.

Author: Lars van den Haak and Tom Verhoeff

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.

* Contributor 1: ...
* TU/e ID number 1: ...
* Contributor 2: ...
* TU/e ID number 2: ...
* Date: ...
"""
from typing import Tuple, Sequence, TypeVar, Callable, Any, cast
import math
from numba import jit  # type: ignore

#: The type of 2D points.
Point = Tuple[float, float]


def mandel_seq(x: float, y: float, n: int = 100) -> Sequence[Point]:
    """Return the mandel sequence for the input point (x, y), using n as upper bound.

    Assumptions:

    * start the sequence at (u_0, v_0) = (0, 0)
    * The coordinate (x, y) will have mandel number n,
      when the sequence starts diverging at (u_n,  v_n)

    :param x: x-coordinate of the point for which the sequence is computed
    :param y: y-coordinate of the point for which the sequence is computed
    :param n: upper bound to detect divergence
    :return: the mandel sequence for the point (x, y)

    :examples:

    >>> mandel_seq(1, 0)
    [(0.0, 0.0), (1.0, 0.0), (2.0, 0.0), (5.0, 0.0)]
    >>> mandel_seq(1, -1)
    [(0.0, 0.0), (1.0, -1.0), (1.0, -3.0)]
    >>> mandel_seq(0, 0, n = 1)
    [(0.0, 0.0), (0.0, 0.0)]
    """
    # TODO Exercise c
    return


def mandel_number(x: float, y: float, n: int = 100) -> int:
    """Return the mandel-number of point (x, y).

    This is the smallest index of the mandel sequence at which u_n^2 + v_n^2 > 4.

    Assumptions:

    * the sequence diverges when u_n^2 + v_n^2 > 4

    :param x: x-coordinate of the point for which the Mandel number is computed
    :param y: y-coordinate of the point for which the Mandel number is computed
    :param n: upper bound to detect divergence
    :return: the mandel-number of point (x, y)

    :examples:

    >>> mandel_number(1.0, 0.0)
    3
    >>> mandel_number(0.0, 0.0, n = 10)
    10
    """
    # TODO Exercise c
    return


# Some colours
Color = Tuple[int, int, int]
black: Color = (0, 0, 0)
grey: Color = (128, 128, 128)
white: Color = (255, 255, 255)
red: Color = (255, 0, 0)
green: Color = (0, 255, 0)
blue: Color = (0, 0, 255)


# For each pixel define its xy-coordinate
def convert_pixel(px: int, py: int, width: int = 600, height: int = 600) -> Tuple[float, float]:
    # TODO Exercise d & e
    return


# For each pixel define it's colour
def color_mandel(px: int, py: int, width: int = 600, height: int = 600,
                 n: int = 100) -> Color:
    # TODO Exercise d & f
    return