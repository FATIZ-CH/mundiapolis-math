#!/usr/bin/env python3
import numpy
def cat_arrays(arr1, arr2):
    return numpy.concatenate((arr1, arr2), axis=None)
cat_arrays = __import__('6-howdy_partner').cat_arrays

arr1 = [1, 2, 3, 4, 5]
arr2 = [6, 7, 8]
print(cat_arrays(arr1, arr2))
print(arr1)
print(arr2)
