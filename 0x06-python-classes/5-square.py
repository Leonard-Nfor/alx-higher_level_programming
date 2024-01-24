#!/usr/bin/python3
"""module"""


class Square:
    """define a square with optional artribute to size"""
    def __init__(self, size=0):
        """initializer and condition to check integer of the size"""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    @property
    def size(self):
        """Return the size of square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        """set the current size of a square"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """return the area of a square"""
        return (self.__size * self.__size)

    def my_print(self):
        """print to stdout"""
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
        if self.__size == 0:
            print("")
