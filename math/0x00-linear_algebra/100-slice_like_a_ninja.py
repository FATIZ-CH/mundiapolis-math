#!/usr/bin/env python3
def np_slice(matrix, axes={}):
    slice_matrix = [slice(None, None, None)]*matrix.ndim
    for f, e in sorted(axes.items()):
        slice_value = slice(*e)
        slice_matrix[f] = slice_value
    matrix = matrix[tuple(slice_matrix)]
    return matrix  
