#!/usr/bin/python3
'''
a class MyInt that inherits from int:
'''


class MyInt(int):
    '''MyInt is a rebel.
    MyInt has == and != operators inverted
    '''

    def __eq__(self, value):
        '''Magid method equals
        '''

        return super().__ne__(value)

    def __ne__(self, value):
        '''Magic method not equals
        '''

        return super().__eq__(value)
