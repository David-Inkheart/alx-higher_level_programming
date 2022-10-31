#!/usr/bin/python3
'''
Defines a square class.
'''

from models.rectangle import Rectangle


class Square(Rectangle):
    '''square class for almost a circle project'''

    def __init__(self, size, x=0, y=0, id=None):
        '''
        Initializes a new Square.

        Args:
            size (int): The size of the new Square.
            x (int): The x coordinate of the new Square.
            y (int): The y coordinate of the new Square.
            id (int): The identity of the new Square.
        Raises:
            TypeError: If either if size is not an int.
            ValueError: If either id size <= 0.
            TypeError: If either of x or y is not an int.
            ValueError: If either of x or y < 0.
        '''
        super().__init__(width=size, height=size, x=x, y=y, id=id)

    @property
    def size(self):
        '''setter getter for the size of the square.'''
        return self.width

    @size.setter
    def size(self, value):
        if type(value) != int:
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def __str__(self):
        '''returns a nicely printed string about the Square'''
        return '[' + self.__class__.__name__ + ']' + ' (' + str(self.id) \
            + ') ' + str(self.x) + '/' + str(self.y) + ' - '\
            + str(self.size)

    def update(self, *args, **kwargs):
        '''
        Assigned arguments in order
        '''
        if not args and not kwargs:
            return

        if args and len(args) != 0:
            try:
                self.id = args[0]
                self.size = args[1]
                self.x = args[2]
                self.y = args[3]
            except IndexError:
                pass
        else:
            for kii, val in kwargs.items():
                setattr(self, kii, val)
