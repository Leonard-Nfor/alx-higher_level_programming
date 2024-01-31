#!/usr/bin/python3
"""specify what to print"""


class Rectangle:
    """A rectangle class"""
    number_of_instances = 0
    print_symbol = "#"

    def __new__(cls, *args, **kwargs):
        instance = super().__new__(cls)
        cls.number_of_instances += 1
        return (instance)

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
        """print rectangle using #"""
        if self.__width == 0 or self.__height == 0:
            return ("")
        if isinstance(self.print_symbol, list):
            return (" ".join(self.print_symbol) * self.__width + '\n') * self.__height
        else:
            return str(self.print_symbol) * self.__width + "\n" * (self.__height - 1) +  str(self.print_symbol) * self.__width

    def __repr__(self):
        """return the string format ofrectangle"""
        return (f"Rectangle({self.__width}, {self.__height})")

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
