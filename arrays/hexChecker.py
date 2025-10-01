# isHex() uses the advantage of Python's IN keyword
def isHex(hexNumber: str) -> bool:
    # array with all valid hexadecimal digits
    hexDigits: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for index1 in range(len(hexNumber)):
        # we use string slicing to check if any character of hexNumber is...
        # ...NOT a valid hexadecimal digit
        if not(hexNumber[index1] in hexDigits):
            return False
    return True

# the version below will be easier to port to pseudocode
def isHexP(hexNumber: str) -> bool:
    # array with all valid hexadecimal digits
    hexDigits: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for index1 in range(len(hexNumber)):
        ok: bool = False
        for index2 in range(len(hexDigits)):
            # in pseudocode, we can't use slicing []; the comparison below is
            #  SUBSTRING(hexNumber, index1, 1) == hexDigits[index2]
            if hexNumber[index1] == hexDigits[index2]:
                ok = True
        if not ok:
            return False
    return True

number: str = input('Input a number in hexadecimal base: ').upper()
message: str = ''
if isHexP(number):
    message = 'a valid'
else:
    message = 'an invalid'
    
#print(str(number) + ' is ' + message + ' hexadecimal number.')
print(f'{number} is {message} hexadecimal number.\n')
