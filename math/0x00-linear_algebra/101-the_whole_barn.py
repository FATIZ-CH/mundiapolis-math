#!/usr/bin/env python3
def add_matrices(mat1, mat2):
    if np.shape(mat1) != np.shape(mat1):
        return None

    result = np.add(mat1, mat2)
    return result
  
  
add_matrices = __import__('101-the_whole_barn').add_matrices
