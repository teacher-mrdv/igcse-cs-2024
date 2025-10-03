# 2D Arrays basics
# Here we use lists to simulate arrays, again.

# this method creates a two dimensional array of the specified dimensions
# (rows and columns), and initialises the array with the given initialValue
def create2DArray(rows, columns, initialValue):
    temp = []
    column = [initialValue] * columns	# create one column
    for row in range(rows):				# create the rows
        temp.append(column)
    return temp

def prettyPrintArray(array):
    length:int = len(array)
    print('[', array[0])
    for rowIndex in range(1, length):
        print(f'  {array[rowIndex]}', end='')
        if rowIndex < length-1:
            print()
    print(' ]')

# simpler, but in line with IGCSE pseudocode
def printArray(array):
    rowLength:int = len(array)
    columnLength:int = len(array[0])
    for rowIndex in range(rowLength):
        for colIndex in range(columnLength):
            print(array[rowIndex][colIndex], end=' ')
        print()

# Task 0: complete this method so that it prints a specific ROW from an array
# make sure to validate the given row as it has to be < the number of rows
def printRow(array: list, rowIndex:int):
    rowLength:int = len(array)
    if rowIndex >= rowLength:
        return None
    columnLength:int = len(array[rowIndex])
    #for colIndex in range(columnLength):
        #print(array[rowIndex][colIndex], end=' ')
    print(array[rowIndex])
    print()


# DECLARE arr2d : ARRAY[0:1, 0:3] OF INTEGER

arr2d = create2DArray(2, 4, 0)
print(arr2d)
print()
prettyPrintArray(arr2d)
print()
another2dArray = create2DArray(5, 4, None)
prettyPrintArray(another2dArray)
print()
another2dArray = [ ['0','1','2','3'], ['4','5','6','7'], ['8','9','A','B'], ['C','D','E','F'], ['G','H','I','J'] ]
printArray(another2dArray)
columnLen = len(another2dArray[0])
rowLen    = len(another2dArray)
print(f'\nlength of rows = {rowLen}')
print(f'length of each column = {columnLen}\n')
# Use the printRow function to print column #2 or another2dArray
printRow(another2dArray, 2)
# diagonal if array is square
if columnLen == rowLen:
    
# mirror another2dArray

# transpose another2dArray

