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
        layout = QtWidgets.QVBoxLayout()
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
        layout.addWidget(red_button)
        green_button = QtWidgets.QPushButton('GREEN', self)
        layout.addWidget(green_button)
        white_button = QtWidgets.QPushButton('WHITE', self)
        layout.addWidget(white_button)
        blue_button = QtWidgets.QPushButton('BLUE', self)
        layout.addWidget(blue_button)

        blur_button = QtWidgets.QPushButton('Blur image', self)
        layout.addWidget(blur_button)

        self.shift_x = QLineEdit("Input centre X coordinate", self)
        layout.addWidget(self.shift_x)
        self.shift_y = QLineEdit("Input centre Y coordinate", self)
        layout.addWidget(self.shift_y)
        confirm_button = QtWidgets.QPushButton('Confirm centre point', self)
        layout.addWidget(confirm_button)

        # Connect the random_color function to a click event
        red_button.clicked.connect(self.red_color)
        green_button.clicked.connect(self.green_color)
        white_button.clicked.connect(self.white_color)
        blue_button.clicked.connect(self.blue_color)
        blur_button.clicked.connect(self.blur_image)
        confirm_button.clicked.connect(self.assign_x_y)

        self.w = None
        self.blur = False
        # self.Exercise_j()
        self.choose_color = blue
        self.update()

    def assign_x_y(self):
        """"Assign users input to variable."""
        global x_coordinate
        global y_coordinate
        x_coordinate = float(self.shift_x.text()) - 1.5
        y_coordinate = float(self.shift_y.text()) - 1
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

    def Exercise_j(self) -> None:

        # creating a QLineEdit object
        lower_x = QLineEdit("Input lower X limit", self)
        number_validator = QtGui.QDoubleValidator(self)
        lower_x.setValidator(number_validator)

        lower_y = QLineEdit("Input lower Y limit", self)
        lower_y.setValidator(number_validator)

        # setting geometry
        lower_x.setGeometry(80, 80, 150, 40)
        lower_x.setGeometry(80, 80, 150, 40)

        # adding action to the line edit when enter key is pressed
        lower_x.returnPressed.connect(lambda: self.set_lower_x())

        # method to do action
        def set_lower_x(self) -> None:
            """"Set lower X value."""
            self.value_lower_x = lower_x.text()
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
        global x_coordinate
        global y_coordinate
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
