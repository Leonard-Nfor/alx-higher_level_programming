#!/usr/bin/python3
""" specify the interpreter to use when executing the script."""


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
