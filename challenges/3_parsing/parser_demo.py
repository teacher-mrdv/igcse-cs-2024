"""
Parsing strings demo

https://docs.python.org/3.10/library/stdtypes.html?highlight=find#str.find
https://docs.python.org/3.10/library/stdtypes.html?highlight=isnumeric#str.isnumeric
https://docs.python.org/3.10/library/string.html?highlight=string#module-string
https://www.geeksforgeeks.org/python-string/
https://www.geeksforgeeks.org/string-slicing-in-python/

"""
def isFloat(string:str) -> bool:
    try:
        float(string)
        return True
    except ValueError:                  # tried TypeError, with worse results
        return False


fraction:str = '3 / 4'
fraction = fraction.replace(' ', '')      # remove all spaces from input
fraction_split:int   = fraction.find('/') # find the index of the / find returns -1 if not found

coordinates:str = ' 7.25, -9.67 '
coordinates = coordinates.replace(' ', '')
coordinate_split:int = coordinates.find(',')

print(fraction_split)                   # output: 1
print(coordinate_split)                 # output: 4

numerator   = fraction[:fraction_split]
denominator = fraction[fraction_split+1:]
print(numerator)                        # output: 3
print(denominator)                      # output: 4

x = coordinates[:coordinate_split]
y = coordinates[coordinate_split+1:]
print(x)                                # output: 7.25
print(y)                                # output: -9.67

print(numerator.isnumeric())            # output: True
print(denominator.isnumeric())          # output: True

print( isFloat(x) )                     # output: True
print( isFloat(y) )                     # output: True

print(type(x))                          # output: <class 'str'>

