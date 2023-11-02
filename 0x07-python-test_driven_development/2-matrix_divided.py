#!/usr/bin/python3
"""
Defines the matrix_divided function.
"""


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.
    """
    new_matrix = []

    if type(div) is not float and type(div) is not int:
        raise TypeError("div must be a number")
    if (div == 0):
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix) - 1):
        if (len(matrix[i]) != len(matrix[i + 1])):
            raise TypeError("Each row of the matrix must have the same size")
    for m in range(len(matrix)):
        result_list = []
        for j in matrix[m]:
            if (type(j) is not int and type(j) is not float):
                raise TypeError("matrix must be a matrix (list of lists)"
                                + " of integers/floats")
            else:
                result = j / div
                result_list.append(round(result, 2))
        new_matrix.append(result_list)
    return new_matrix
