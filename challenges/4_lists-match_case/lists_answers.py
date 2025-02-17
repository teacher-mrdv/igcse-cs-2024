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
    if dayNumber < 1 or dayNumber > 7:
        return 'Invalid day number'     # just in case!
    dayNumber = dayNumber - 1
    return daysOfTheWeek[dayNumber]
    
def translateFromEnglish(day:str) -> str:
    day = day.title()
    daysOfTheWeek = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 
                     'Sunday']
    diasDeLaSemana = ['lunes', 'martes', 'miercoles', 'jueves', 'viernes', 'sabado',
                      'domingo']
    for index in range(len(daysOfTheWeek)): # the lengths of both lists should be the same
        if day == daysOfTheWeek[index]:
            return diasDeLaSemana[index]
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