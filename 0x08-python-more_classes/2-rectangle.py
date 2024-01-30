#!/usr/bin/python3
"""direct to specifict interpreter"""


class Rectangle:
    """ This class define a rectangle base on its private attr"""
    def __init__(self, width=0, height=0):
        """ To initialised the instance"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """Return the width"""
        return (self.__width)

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Return height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """return the area of a rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the peremeter"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * self.__width + 2 * self.__height)
