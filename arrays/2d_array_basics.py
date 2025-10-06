# 2D Arrays basics
# Here we use lists to simulate arrays, again.
# MANY THANKS to my MYP Computer Science G2-02 class (2025) for asking awesome questions!!!

# this method creates a two-dimensional array of the specified dimensions
# (rows and columns), and initialises the array with 0s
def create2DArray(rows, columns) -> list:
    # best way to create a 2D array-like data structure in Python
    temp: list = [[0] * columns for _ in range(rows)]
    return temp

def arraySize(array: list) -> list:
    rows: int = len(array)
    columns: int = len(array[0])
    size: list = []
    size.append(rows)
    size.append(columns)
    return size

def prettyPrintArray(array):
    length:int = len(array)
    print('[', array[0])
    for rowIndex in range(1, length):
        print(f'  {array[rowIndex]}', end='')
        if rowIndex < length-1:
            print()
    print(' ]')
    print(f'size [rows, columns] = {arraySize(array)}\n')

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

# Task 3: Write a method that it returns a copy of the input array, MIRRORED horizontally
# i.e. invert the order of the rows. The only validation here is to make sure the array is not empty.
def hMirror(array: list) -> list:
    if len(array) <= 0:
        return []
    rows: int = len(array)
    columns: int = len(array[0])
    mirror: list = create2DArray(rows, columns)
    for row in range(rows):
        for column in range(columns):
            mirror[rows-1-row][column] = array[row][column]
    return mirror

# Task 4: Write a method that it returns a copy of the input array, MIRRORED vertically this time
# i.e. invert the order of the columns. The only validation here is to make sure the array is not empty.
def vMirror(array: list) -> list:
    if len(array) <= 0:
        return []
    rows: int = len(array)
    columns: int = len(array[0])
    mirror: list = create2DArray(rows, columns)
    for row in range(rows):
        for column in range(columns):
            mirror[row][columns-1-column] = array[row][column]
    return mirror

# Task 5: complete this method so that it returns a copy of the input array...
# ...TRANSPOSED (columns becomes rows, and rows become columns)
# the only validation here is to make sure the array is not empty.
def transpose(array: list) -> list:
    if len(array) <= 0:
        print('Error-array is empty')
        return []
    originalRows:int = len(array)
    originalColumns: int = len(array[0])
    transposed: list = create2DArray(originalColumns, originalRows)
    for row in range(originalRows):
        for column in range(originalColumns):
            transposed[column][row] = array[row][column]
    return transposed

#################################################################################
# Main Method ###################################################################
#################################################################################

# PSEUDOCODE
# DECLARE Arr2d : ARRAY[0:1, 0:3] OF INTEGER
arr2d = create2DArray(2, 4)
print("\nPrinting a 2D array with Python's print")
print(arr2d)
print('\nNow using our own functions')
printArray(arr2d)
print()
prettyPrintArray(arr2d)

# PSEUDOCODE and remarks:
# DECLARE Another2dArray : ARRAY[0:4, 0:3] OF CHAR
# Below: our create2DArray function initialises the array with 0s by default,
# which Python allows to be replaced with any other data [type]
# Reminder: Python doesn't have a char/character data type, only string
another2dArray = create2DArray(5, 4)
print('Creating a 5r4c 2D array')
prettyPrintArray(another2dArray)
print('Then we populate it')
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
squareArray = create2DArray(3, 3)
squareArray = [ [9,8,7], [6,5,4], [3,2,1] ]
prettyPrintArray(squareArray)
columnLen = len(squareArray[0])
rowLen    = len(squareArray)
print(f'length of rows = {rowLen}')
print(f'length of each column = {columnLen}\n')
print('First column (index 0) of the array above: ', end='')
printColumn(squareArray, 0)
print('Last row (len(array)-1) of the array above: ', end='')
printRow(squareArray, len(squareArray)-1)
print('Diagonal of the array above: ', end='')
printDiagonal(squareArray)
print()

# "mirror" an array
print('Horizontal mirroring')
printArray(squareArray)
print()
horizontal:list = hMirror(squareArray)
printArray(horizontal)
print()

print('Verical mirroring')
printArray(squareArray)
print()
vertical:list = vMirror(squareArray)
printArray(vertical)
print()

# transpose an array
print('Transposing')
transposed:list = transpose(another2dArray)
prettyPrintArray(another2dArray)
prettyPrintArray(transposed)
print()

# Davi's question - processing a 2D array by column (let's do the rows first):
print('\nProcessing an array')
prettyPrintArray(squareArray)
print('Processing rows:')
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
