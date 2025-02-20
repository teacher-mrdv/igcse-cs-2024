######################################################
# Basic statistics with Pyhton						 #
######################################################
#													 #
# https://fstring.help/cheat/						 #
# https://www.geeksforgeeks.org/list-methods-python/ #
#													 #
######################################################


# float type check: returns True if the string contains a valid number/float, False otherwise
def isFloat(string:str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False

# Returns the smallest value in a list of numbers
def maximum(numbers:list) -> float:
    maximum = numbers[0]
    for i in range(1, len(numbers)):	# why starting the range from 1?
        if numbers[i] > maximum:
            maximum = numbers[i]
    return maximum

#######################################################################
# CHALLENGE:
# Complete the methods to calculate the average of a list of numbers
# smallest value (minimum), and the range.
# They should take a list of numbers as parameter, and return a float
# Like the maximum function above.
#######################################################################



#----------------------------------------------------------------------
number:float = -1  # default value to go into the while loop
precision:int = 3
numbersList = []
while number != 0: # rogue value to stop inputting numbers
    num:str = input('Enter a number (0 ends): ')
    while not isFloat(num): # float type validation check
        num = input('Enter a valid number (0 ends): ')
    number  = float(num)
    numbersList.append(number)
    print(numbersList)		# see how the list changes as we add numbers
if 0 in numbersList:		# easy way to check if an element is in the list
    numbersList.remove(0)	# remove the zero we input at the end
print('\nStats:')
print(numbersList)
print(f'Maximum = {maximum(numbersList):.{precision}f}')
#print(f'Minimum = {minimum(numbersList):.2f}')		# the number of decimals can also...
#print(f'Average = {average(numbersList):.{precision}f}')
#print(f'Range   = {range(numbersList):.2f}')		# be hard-coded with a literal (number)

