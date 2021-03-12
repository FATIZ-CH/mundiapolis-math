#!/usr/bin/env python3
def np_cat(mat1, mat2, axis=0):
    mat_1 = np.array(mat1)
    mat_2 = np.array(mat2)
    mat_3 = np.concatenate((mat_1, mat_2), axis)
    return mat_3
 
