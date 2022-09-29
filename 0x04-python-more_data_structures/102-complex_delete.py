#!/usr/bin/python3
def complex_delete(my_dict, value):
    copy = my_dict.copy()
    for kiis, valew in copy.items():
        if value in valew:
            del my_dict[kiis]
    return my_dict
