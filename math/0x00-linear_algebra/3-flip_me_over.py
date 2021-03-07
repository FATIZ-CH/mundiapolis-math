#!/usr/bin/env python3

def matrix_transpose(matrix):
    new_matrix = []
    
    for i in range(len(matrix[0])):
        N_row = []
        for j in range(len(matrix)):
            N_row.append(matrix[j][i])
        new_matrix.append(N_row)

    return new_matrix
  
matrix_transpose = __import__('3-flip_me_over').matrix_transpose

mat1 = [[1, 2], [3, 4]]
print(mat1)
print(matrix_transpose(mat1))
mat2 = [[1, 2, 3, 4, 5], [6, 7, 8, 9, 10], [11, 12, 13, 14, 15],
        [16, 17, 18, 19, 20], [21, 22, 23, 24, 25], [26, 27, 28, 29, 30]]
print(mat2)
print(matrix_transpose(mat2))
