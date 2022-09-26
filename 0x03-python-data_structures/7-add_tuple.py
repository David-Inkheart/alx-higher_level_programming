#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):

    a_tuple = list(tuple_a) + [0]*2
    b_tuple = list(tuple_b) + [0]*2
    add_tuple = [x + y for x, y in zip(a_tuple, b_tuple)]
    return tuple(add_tuple[0:2])
