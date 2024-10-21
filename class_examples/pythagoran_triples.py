##################################################################
# This program inputs and validates 3 integers and tells whether
# they are Pythagorean triples or not
# MRDV class example 2024.10
##################################################################

# input three integers: a, b & c
a = input('Enter a = ')
a = int(a)		# replace int(n) with float(n) for decimals/real numbers
# convert the input to an integer and validate the input to ensure a > 0
while a<=0:
    # a shorter/'nested' way to input an integer
    a = int( input('Enter a = ') )
    
b = int( input('Enter b = ') )
# validate the input to ensure b > 0
while b <= 0:
    b = int( input('Enter b = ') )

c = int( input('Enter c = ') )
# validate the input to ensure c > 0
while c <= 0:
    c = int( input('Enter c = ') )

# print with format; {variable} outputs the value/content of the variable to the screen
print(f'You entered a = {a} , b = {b} and c = {c}')

# this is a boolean variable: it can be true or false, depending on the comparison
# for Pythagorean triples: e.g. 3**2 + 4**2 == 5**2? does 9+16 equal 25?
pythagoran_triples = a**2 + b**2 == c**2

# output a, b & c and end the line with a space
# (as opposed to the default of \n which makes the program start printing on the next line)
print(a, b, c, end=' ')

if pythagoran_triples:	# this can also be written as... if pythagoran_triples == True:
    print('are Pythagorean triples')
else:
    print('are not Pythagorean triples')
