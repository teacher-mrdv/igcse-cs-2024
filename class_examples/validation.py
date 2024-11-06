n = int( input('Enter an integer: ') )
d = int( input('Enter an integer other than zero: ') )
while d == 0:
    print('Error - the denominator cannot be zero!')
    d = int( input('Enter an integer other than zero: ') )
f = round(n/d, 3)
print(f'{n} / {d} = {f}')
