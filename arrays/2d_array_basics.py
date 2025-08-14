# 2D Arrays basics
# Here we use lists to simulate arrays, again.

# this method creates a two dimensional array of the specified dimensions
# (rows and columns), and initialises the array with the given initialValue
def create2DArray(rows, columns, initialValue):
    temp = []
    column = [initialValue] * columns	# create one column
    for r in range(rows):				# create the rows
        temp.append(column)
    return temp

# DECLARE arr2d : ARRAY[0:1, 0:3] OF INTEGER
arr2d = create2DArray(2, 4, 0)
print(arr2d)