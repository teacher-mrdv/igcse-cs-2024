"""
Python functions, lists and match/case demo

references
https://docs.python.org/3.10/tutorial/inputoutput.html
https://mypy.readthedocs.io/en/stable/cheat_sheet_py3.html
https://www.geeksforgeeks.org/python-lists/
https://www.geeksforgeeks.org/pad-or-fill-a-string-by-a-variable-in-python-using-f-string/
https://www.geeksforgeeks.org/python-remove-spaces-from-a-string/

"""

# try to CLear the SCReen by printing 25 new lines
def clscr() -> None:
    print('\n' * 25)
    
# finds the longest length in a list of strings
def longestInList(stringList:list) -> int :
    longest:int = 0
    wordLength:int = 0
    for word in stringList:
        wordLength = len(word)
        if wordLength > longest:
            longest = wordLength
    return longest

# our list for this example
daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 
                 'Sunday']

# 2 different ways to output it with for loops:
dayNumber:int = 1
for day in daysOfTheWeek:
    print(f'{dayNumber} = {day}')
    dayNumber = dayNumber + 1
print()
    
for dayNumber in range(len(daysOfTheWeek)):
    print(f'{dayNumber+1} = {daysOfTheWeek[dayNumber]}')
print()

d = int(input('Enter a day (1=Monday...7=Sunday): '))
while d < 1 or d > 7:   #range check
    d = int(input('Error in input. Enter a day ( 1<= day <= 7 ): '))

match d:
    case 1:
        print(daysOfTheWeek[0])
    case 2:
        print(daysOfTheWeek[1])
    case 3:
        print(daysOfTheWeek[2])
    case 4:
        print(daysOfTheWeek[3])
    case 5:
        print(daysOfTheWeek[4])
    case 6:
        print(daysOfTheWeek[5])
    case 7:
        print(daysOfTheWeek[6])
    case _:
        print('Error in input (1~7)!')  # just in case!

clscr()

print('Lets get international! Enter your [first/second] language equivalents to...')
diasDeLaSemana = []
length = longestInList(daysOfTheWeek)
for day in daysOfTheWeek:
    print(f'{day:{length}} = ', end = '')
    dia = input()
    diasDeLaSemana.append(dia)

print()
length = longestInList(diasDeLaSemana)
for index in range( len(diasDeLaSemana) ):
    print(f'{diasDeLaSemana[index]:{length}} = {daysOfTheWeek[index]}')
    
