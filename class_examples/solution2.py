a = 0
b = 0
c = 0
while not(a + b > c and b + c > a and a + c > b):
    a = float(input('A = '))
    while a <= 0:
        print('Error - A must be positive, non zero!')
        a = float(input('A = '))

    b = float(input('B = '))
    while b <= 0:
        print('Error - B must be positive, non zero!')
        b = float(input('B = '))

    c = float(input('C = '))
    while c <= 0:
        print('Error - C must be positive, non zero!')
        c = float(input('C = '))


print(f'{a}, {b} and {c}', end=' ')
if a + b > c and b + c > a and a + c > b:
    print('can be sides of a triangle', end=', ')
else:
    print('can not be sides of a triangle', end=', ')
#end if
    
if a**2 + b**2 == c**2:
    print('and are also Pythagorean triples.')
else:
    print('and are not Pythagorean triples.')
#end if

