"""
Write a function that accepts an integer and returns its corresponding
day of the week (e.g. 1=Monday, 7=Sunday). don't forget to validate the integer

Write a function to translate an English day of the week to another language
hints for lists challenge
"""
# finds the longest length in a list of strings, from demo
def longestStrInList(stringList:list) -> int :
    longest:int = 0
    wordLength:int = 0
    for word in stringList:
        wordLength = len(word)
        if wordLength > longest:
            longest = wordLength
    return longest

def dayOfTheWeek(dayNumber:int) -> str:
    daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 
                     'Sunday']
    # your code goes here!

    
def translateFromEnglish(day:str) -> str:
    daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 
                     'Sunday']
    # your code goes here!
    return 'Error'


# tests
for i in range(-1, 9):
    print( dayOfTheWeek(i) )

print()

daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 
                 'Sunday']
length = longestStrInList(daysOfTheWeek)
for day in daysOfTheWeek:
    print(f'{day:{length}} = {translateFromEnglish(day)}' )

"""
Expected output:

Invalid day number
Invalid day number
Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
Invalid day number

Monday    = lunes
Tuesday   = martes
Wednesday = miercoles
Thursday  = jueves
Friday    = viernes
Saturday  = sabado
Sunday    = domingo
"""
