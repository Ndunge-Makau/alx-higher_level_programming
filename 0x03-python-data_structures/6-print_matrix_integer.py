#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row:
            print("{}".format(i), end='')
            if i != row[len(row) - 1]:
                print(" ", end='')
 
        print("")
