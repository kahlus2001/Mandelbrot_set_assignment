"""Program to draw Mandelbrot fractals: the graphical user interface.

Author: Lars van den Haak and Tom Verhoeff

Copyright (c) 2021 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.
"""
from PyQt5 import QtGui, QtWidgets
from PyQt5.QtGui import QColor
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QLineEdit

from mandel import *
import random


def squares(px: int, py: int, c1: Color = green, c2: Color = blue) -> Color:
    """Colors the screen in squares of 20 pixels

    :param px: pixel x-coordinate
    :param py: pixel y-coordinate
    :param c1: Color of the first type of square
    :param c2: Color of the second type of square
    :return: Color for the input pixel
    """
    if px // 20 % 2 == py // 20 % 2:
        c = c1
    else:
        c = c2
    return c


class GUI(QtWidgets.QMainWindow):
    """A class where we make our Graphical User Interface based on PyQT
    """

    def __init__(self) -> None:
        """Initializer of the GUI class
        """
        super().__init__()
        main = QtWidgets.QWidget()
        layout = QtWidgets.QVBoxLayout()
        main.setLayout(layout)
        self.setCentralWidget(main)

        self.canvas = QtWidgets.QLabel()
        self.canvas.setPixmap(QtGui.QPixmap(600, 600))
        layout.addWidget(self.canvas)

        red_button = QtWidgets.QPushButton('RED', self)
        layout.addWidget(red_button)
        green_button = QtWidgets.QPushButton('GREEN', self)
        layout.addWidget(green_button)
        white_button = QtWidgets.QPushButton('WHITE', self)
        layout.addWidget(white_button)
        blue_button = QtWidgets.QPushButton('BLUE', self)
        layout.addWidget(blue_button)

        # Connect the random_color function to a click event
        red_button.clicked.connect(self.red_color)
        green_button.clicked.connect(self.green_color)
        white_button.clicked.connect(self.white_color)
        blue_button.clicked.connect(self.blue_color)

        self.choose_color = blue
        self.update()

    def update(self) -> None:  # type: ignore
        """Draw a new image."""
        self.make_image()
        super().update()

    def red_color(self) -> None:
        """Change the colors of the image into red.
        """
        self.choose_color = red
        self.update()

    def green_color(self) -> None:
        """Change the colors of the image into random colors.
        """
        self.choose_color = green
        self.update()

    def white_color(self) -> None:
        """Change the colors of the image into random colors.
        """
        self.choose_color = white
        self.update()

    def blue_color(self) -> None:
        """Change the colors of the image into random colors.
        """
        self.choose_color = blue
        self.update()

    def mousePressEvent(self, event: QtGui.QMouseEvent) -> None:
        """Event handler for mouse clicking.

        :param event: The QMouseEvent from the PyQt5 library.
        """
        if self.canvas.underMouse():
            print(event)

    def make_image(self) -> None:
        """Puts an image on screen created by function 'coloring'
        """

        painter = QtGui.QPainter(self.canvas.pixmap())



        def coloring(px: int, py: int) -> Color:
            """Picks the correct coloring function.
            """

            return color_mandel(px, py)

        for x in range(0, 600):
            for y in range(0, 600):
                (r, g, b) = coloring(x, y)
                if self.choose_color == red:
                    r = b
                    b = 0
                elif self.choose_color == green:
                    g = b
                    b = 0
                elif self.choose_color == white:
                    g = b
                    r = b
                painter.setPen(QColor(r, g, b))
                painter.drawPoint(x, y)
        painter.end()
