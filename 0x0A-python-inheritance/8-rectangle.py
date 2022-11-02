#!/usr/bin/python3
"""
Building a class - Rectangle inherits from BaseGeometry
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """
    child class using parent class function
    """
    def __init__(self, width, height):
        self.__width = width
        self.__height = height

        super().integer_validator('width', width)
        super().integer_validator('height', height)
