def isHex(hexNumber: str) -> bool:
    hexDigits: list = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C', 'D', 'E', 'F']
    for index1 in range(len(hexNumber)):
        if not(hexNumber[index1] in hexDigits):
            return False
    return True 

number: str = input('Input a number in hexadecimal base: ').upper()
message: str = 'Error'
if isHex(number):
    message = 'a valid'
else:
    message = 'an invalid'
    
print(f'{number} is {message} hexadecimal number', number, message)
