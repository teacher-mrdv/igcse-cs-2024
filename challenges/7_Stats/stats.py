# Stats
import random

def minimum(d :list[int]) -> int :
    minimum :int = d[0]
    for index in range(1, len(d)):
        if d[index] < minimum:
            minimum = d[index]
    return minimum

def maximum(d :list[int]) -> int:
    maximum :int = d[0]
    # your code goes here
    return maximum

def list_range(d :list[int]) -> int:
    # your code goes here

def median(d :list[int]) -> float:
    median :float = 0
    d.sort()
    # your code goes here
    return median

# This is called a PROCEDURE instead of a function, ...
# ...because it returns nothing (None)
def print_stats(d :list[int]) -> None:
    print( 'Data = ', d )
    print( 'Maximum: ', minimum(d) )
    print( 'Minimum: ', maximum(d) )
    print( 'Range  : ', list_range(d) )
    print( 'Median : ', median(d) )
    
# main
data1 :list[int] = [5, 7, 1, 3, 9]
print_stats(data1)
print()
# generates a list of 10 integers between 1 and 99
random_data :list[int] = random.sample(range(1, 100), 10)
print_stats(random_data)

