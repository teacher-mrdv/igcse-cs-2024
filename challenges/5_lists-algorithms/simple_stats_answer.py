'''
Basic statistics with Pyhton
https://fstring.help/cheat/
https://www.geeksforgeeks.org/list-methods-python/
'''

def average(numbers:list) -> float:
    avg:float = 0
    for n in numbers:
        avg = avg + n
    return avg/len(numbers)

def maximum(numbers:list) -> float:
    maximum:float = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > maximum:
            maximum = numbers[i]
    return maximum

def minimum(numbers:list) -> float:
    minimum:float = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < minimum:
            minimum = numbers[i]
    return minimum

def rangeValue(numbers:list) -> float:
    return maximum(numbers) - minimum(numbers)

# float type check
def isFloat(string:str) -> bool:
    try:
        float(string)
        return True
    except ValueError:
        return False
    
#----------------------------------------------------------
number:float = -1
precision:int = 3
numbersList = []
while number != 0: # rogue value to stop inputting numbers
    num:str = input('Enter a number (0 ends): ')
    while not isFloat(num):	# float type check
        num = input('Enter a valid number (0 ends): ')
    number = float(num)
    numbersList.append(number)
    print(numbersList)
if 0 in numbersList:
    numbersList.remove(0) # remove the zero we input at the end
print('\nStats:')
print(numbersList)
print(f'Average = {average(numbersList):,.{precision}f}')
print(f'Maximum = {maximum(numbersList):,.{precision}f}')
print(f'Minimum = {minimum(numbersList):,.{precision}f}')
print(f'Range   = {rangeValue(numbersList):,.{precision}f}')
