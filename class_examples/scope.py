# https://www.geeksforgeeks.org/python-scope-of-variables/

def repeatString(text: str, times): 
    output: str = text * times
    print('globalString', globalString)
    print('inside the repeatString function (text, times, output): ', text, times, output)
    return output


for i in range(1, 10):
    print('i = ', i, end = ' ')
print()
print('last value of i = ', i)
#print(text, times, output) # not defined error~!
text = 'hello'
times = 'straits'
output = '!!!'
globalString:str = 'global variable'
print()
print('outside the repeatString function (text, times, output): ', text, times, output)
print('repeatString(\'Hola\', 5): ', repeatString('Hola', 5))
