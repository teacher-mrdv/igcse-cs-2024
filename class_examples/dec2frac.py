x = float(input("Decimal = "))
y = x
c = 0
while y-int(y) > 0:
    y=y*10
    c=c+1
print(c)
denom = 10**c
numer = x * denom
print(int(numer), '/', denom)
