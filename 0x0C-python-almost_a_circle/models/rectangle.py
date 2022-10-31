#!/usr/bin/python3
'''
Defines a rectangle class.
'''

from models.base import Base


class Rectangle(Base):
    '''rectangle class for almost a circle project'''

    def __init__(self, width, height, x=0, y=0, id=None):
        '''
        Initializes a new Rectangle.

        Args:
            width (int): The width of the new Rectangle.
            height (int): The height of the new Rectangle.
            x (int): The x coordinate of the new Rectangle.
            y (int): The y coordinate of the new Rectangle.
            id (int): The identity of the new Rectangle.
        Raises:
            TypeError: If either of width or height is not an int.
            ValueError: If either of width or height <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        '''
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        '''setter getter for the width of the Rectangle.'''
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        '''setter getter for the height of the Rectangle.'''
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        '''setter getter for the x coordinate of the Rectangle.'''
        return self.__x

    @x.setter
    def x(self, value):
        if type(value) != int:
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be > 0")
        self.__x = value

    @property
    def y(self):
        '''setter getter for the y coordinate of the Rectangle.'''
        return self.__y

    @y.setter
    def y(self, value):
        if type(value) != int:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be > 0")
        self.__y = value

    def area(self):
        '''Returns the area of the rectangle'''
        return self.__width * self.__height

    def display(self):
        '''displays rectangle size with '#'
        y is newline and x is space
        '''
        if self.__y != 0:
            for newline in range(self.__y):
                print()

        for row in range(self.__height):
            print((' ' * self.__x) + ('#' * self.__width))

    def __str__(self):
        '''returns a nicely printed string about Rectangle'''
        return '[' + self.__class__.__name__ + ']' + ' (' + str(self.id) \
            + ') ' + str(self.__x) + '/' + str(self.__y) + ' - '\
            + str(self.__width) + '/' + str(self.__height)

    def update(self, *args, **kwargs):
        '''
        Assigned arguments in order
        '''
        if not args and not kwargs:
            return

        if args and len(args) != 0:
            try:
                self.id = args[0]
                self.__width = args[1]
                self.__height = args[2]
                self.__x = args[3]
                self.__y = args[4]
            except IndexError:
                pass
        else:
            for kii, val in kwargs.items():
                setattr(self, kii, val)

    def to_dictionary(self):
        '''
        returns the dictionary representation of a Rectangle
        '''
        return {'x': self.__x, 'y': self.__y, 'id': self.id,
                'height': self.__height, 'width': self.__width}
