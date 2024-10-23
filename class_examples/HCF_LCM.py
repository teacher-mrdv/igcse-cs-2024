a = int(input('A = '))
b = int(input('B = '))
# make copies of a and b for processing
x = a
y = b

while not (x == y):	# or x != y ; != means not equal to
    if x > y:
        x = x-y
    if y > x:
        y = y-x
#    print(x, y)
hcf = x

print(f'HCF of {a} and {b} = {hcf}')
lcm = (a*b) // hcf
print(f'LCM of {a} and {b} = {lcm}')