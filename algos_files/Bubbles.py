##
# Python example code to showcase the BUBBLE SORT algorithm
# Note that these algorithms sort in **ascending** order
# * -> not part of the actual algorithm
##

import copy

def bubble_sort1(array: list) -> list:
    swaps: int = 0    # for testing purposes ONLY *
    for passes in range(len(array)):
        for index in range(len(array) - 1):
            if array[index] > array[index + 1]:
                temp = array[index]         # swap
                array[index] = array[index + 1]
                array[index + 1] = temp
                swaps += 1                  # for testing purposes ONLY *
                print('\t\tSwap:', array)        # for testing purposes ONLY *
    print(f'\t< BUBBLE SORT #1 > Passes = {passes}, swaps = {swaps}') # for testing purposes ONLY *
    return array

def bubble_sort2(array: list) -> list:
    swaps: int = 0  # for testing purposes ONLY *
    for passes in range(len(array)):
        for index in range(len(array) - 1 - passes):
            if array[index] > array[index + 1]:
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
                swaps += 1              # for testing purposes ONLY *
                print('\t\tSwap:', array)    # for testing purposes ONLY *
    print(f'\t< BUBBLE SORT #2 > Passes = {passes}, swaps = {swaps}')  # *
    return array

def bubble_sort3(array: list) -> list:
    swaps: int = 0  # for testing purposes ONLY *
    swapped: bool = True
    passes: int = 0
    while swapped:
        swapped = False
        index: int = 0
        for index in range(len(array) - 1 - passes):
            if array[index] > array[index + 1]:
                temp = array[index]
                array[index] = array[index + 1]
                array[index + 1] = temp
                swapped = True
                swaps += 1              # for testing purposes ONLY *
                print('\t\tSwap:', array)    # for testing purposes ONLY *
        passes += 1
    print(f'\t< BUBBLE SORT #3 > Passes = {passes}, swaps = {swaps}')  # *
    return array

### main section of our code
#
already_sorted: list = [1,2,3,4,5]
nearly_sorted: list = [1,2,5,3,4]
reversed_sorted: list = [5,4,3,2,1]
random_sorted: list = [3,1,2,5,4]

print('\n<<< BUBBLE SORT #1 >>>')
print('\tSorted data set:', already_sorted)
to_sort = copy.deepcopy(already_sorted)
print('\tResult:', bubble_sort1(to_sort))
print()
print('\tNearly sorted data set:', nearly_sorted)
to_sort = copy.deepcopy(nearly_sorted)
print('\tResult:', bubble_sort1(to_sort))
print()
print('\tReversed data set:', reversed_sorted)
to_sort = copy.deepcopy(reversed_sorted)
print('\tResult:', bubble_sort1(to_sort))
print()
print('\tRandomly sorted data set:', random_sorted)
to_sort = copy.deepcopy(random_sorted)
print('\tResult:', bubble_sort1(to_sort))

print('\n<<< BUBBLE SORT #2 >>>')
print('\tSorted data set:', already_sorted)
to_sort = copy.deepcopy(already_sorted)
print('\tResult:', bubble_sort2(to_sort))
print()
print('Nearly sorted data set:', nearly_sorted)
to_sort = copy.deepcopy(nearly_sorted)
print('\tResult:', bubble_sort2(to_sort))
print()
print('\tReversed data set:', reversed_sorted)
to_sort = copy.deepcopy(reversed_sorted)
print('\tResult:', bubble_sort2(to_sort))
print()
print('\tRandomly sorted data set:', random_sorted)
to_sort = copy.deepcopy(random_sorted)
print('\tResult:', bubble_sort2(to_sort))

print('\n<<< BUBBLE SORT #3 >>>')
print('\tSorted data set:', already_sorted)
to_sort = copy.deepcopy(already_sorted)
print('\tResult:', bubble_sort3(to_sort))
print()
print('\tNearly sorted data set:', nearly_sorted)
to_sort = copy.deepcopy(nearly_sorted)
print('\tResult:', bubble_sort3(to_sort))
print()
print('\tReversed data set:', reversed_sorted)
to_sort = copy.deepcopy(reversed_sorted)
print('\tResult:', bubble_sort3(to_sort))
print()
print('\tRandomly sorted data set:', random_sorted)
to_sort = copy.deepcopy(random_sorted)
print('\tResult:', bubble_sort3(to_sort))

