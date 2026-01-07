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
                temp = array[index]         # start swapping
                array[index] = array[index + 1]
                array[index + 1] = temp		# end swapping
                swaps += 1                  # for testing purposes ONLY *
                print('\t\tSwap:', array)   # for testing purposes ONLY *
        print('\tpass completed')
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
                swaps += 1              	# for testing purposes ONLY *
                print('\t\tSwap:', array)	# for testing purposes ONLY *
        print('\tpass completed')
    print(f'\t< BUBBLE SORT #2 > Passes = {passes}, swaps = {swaps}')  # *
    return array

def bubble_sort3(array: list) -> list:
    swaps: int = 0		# for testing purposes ONLY *
    passes: int = 0		# for testing purposes ONLY *
    swapped: bool = True
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
        print('\tpass completed')
    print(f'\t< BUBBLE SORT #3 > Passes = {passes}, swaps = {swaps}')  # *
    return array

# function that looks for a key inside of and array
# and returns the index of the key (first occurrence only if there are many),
# or -1 (arbitrary rogue value) if the key is not found.
# this is the linear search algorithm.
def linear_search(array: list, key: int) -> int:
    for index in range(len(array)):
        if array[index] == key:
            return index
    return -1

def search(array: list, key: int) -> None:
    print(f'Looking for {key} in the array')
    search_index: int = linear_search(to_sort, key)
    if search_index != -1:
        print(f'{key} found at index {search_index}')
    else:
        print(f'{key} was not found.')

def count_evens(array: list) -> int:
    count: int = 0
    for index in range(len(array)):
        if array[index] % 2 == 0:
            count += 1
    return count

### main section of our code
#
already_sorted: list = [1,2,3,4,5]
nearly_sorted: list = [1,2,5,3,4]
reversed_sorted: list = [5,4,3,2,1]
random_sorted: list = [3,1,2,5,4]

print('\n<<< BUBBLE SORT #1 >>>')
print('Sorted data set:', already_sorted)
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

print('\n<<< LINEAR SEARCH >>>')
search(to_sort, 3)
search(to_sort, 9)

print('\n<<< LINEAR SEARCH + counting >>>')
print(f'There are {count_evens(to_sort)} even numbers in the array')

