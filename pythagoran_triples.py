#a = input('Enter a = ')
#a = int(a)
#b = input('Enter b = ')
#b = int(b)
#c = int( input('Enter c = ') )
# replace int with float for decimals/real numbers
a = int( input('Enter a = ') )
b = int( input('Enter b = ') )
c = int( input('Enter c = ') )
# validations for a,b,c integers > 0
while a<=0:
    a = int( input('Enter a = ') )
while b<=0:
    b = int( input('Enter b = ') )
while c<=0:
    c = int( input('Enter c = ') )
print(f'You entered a = {a} , b = {b} and c = {c}')

pythagoran_triples = a**2 + b**2 == c**2
print(a, b, c, end=' ')
if pythagoran_triples:
    print('are pythagorean triples')
else:
    print('are not pythagorean triples')
