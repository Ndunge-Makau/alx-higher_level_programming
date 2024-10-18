#!/bin/bash

"""Defines find_peak function"""


def find_peak(list_of_integers):
    """Find the peak of an unsorted list of integers."""

    if list_of_integers is None:
        return None

    length = len(list_of_integers)

    if length == 1:
        return list_of_integers
    elif length == 2:
        return max(list_of_integers)
    low = 0
    high = length - 1

    while low <= high:
        mid = (low + high) // 2
        if (mid == 0 or list_of_integers[mid] >= list_of_integers[mid - 1]) and (mid == length - 1 or list_of_integers[mid] >= list_of_integers[mid + 1]):
            return list_of_integers[mid]
        elif mid > 0 and list_of_integers[mid - 1] > list_of_integers[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return None
