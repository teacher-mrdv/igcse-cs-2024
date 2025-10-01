# 2D Arrays basics
# Here we use lists to simulate arrays, again.
# MANY THANKS to my MYP Computer Science G2-02 class (2025) for asking awesome questions!!!

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
    for colIndex in range(columnLength):
        print(array[rowIndex][colIndex], end=' ')
    #print(array[rowIndex])
    print()
    
# Task 1: complete this method so that it prints the left-to-right diagonal of an array
# make sure to validate that the array is a square (number of rows=number of columns)
def printDiagonal(array: list):
    rowLength:int = len(array)
    columnLength:int = len(array[rowLength-1]) # length of the last row also works
    if rowLength != columnLength:
        print('The array input is not a square, cannot extract a diagonal.')
        return
    for index in range(rowLength):
        print(array[index][index], end=' ')
    print()
    return 

# Task 2: complete this method so that it prints a specific COLUMN from an array
# make sure to validate the given column as it has to be < the number of column
def printColumn(array: list, columnIndex:int):
    rowLength:int = len(array)
    columnLength:int = len(array[0])
    if columnIndex >= columnLength:
        return
    for rowIndex in range(rowLength):
        print(array[rowIndex][columnIndex], end=' ')
    print()
    
#################################################################################
# Main Method ###################################################################
#################################################################################

# PSEUDOCODE
# DECLARE Arr2d : ARRAY[0:1, 0:3] OF INTEGER
arr2d = create2DArray(2, 4, 0)
print(arr2d)
print()
prettyPrintArray(arr2d)
print()
# PSEUDOCODE and remarks:
# DECLARE Another2dArray : ARRAY[0:4, 0:3] OF CHAR
# Below: '' or None to initialise the array with empty strings or null/nothing;
# Python doesn't have a char/character data type, only string
another2dArray = create2DArray(5, 4, '')
prettyPrintArray(another2dArray)
print()
another2dArray = [ ['0','1','2','3'], ['4','5','6','7'], ['8','9','A','B'], ['C','D','E','F'], ['G','H','I','J'] ]
printArray(another2dArray)
columnLen = len(another2dArray[0])
rowLen    = len(another2dArray)
print(f'\nlength of rows = {rowLen}')
print(f'length of each column = {columnLen}\n')
printDiagonal(another2dArray)
# Use the printRow function to print column #2 or another2dArray
print('3rd row (index 2) of the array above: ', end='')
printRow(another2dArray, 2)
print('Last column (index columnLength-1) of the array above: ', end='')
printColumn(another2dArray, columnLen-1)
print()

# diagonal if array is square
squareArray = create2DArray(3, 3, 0)
squareArray = [ [9,8,7], [6,5,4], [3,2,1] ]
prettyPrintArray(squareArray)
columnLen = len(squareArray[0])
rowLen    = len(squareArray)
print(f'\nlength of rows = {rowLen}')
print(f'length of each column = {columnLen}\n')
print('First column (index 0) of the array above: ', end='')
printColumn(squareArray, 0)
print('Last row (len(array)-1) of the array above: ', end='')
printRow(squareArray, len(squareArray)-1)
print('Diagonal of the array above: ', end='')
printDiagonal(squareArray)
print()

# mirror another2dArray

# transpose another2dArray
# Work in progress--- convert to function!
for c in range(len(another2dArray[0])):
    for r in range(len(another2dArray)):
        print(another2dArray[r][c], end=' ')
    print()

print()

# Davi's question - processing a 2D array by column (and by rows first):
prettyPrintArray(squareArray)
print('\nProcessing rows:')
for rowIndex in range(len(squareArray)):
    suma: int = 0
    for columnIndex in range(len(squareArray[0])):
        x: int = squareArray[rowIndex][columnIndex]
        suma += x
        print(x, end=' ')
    print(f' = {suma}')
print('\nProcessing columns:')
for columnIndex in range(len(squareArray[0])):
    suma: int = 0
    for rowIndex in range(len(squareArray)):
        x: int = squareArray[rowIndex][columnIndex]
        suma += x
        print(x, end=' ')
    print(f' = {suma}')
print()
