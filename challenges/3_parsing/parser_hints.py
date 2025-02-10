"""
Now write 2 methods to parse check whether a string can be a fraction
or an x,y point and return True if they are valid, otherwise False
Then we write functions to get the numerator and denominator/ x and y
if the strings are valid

--> hints for parsing problems
"""

def isFloat(str:str) -> bool:   # from demo
    try:
        float(str)
        return True
    except ValueError:
        return False

def isFraction(fraction:str) -> bool:
    ## Your code goes here

def getNumerator(fraction:str) -> int:
    ## Your code goes here
    

def getDenominator(fraction:str) -> int:
    #call isFraction before calling this one
    ## Your code goes here

def isCoords(coordinates:str) -> bool:
    ## Your code goes here
    return isFloat(x) and isFloat(y)

def getX(coordinates:str) -> float:
    # call the isCoords function before calling this one
    ## Your code goes here
    return float(x)

def getY(coordinates:str) -> float:
    # call the isCoords function before calling this one
    ## Your code goes here


# testing
fractions   = [ ' 3 / 4 ', ' 3 \ 8 ', '.1/2' ]
coordinates = [ '7 .25, -9.67', ' 7,25, -9,67 ', '5,4' ]

for f in fractions:
    if isFraction(f):
        print(f'{getNumerator(f)}/{getDenominator(f)}')
    else:
        print('Not a fraction')
        
for c in coordinates:
    if isCoords(c):
        print(f'{getX(c)}/{getY(c)}')
    else:
        print('Not a coordinate pair')

"""
OUTPUT should be:
    3/4
    Not a fraction
    Not a fraction
    7.25/-9.67
    Not a coordinate pair
    5.0/4.0
"""
