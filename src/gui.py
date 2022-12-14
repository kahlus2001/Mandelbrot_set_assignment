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


x_coordinate = - 1.5
y_coordinate = - 1
x_low = - 1.5
x_high = 0.5
y_low = - 1
y_high = 1


class CentreWindow(QtWidgets.QWidget):
    """
    This "window" is a QWidget. If it has no parent, it
    will appear as a free-floating window as we want.
    """

    def __init__(self):
        super().__init__()
        layout = QtWidgets.QVBoxLayout()
        self.label = QtWidgets.QLabel("Centre Window")
        self.label.setPixmap(QtGui.QPixmap(600, 600))
        layout.addWidget(self.label)

        self.shift_x = QLineEdit("Input centre X coordinate", self)
        self.shift_y = QLineEdit("Input centre Y coordinate", self)

        self.shift_x.setGeometry(650, 80, 150, 40)
        self.shift_y.setGeometry(650, 120, 150, 40)

        confirm_button = QtWidgets.QPushButton('Confirm', self)
        layout.addWidget(confirm_button)
        confirm_button.clicked.connect(self.assign_x_y)
        confirm_button.setGeometry(665, 200, 120, 60)

    def assign_x_y(self):
        """"Assign users input to variable."""
        global x_coordinate
        global y_coordinate
        x_coordinate = float(self.shift_x.text()) - 1.5
        y_coordinate = float(self.shift_y.text()) - 1
        self.update()
        self.close()


class GUI(QtWidgets.QMainWindow):
    """A class where we make our Graphical User Interface based on PyQT
    """

    def __init__(self) -> None:
        """Initializer of the GUI class
        """
        super().__init__()
        main = QtWidgets.QWidget()
        layout = QtWidgets.QGridLayout()
        main.setLayout(layout)
        self.setCentralWidget(main)

        self.canvas = QtWidgets.QLabel()
        self.canvas.setPixmap(QtGui.QPixmap(600, 600))
        layout.addWidget(self.canvas)

        # creating menu bar
        mainMenu = self.menuBar()
        # adding file menu in it
        fileMenu = mainMenu.addMenu("File")
        # creating save action
        saveAction = QtWidgets.QAction("Save", self)
        # setting save action shortcut
        saveAction.setShortcut("Ctrl + S")
        # adding save action to filemenu
        fileMenu.addAction(saveAction)
        # setting triggered method
        saveAction.triggered.connect(self.save)

        red_button = QtWidgets.QPushButton('RED', self)
        layout.addWidget(red_button, 1, 1)
        green_button = QtWidgets.QPushButton('GREEN', self)
        layout.addWidget(green_button, 1, 2)
        white_button = QtWidgets.QPushButton('WHITE', self)
        layout.addWidget(white_button, 1, 3)
        blue_button = QtWidgets.QPushButton('BLUE', self)
        layout.addWidget(blue_button, 2, 1)

        blur_button = QtWidgets.QPushButton('Blur image', self)
        layout.addWidget(blur_button, 2, 3)

        self.shift_x = QLineEdit("Centre X coordinate", self)
        layout.addWidget(self.shift_x, 3, 1)
        self.shift_y = QLineEdit("Centre Y coordinate", self)
        layout.addWidget(self.shift_y, 3, 2)
        confirm_button = QtWidgets.QPushButton('Confirm centre point', self)
        layout.addWidget(confirm_button, 3, 3)

        self.lower_x = QLineEdit("Lower X limit", self)
        layout.addWidget(self.lower_x, 4, 1)
        self.upper_x = QLineEdit("Upper X limit", self)
        layout.addWidget(self.upper_x, 4, 2)
        self.lower_y = QLineEdit("Lower Y limit", self)
        layout.addWidget(self.lower_y, 5, 1)
        self.upper_y = QLineEdit("Upper Y limit", self)
        layout.addWidget(self.upper_y, 5, 2)
        bounds_button = QtWidgets.QPushButton('Confirm new bounds', self)
        layout.addWidget(bounds_button, 5, 3)

        # Connect the random_color function to a click event
        red_button.clicked.connect(self.red_color)
        green_button.clicked.connect(self.green_color)
        white_button.clicked.connect(self.white_color)
        blue_button.clicked.connect(self.blue_color)
        blur_button.clicked.connect(self.blur_image)
        confirm_button.clicked.connect(self.assign_x_y)
        bounds_button.clicked.connect(self.change_bounds)

        self.w = None
        self.blur = False
        # self.Exercise_j()
        self.choose_color = blue
        self.update()

    def change_bounds(self):
        """"Change the range to show the Mandelbrot set."""
        global x_low
        global x_high
        global y_low
        global y_high
        x_low = float(self.lower_x.text())
        x_high = float(self.upper_x.text())
        y_low = float(self.lower_y.text())
        y_high = float(self.upper_y.text())
        self.update()

    def assign_x_y(self):
        """"Assign users input to variable."""
        global x_coordinate
        global y_coordinate
        global x_low
        global y_low
        x_coordinate = float(self.shift_x.text()) + x_low
        y_coordinate = float(self.shift_y.text()) + y_low
        self.update()

    def blur_image(self) -> None:
        """"Blur the image by taking the average of the surrounding pixels."""
        self.blur = True
        # imageblur[x, y] = (image[x - 1][y] + image[x][y] + image[x + 1][y]) / 3
        self.update()

    # save method
    def save(self):
        # selecting file path
        filePath, _ = QtWidgets.QFileDialog.getSaveFileName(self, "Save Image", "",
                                                            "PNG(*.png);;JPEG(*.jpg *.jpeg);;All Files(*.*) ")
        # if file path is blank return back
        if filePath == "":
            return
        # saving canvas at desired path
        self.canvas.pixmap().save(filePath)

    def show_new_window(self, checked):
        """"Open new window to input centre point."""
        if self.w is None:
            self.w = CentreWindow()
        self.w.show()

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
        global x_coordinate
        global y_coordinate
        global x_low
        global x_high
        global y_low
        global y_high
        change_range(x_low, x_high, y_low, y_high)
        painter = QtGui.QPainter(self.canvas.pixmap())

        def coloring(px: int, py: int, x_shift: float = -1.5, y_shift: float = - 1) -> Color:
            """Picks the correct coloring function.
            """

            return color_mandel(px, py, x_shift, y_shift)

        if self.blur == True:
            for x in range(0, 600):
                for y in range(0, 600):
                    x, y = (self.canvas.pixmap()[x - 1][y] + self.canvas.pixmap()[x][y] + self.canvas.pixmap()[x + 1][
                        y]) / 3
                    painter.drawPoint(x, y)
        else:
            for x in range(0, 600):
                for y in range(0, 600):
                    (r, g, b) = coloring(x, y, x_coordinate, y_coordinate)
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
