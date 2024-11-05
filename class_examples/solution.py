a = float(input('A = '))
b = float(input('B = '))
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

