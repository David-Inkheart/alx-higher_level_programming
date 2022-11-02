#!/usr/bin/python3
"""
Building a class - BaseGeometry
"""


class BaseGeometry:
    """
    empty class + public instance method area(self)
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """function that validates valye
        """

        self.name = name
        self.value = value
        if not type(value) == int:
            raise TypeError("{} must be an integer".format(self.name))
        if value <= 0:
            raise ValueError("{} must be greater than 0".format(self.name))
