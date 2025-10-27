# Your code/functions may go here


# this method creates a two-dimensional array of the specified dimensions
# (rows and columns), and initialises the array with 0s
# PSEUDOCODE equivalent:
# DECLARE Temp : ARRAY[0:Rows, 0:Columns] OF INTEGER
def create2DArray(rows, columns) -> list:
    # best way to create a 2D array-like data structure in Python
    temp: list = [[0] * columns for r in range(rows)]
    return temp

# visualise the 2D-array in a user-friendly way
def printArray(array: list):
    rowLength:int = len(array)
    columnLength:int = len(array[0])
    print('    0 1 2 3 4 5 6 7  8 9')        # optional
    for rowIndex in range(rowLength):
        print(f'{rowIndex}: ', end = ' ')    # optional
        for colIndex in range(columnLength):
            print(array[rowIndex][colIndex], end=' ')
            if colIndex == len(array[0])-3:
                print(' ', end='')
        if rowIndex == len(array)-3:
            print()
        print()


### main ###
# arrayOK includes extra columns both given and calculated parity bits
# and rows for the given and calculated parity blocks
arrayOK: list  = create2DArray(7, 10)
# arrayBad includes extra columns both given and calculated parity bits
# and rows for the given and calculated parity blocks
arrayBad: list = create2DArray(7, 10)
arrayOK = [ [1,0,1,1,0,0,1,0,0,0],
            [0,1,1,0,1,1,0,1,1,0],
            [1,1,0,0,1,0,0,0,1,0],
            [0,0,0,1,1,1,1,0,0,0],
            [1,0,1,0,0,0,0,1,1,0],
            [1,0,1,0,1,0,0,0,1,0],
            [0,0,0,0,0,0,0,0,0,0] ]

arrayBad =  [ [1,0,1,1,0,0,1,0,0,0],
              [0,1,1,0,1,1,0,1,1,0],
              [1,1,0,0,1,0,0,0,1,0],
              [0,0,0,1,0,1,1,0,0,0],
              [1,0,1,0,0,0,0,1,1,0],
              [1,0,1,0,1,0,0,0,1,0],
              [0,0,0,0,0,0,0,0,0,0] ]

print("Error-free test data:")
printArray(arrayOK)
print("\n\nTest data with error:")
printArray(arrayBad)
