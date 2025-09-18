###
# Python arrays basics
# Here we use lists to simulate arrays
# expected output at the end of the code vvv>>> %Run array_basics.py
###

# this method creates a ONE dimensional array of the specified 'length'
# and initialises the array with the given 'initialValue'
# the data type of the array will match the data type of 'initialValue'
def createArray(length, initialValue) -> list:
    temp: list = [initialValue] * length
    return temp

# function to populate the array 'array'. 'array' should have already been initialised with the desired length
def inputElements(array):
    for index in range(len(array)):
        print(f'Enter element {index}: ', end='') 
        array[index] = input()
        print(array) # see how the array is being populated (length versus size)
    
# task 3: write an algorithm that returns the amount of even numbers in an array (assume the array is made of integers)
def evens(array) -> int:
    evenCounter: int = 0
    for element in array:
        if element % 2 == 0:
            evenCounter = evenCounter + 1
    return evenCounter

# task 4: write an algorithm that returns the amount of odd numbers in an array (assume the array is made of integers)
def odds(array) -> int:
    length = len(array)
    return length - evens(array)

# or, alternatively...
# def odds(array) -> int:
#     length: int = len(array)
#     oddCounter: int = 0
#     for index in range(length):
#         if array[index] % 2 != 0:
#             oddCounter = oddCounter + 1
#     return oddCounter

# task 5: write an algorithm that returns the smallest number in the array
def minimum(array) -> int:
    length: int = len(array)
    minimo: int = array[0]
    for index in range(1, length):
        if array[index] < minimo:
            minimo = array[index]
    return minimo

# task 6a: write an algorithm that returns the number of vowels of a word (string)
def countVowels(word: str) -> int:
    vowelsList: list = ['a', 'e', 'i', 'o', 'u']
    counter: int = 0
    length: int = len(word)
    for index in range(length):
        if word[index].lower() in vowelsList:
            counter = counter + 1
    return counter
# or, alternatively...
# def countVowels(word: str) -> int:
#     vowelsList: list = ['a', 'e', 'i', 'o', 'u']
#     counter: int = 0
#     for character in word:
#         if character.lower() in vowelsList:
#             counter = counter + 1
#     return counter

# task 7a: write an algorithm that returns the number of vowels of all the words in an array (of strings)
def allVowels(array: list) -> int:
    total: int = 0
    length: int = len(array)
    for index in range(length):
        total = total + countVowels(array[index])
    return  total

# def allVowels(array: list) -> int:
#     total: int = 0
#     for word in array:
#         total = total + countVowels(word)
#     return  total

    
### Main program ###
# https://docs.python.org/3/library/random.html#functions-for-sequences
randomNumbers = [95, 11, 39, 43, 55, 9, 61, 79, 21, 6, 19, 64, 51, 25, 93, 33, 90, 73, 3, 67, 96, 2, 24, 52, 34, 28, 46, 69, 49, 97, 82, 31, 13, 32, 36, 22, 38, 92, 12, 29, 1, 72, 56, 71, 20, 54, 66, 94, 40, 41, 89, 62]
randomWords   = ['sector', 'paper', 'clothes', 'percentage', 'magazine', 'hotel', 'county', 'effort', 'map']
# DECLARE arr1d : ARRAY[0:4] OF INTEGER
arr1d = createArray(5, 0)
print(f'Array = {arr1d}    length = {len(arr1d)}')
inputElements(arr1d)
print(arr1d)
                          
# task 0: print the length of the 'randomNumbers' array (Python list)
print( len(randomNumbers) )
                          
# task 1: print the first element of arr1d
print( arr1d[0] )

# task 2: print the last element of the 'randomNumbers' array, without using a literal (number) for the index. Use your knowledge from task 0.
print( randomNumbers[ len(randomNumbers)-1] )

# task 3:
print( evens(randomNumbers) )

# task 4:
print( odds(randomNumbers) )

# task 5:
print( minimum(randomNumbers) )

# task 6b: print the number of vowels of the word 'percentage' from the array 'randomWords'
print( countVowels(randomWords[3]) )

# task 7b: print the total number of vowels of the all the words in the array 'randomWords'
print( allVowels(randomWords) )

### EXPECTED OUTPUT
#
# >>> %Run array_basics.py
# Array = [0, 0, 0, 0, 0]    length = 5
# Enter element 0: 1
# ['1', 0, 0, 0, 0]
# Enter element 1: 2
# ['1', '2', 0, 0, 0]
# Enter element 2: 3
# ['1', '2', '3', 0, 0]
# Enter element 3: 4
# ['1', '2', '3', '4', 0]
# Enter element 4: 5
# ['1', '2', '3', '4', '5']
# ['1', '2', '3', '4', '5']
# 52
# 1    <- this output depends on which integer you input first as element index 0
# 62
# 25
# 27
# 1
# 4
# 21
#
###