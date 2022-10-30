#!/usr/bin/python3
'''
This class will be the “base” of all other classes in this project
The goal of it is to manage id attribute in all future classes
and to avoid duplicating the same code (by extension, same bugs)
'''


class Base:
    '''My base class'''

    __nb_objects = 0

    def __init__(self, id=None):

        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects
