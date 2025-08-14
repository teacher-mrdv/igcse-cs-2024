# Creating, printing and getting the dimensions and lengths of arrays
# We are using NumPy which has an expanded implementation of arrays instead of Python lists
# https://numpy.org/doc/2.1/reference/arrays.ndarray.html
# [NumPy]  Array = static length, has a defined maximum of elements that can be stored its allocated memory space
# [Python] list  = dynamic length (grows and shrinks depending of its contents)

### ndim		array.ndim
# Purpose: It indicates how many levels of nesting or axes an array possesses (dimensions).
# Usage: You access it as an attribute of a NumPy array: array_name.ndim.
# Return Value: An integer representing the number of dimensions.
# Examples:
# A scalar (single value) has ndim = 0.
# A 1-dimensional array (vector) has ndim = 1.
# A 2-dimensional array (matrix) has ndim = 2.

### shape		array.shape
# Returns the shape of an array in a tuple (think about it as an immutable list) of ints
# The elements of the shape tuple give the lengths of the corresponding array dimensions.

import numpy as np

# pseudocode:    DECLARE array1D : ARRAY[0:9] OF INTEGER
# Python    :    full(shape, fill_value, dtype=None): Returns a new array of given shape and type 'dtype', filled with 'fill_value'. shape = length, eg. 10 integers
array1D = np.full(10, 0, dtype = int)
print( type(array1D) )
print( array1D )
print()
array1D = np.array( [27, 19, 36, 42, 16, 89, 21, 18, 55, 72] )
print( array1D )
print( f'Dimensions (ndim) = {array1D.ndim}' )
print( f'Length (shape)    = {array1D.shape}')
print()


# pseudocode:    DECLARE array2D : ARRAY[0:2, 0:3] OF INTEGER
# Python    :    full(shape, fill_value, dtype=None): Return a new array of given shape and type, filled with `fill_value`. shape = lengths, eg. 2 columns, 5 rows
array2D = np.full( (2, 4), 0, dtype = int)
print( array2D )
print( type(array2D) )
array2D = np.array(  [[1, 2, 3, 4], [5, 6, 7, 8]] )
print( array2D )
print( f'Dimensions (ndim) = {array2D.ndim}' )
print( f'Length (shape)    = {array2D.shape}')

rows = np.size(array2D, axis=0)    # Number of rows
columns = np.size(array2D, axis=1) # Number of columns
print(f'Number of rows: {rows}')
print(f'Number of columns: {columns}')

rows = array2D.shape[0]
columns = array2D.shape[1]
print(f'Number of rows: {rows}')
print(f'Number of columns: {columns}')
print()
# creates a new array of shape (dimensions): 2 rows x 5 columns, and fills it up with Xs
# 'X' can be changed with anything else
new_array = np.full( (2, 5), 'X', dtype = str)
print( new_array )
print( f'Dimensions (ndim) = {new_array.ndim}' )
print( f'Length (shape)    = {new_array.shape}')
rows = new_array.shape[0]
columns = new_array.shape[1]
print(f'Number of rows: {rows}')
print(f'Number of columns: {columns}')
