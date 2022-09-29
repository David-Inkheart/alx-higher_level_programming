#!/usr/bin/python3
def print_sorted_dictionary(my_dict):
    for kiis in sorted(my_dict.keys()):
        print("{}: {}".format(k, my_dict[kiis]))
