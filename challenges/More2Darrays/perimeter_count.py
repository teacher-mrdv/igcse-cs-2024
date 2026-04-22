array2D = [ [True, True, False, True, False, True, True, False, False, True],
            [False, True, True, True, True, False, False, True, True, False],
            [False, True, True, False, True, True, False, True, False, False],
            [False, True, True, True, True, False, True, True, True, False],
            [True, True, False, True, True, True, True, False, False, True],
            [False, True, False, False, True, False, True, True, False, False],
            [True, False, True, False, False, True, False, False, False, True],
            [True, False, False, True, True, True, False, True, False, False],
            [False, False, True, True, True, True, False, True, False, False],
            [True, True, False, True, True, False, True, True, True, False] ]

#import random
#rows = 10
#cols = 10
# Generate a 2D list using list comprehension and random.choice
#array2D = [[random.choice([True, False]) for c in range(cols)] for r in range(rows)]

# Print the 2D array to see the structure
for row in array2D:
    for col in row:
        print(f"{col!s:^5} ", end=' ')
    print()

def perimeter_count(array: list):
    total: int = 0
    for column in range(len(array)):
        if array[0][column]:
            total += 1
        if array[len(array)-1][column]:
            total += 1
    for row in range(1, len(array[0])-1):
        if array[row][0]:
            total += 1
        if array[row][len(array)-1]:
            total += 1
        
    return total

print()
print( perimeter_count(array2D) )