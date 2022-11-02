#!/usr/bin/python3
"""
Building a class - Square inherits from Rectangle
"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    grandchild class
    """
    def __init__(self, size):
        self.__size = size

        super().integer_validator('size', size)

    def area(self):
        return self.__size * self.__size

    def __str__(self):
        return '[{}] {}/{}'.format(self.__class__.__name__,
                                   self.__size, self.__size)
