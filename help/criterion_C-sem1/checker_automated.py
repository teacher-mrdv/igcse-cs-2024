#
# Main version with hard coded values and manual automated testing
# (manaual input available, but commented out in the main section of the code)
#

def isValidBinary(digits: str) -> bool:
    # range check (only 0 / 1 accepted)
    for index in range(len(digits)):
        #  IF SUBSTRING(Digits, Index, 1) != '1' AND SUBSTRING(Digits, Index, 1) != '0' ...
        if digits[index] != '1' and digits[index] != '0':
            return False
    return True

# input and validate a 2D array
### function added and not originally designed/planned; handy as we can call it multiple times
### to input as many 2D arrays as needed; originally planned to be in the main section of the code
def input2Darray(binary: list):
    for row in range(6):
        if row < 5:
            print(f'Input row #{row}')
        else:
            print('Input the parity block')
        #endif
        while True :
            bits: str = input('\tEnter 9 bits (8 data bits + 1 even parity bit @ the end): ').strip()
            # range check (isValidBinary) and length check
            if isValidBinary(bits) and len(bits) == 9:
                break
            else:
                print('\tInput is not a valid binary number. Re-enter.')
            #endif
        for column in range(len(bits)):    # or for column in range(len(binary[0])-1):
            binary[row][column] = int(bits[column])
        #next column
        # we could also calculate the parity bit after we input each row
        #binary[row][9] = calculateParityBit(binary[row])
    #next row

# visualise the 2D-array in a user-friendly way
### function added and not originally designed/planned
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
        
# calculates the parity bit of a 1D array (list)/row of the 2D array of bits
def calculateParityBit(binary: list) -> int:
    sumOfBits: int = 0
    for index in range(len(binary)-2):
        if binary[index] == 1:
            sumOfBits = sumOfBits + 1
        #endif
    return sumOfBits % 2

# calculates the even parity block of the input
# 8 data bits + given parity bit
def calculateParityBlock(binary: list) -> list:
    block: list = [0] * len(binary[0])
    for column in range(len(binary[0])):
        sumOfBits:int = 0
        for row in range(len(binary)-2):
            if binary[row][column] == 1:
                sumOfBits = sumOfBits + 1
            #endif
        #next row
        block[column] = sumOfBits % 2
    #next column
    return block

# check the given parity bit with the calculated one of the 2D array (list) of bits (ints)
def checkParityBit(binary: list) -> int:
    # add the calculated parity bits on the 10th column of the 2D array 
    for row in range(len(binary)-1):
        binary[row][9] = calculateParityBit(binary[row])
    #for row in range(len(binary)-1):    # optional, actually redundant as the calculated parity bit can be calculated...
                                         # ...and compared with the given parity bit as it's calculated and...
                                         # ...added to the last column of each row
        if binary[row][8] != binary[row][9]:
            return row
    return -1

# check the given parity block with the calculated one of the 2D array (list) of bits (ints)
def checkParityBlock(binary: list) -> int:
    # calculate the parity block and add it to the 7th row of the 2D array
    binary[6] = calculateParityBlock(binary)
    for column in range(len(binary[0])):
        if binary[5][column] !=  binary[6][column]:
            return column
    return -1

# check for an even parity bit error and return its location in the array
### function added and not originally designed/planned
def checkForError(binary: list) -> str:
    result: str = 'No error found'
    binary[6] = calculateParityBlock(binary)
    rowCheck: int = checkParityBit(binary)
    columnCheck: int = checkParityBlock(binary)
    # check for parity bit errors in a row and column
    if rowCheck != -1 and columnCheck != -1:
        result = f'Error @ row {rowCheck} and column {columnCheck}'
    return result

# this helper function creates a two-dimensional array
# of specified dimensions (rows and columns), and initialises it with 0s
# PSEUDOCODE equivalent:
# DECLARE Temp : ARRAY[0:Rows, 0:Columns] OF INTEGER
# Python allows us to change the data type of the array (list) afterwards
def create2DArray(rows, columns) -> list:
    # best way to create a 2D array-like data structure in Python
    temp: list = [[0] * columns for row in range(rows)]
    return temp

### main ###
# these arrays have an additional column allowance for the calculated even parity bit
# and an additional row at the end for the calculated parity block
arrayOK: list  = create2DArray(7, 10)
arrayBad: list = create2DArray(7, 10)

#for testing purposes, as I don't want to manually input the data so many times
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


'''
# manual input of data
print('Input array with no errors')
input2Darray(arrayOK)
print('\nInput array with an error')
input2Darray(arrayBad)
print()
'''

# add calculated parity bits and parity block to error-free 2D array
checkParityBit(arrayOK)
arrayOK[6] = calculateParityBlock(arrayOK)
printArray(arrayOK)
print(checkForError(arrayOK))
print()
# add calculated parity bits and parity block to 2D array with error
checkParityBit(arrayBad)
arrayBad[6] = calculateParityBlock(arrayBad)
printArray(arrayBad)
print(checkForError(arrayBad))