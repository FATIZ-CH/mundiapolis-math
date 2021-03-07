#!/usr/bin/env python3
import numpy
def mat_mul(mat1, mat2):
    return numpy.dot(mat1,mat2)
mat_mul = __import__('8-ridin_bareback').mat_mul

mat1 = [[1, 2],
        [3, 4],
        [5, 6]]
mat2 = [[1, 2, 3, 4],
        [5, 6, 7, 8]]
print(mat_mul(mat1, mat2))
