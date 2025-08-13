# Creating, printing and getting the dimensions and lengths of arrays
# We are using NumPy which has arrays instead of Python lists
# [NumPy]  Array = static length, has a defined maximum of elements that can be stored its allocated memory space
# [Python] list  = dynamic length (grows and shrinks depending of its contents)

import numpy as np

array1D = np.array( [1, 2, 3, 4, 5, 6, 7, 8] )
print( type(array1D) )
print( array1D )
print( f'Dimensions (ndim) = {array1D.ndim}' )
print( f'Dimensions (shape) = {array1D.shape}')
print()
array2D = np.array(  [[1, 2, 3, 4], [5, 6, 7, 8]] )
print( type(array2D) )
print( array2D )
print( f'Dimensions (ndim) = {array2D.ndim}' )
print( f'Dimensions (shape) = {array2D.shape}')

rows = np.size(array2D, axis=0)    # Number of rows
columns = np.size(array2D, axis=1) # Number of columns
print(f'Number of rows: {rows}')
print(f'Number of columns: {columns}')

rows = array2D.shape[0]
columns = array2D.shape[1]
print(f'Number of rows: {rows}')
print(f'Number of columns: {columns}')
print()
# creates a new array of shape (dimensions): 3 rows x 2 columns, and fills it up with -1s
# -1 can be changed with anything else
new_array = np.full( (2, 5), 'X')
print( new_array )
print( f'Dimensions (ndim) = {new_array.ndim}' )
print( f'Dimensions (shape) = {new_array.shape}')
rows = new_array.shape[0]
columns = new_array.shape[1]
print(f'Number of rows: {rows}')
print(f'Number of columns: {columns}')