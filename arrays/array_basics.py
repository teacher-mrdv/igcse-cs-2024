# Python arrays basics
# Here we use lists to simulate arrays

# this method creates a ONE dimensional array of the specified 'length'
# and initialises the array with the given 'initialValue'
# the data type of the array will match the data type of 'initialValue'
def createArray(length, initialValue) -> list:
    temp: list = []
    for times in range(length):
        temp.append(initialValue)
    return temp

def inputElements(array):
    for index in range(len(array)):
        print(f'Enter element {index}: ', end='') 
        array[index] = input()
        print(array) # see how the array is being populated (length versus size)
    
# task 3: write an algorithm that returns the amount of even numbers in an array (assume the array is made of integers)
def evens(array) -> int:
    

# task 4: write an algorithm that returns the amount of odd numbers in an array (assume the array is made of integers)
def odds(array) -> int:
    

# task 5: write an algorithm that returns the smallest number in the array
def minimum(array) -> int:
    

# task 6a: write an algorithm that returns the number of vowels of a word (string)
def vowels(word: str) -> int:
    

# task 7a: write an algorithm that returns the number of vowels of all the words in an array (of strings)
def vowels(array: list) -> int:
    
    
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
print(len(randomNumbers))
# task 1: print the first element of arr1d
print(arr1d[0])
# task 2: print the last element of the 'randomNumbers' array, without using a literal (number) for the index. Use your knowledge from task 0.
print(randomWords[ len(randomWords)-1] ) # when the index starts from zero
# task 3:
print( evens(randomNumbers) )

# task 4:
print( odds(randomNumbers) )

# task 5:
print( minimum(randomNumbers) )

# task 6b: print the number of vowels of the word 'percentage' from the array 'randomWords'


# task 7b: print the number of vowels of the words in the array 'randomWords'




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