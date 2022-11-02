#!/usr/bin/python3
"""MyList
"""


class MyList(list):
    """inheriting from list class
    """

    def __init__(self):
        """initializer for Mylist
        """
        pass

    def print_sorted(self):
        """Prints list in sorted format
        """
        sorted_list = list.copy(self)
        list.sort(sorted_list)
        print(sorted_list)
