#!/usr/bin/python3
class Rectangle:
    """A rectangle class"""
    def __init__(self, width=0, height=0):
        """initialisation takes place here"""
        self.__width = width
        self.__height = height

    @property
    def width(self):
        """retrieve the width"""
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
        """return the height"""
        return (self.__height)

    @height.setter
    def height(self, value):
        """set value"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """the area of rectangle"""
        return (self.__width * self.__height)

    def perimeter(self):
        """return the total distance round the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return (0)
        else:
            return (2 * self.__width + 2 * self.__height)

    def __str__(self):
        if self.__width == 0 or self.__height == 0:
            return ("")
        rectangle_str = ""
        for i in range(self.__height):
            rectangle_str += "#" * self.__width + "\n"
        return (rectangle_str)
