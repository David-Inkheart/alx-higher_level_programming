#!/usr/bin/python3
"""An algorithm to find a peak
Approach will be an implementation of
divide and conquer algorithm."""

def find_peak(list_of_integers):
    if not list_of_integers:
        return None
    if len(list_of_integers) == 1:
        return list_of_integers[0]
    mid = len(list_of_integers) // 2
    if (mid-1 < 0 or list_of_integers[mid] > list_of_integers[mid-1]) and \
       (mid+1 >= len(list_of_integers) or list_of_integers[mid] > list_of_integers[mid+1]):
        return list_of_integers[mid]
    elif mid+1 < len(list_of_integers) and list_of_integers[mid] < list_of_integers[mid+1]:
        return find_peak(list_of_integers[mid+1:])
    else:
        return find_peak(list_of_integers[:mid])

