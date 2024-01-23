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
