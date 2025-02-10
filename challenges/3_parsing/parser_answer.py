"""
Write 2 methods to parse check whether a string can be a fraction
or an x,y point and return True if they are valid, otherwise False
Then we write functions to get the numerator and denominator/ x and y
if the strings are valid

--> hints for parsing problems
"""

def isFloat(string:str) -> bool:   			# float type check
    try:
        float(string)
        return True
    except ValueError:
        return False

def isFraction(fraction:str) -> bool:		# format check
    fraction = fraction.replace(' ', '')
    fraction_split = fraction.find('/')
    if fraction_split == -1:
        return False
    numerator:str   = fraction[:fraction_split]
    denominator:str = fraction[fraction_split+1:]
    return numerator.isnumeric() and denominator.isnumeric() # type check (int)

def getNumerator(fraction:str) -> int:
    # if it's a valid fraction (isFraction returns true)...
    fraction = fraction.replace(' ', '')
    fraction_split = fraction.find('/')
    numerator = int(fraction[:fraction_split])
    return numerator

def getDenominator(fraction:str) -> int:
    # if it's a valid fraction (isFraction returns true)...
    fraction = fraction.replace(' ', '')
    fraction_split:int = fraction.find('/')
    denominator = int(fraction[fraction_split+1:])
    return denominator

def isValidFraction(fraction:str) -> bool:
    """if isFraction(fraction):
        return getDenominator(fraction) != 0
    return False"""
    return isFraction(fraction) and (getDenominator(fraction) != 0)

def isCoords(coordinates:str) -> bool:
    coordinates = coordinates.replace(' ', '')
    coordinate_split:int = coordinates.find(',')
    x:str = coordinates[:coordinate_split]
    y:str = coordinates[coordinate_split+1:]
    return isFloat(x) and isFloat(y)

def getX(coordinates:str) -> float:
    # call the isCoords function before calling this one
    coordinates = coordinates.replace(' ', '')
    coordinate_split:int = coordinates.find(',')
    x:float = float(coordinates[:coordinate_split])
    return float(x)

def getY(coordinates:str) -> float:
    # call the isCoords function before calling this one
    coordinates = coordinates.replace(' ', '')
    coordinate_split:int = coordinates.find(',')
    y:float = float(coordinates[coordinate_split+1:])
    return float(y)


# testing - fraction input and validation
fraction1 = input('Enter a fraction in n/m format: ')
while not isValidFraction(fraction1):
    fraction1 = input('Error in input. Enter a fraction in N/M format with M non 0: ')
num1 = getNumerator(fraction1)
den1 = getDenominator(fraction1)
print(f'{num1}/{den1}')

# testing - coordinates input and validation
SFS = 3 # significant figures --read https://realpython.com/how-to-python-f-string-format-float/
pointA = input('Enter a point in x,y format: ')
while not isCoords(pointA):
    pointA = input('Error in input. Enter a point in X,Y format: ')
x1 = getX(pointA)
y1 = getY(pointA)
print(f'P({x1:.{SFS}f}, {y1:.{SFS}f})')
