"""Program to draw Mandelbrot fractals: the main entry point.

Author: Lars van den Haak and Tom Verhoeff

Copyright (c) 2020 - Eindhoven University of Technology, The Netherlands

This software is made available under the terms of the MIT License.

* Contributor 1: ...
* TU/e ID number 1: ...
* Contributor 2: ...
* TU/e ID number 2: ...
* Date: ...
"""
from gui import GUI
from PyQt5 import QtWidgets
import sys

# Don't execute this if file is imported
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = GUI()
    window.show()
    app.exec_()
