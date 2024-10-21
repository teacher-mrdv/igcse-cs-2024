a = int(input('A = '))
b = int(input('B = '))
# make copies of a and b for processing
x = a
y = b

while x != y:
    if x > y:
        x = x-y
    if y>x:
        y = y-x
hcf = x

print(f'HCF of {a} and {b} = {hcf}')
lcm = (a*b) / hcf
print(f'LCM of {a} and {b} = {lcm}')