def average(numbers:list) -> float:
    avg:float = 0
    for n in numbers:
        avg = avg + n
    return avg/len(numbers)

def maximum(numbers:list) -> float:
    maximum:float = 0
    for n in numbers:
        if n > maximum:
            maximum = n
    return maximum


#----------------------------------------------------------
number:float = -1
numbersList = []
while number != 0: # rogue value to stop inputting numbers
    num:str = input('Enter a number (0 ends): ')
    while not num.isnumeric():
        num:str = input('Enter a valid number (0 ends): ')
    number:float = int(num)
    numbersList.append(number)
    print(numbersList)
numbersList.remove(0) # remove the zero we input at the end
print(numbersList)
print(f'Average = {average(numbersList):.2f}')
print(f'Maximum = {maximum(numbersList):.2f}')
#print(f'Minimum = {mximum(numbersList):.2f}')
#print(f'Range   = {range(numbersList):.2f}')
