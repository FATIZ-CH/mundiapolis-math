#!/usr/bin/env python3
import numpy as np
def np_slice(matrix, axes={}):
   
    slice_matrix = [slice(None, None, None)] * matrix.ndim
    for f, e in sorted(axes.items()):
        slice_value = slice(*e)
        slice_matrix[f] = slice_value
    matrix = matrix[tuple(slice_matrix)]
    return matrix
  
np_slice = __import__('100-slice_like_a_ninja').np_slice

mat1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])
print(np_slice(mat1, axes={1: (1, 3)}))
print(mat1)
mat2 = np.array([[[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]],
                 [[11, 12, 13, 14, 15], [16, 17, 18, 19, 20]],
                 [[21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]])
print(np_slice(mat2, axes={0: (2,), 2: (None, None, -2)}))
print(mat2)
