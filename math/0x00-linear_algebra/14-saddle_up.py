#!/usr/bin/env python3
import numpy as np
def np_matmul(mat1, mat2):
    mat3 = np.dot(mat1, mat2)
    return mat3
np_matmul = __import__('14-saddle_up').np_matmul
