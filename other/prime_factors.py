'''
Division Method
https://www.math-only-math.com/methods-of-prime-factorization.html

(Start with 2 as the smallest prime)
Divide the number by the smallest prime number which divides the number exactly (number modulo smallest_prime = 0).
Divide the quotient again by the smallest or the next smallest prime number if it is not exactly divisible by the smallest prime number.
Repeat the process until the quotient becomes 1.

'''
def primefactors(n:int) -> list:
    primefactors = []
    factor = 2
    while n > 1:
        if n % factor == 0:
            primefactors.append(factor)
            n = n // factor
        else:
            factor = factor + 1
    return primefactors

def validate(n:str) -> bool:
    return n.isnumeric() and int(n) > 0

number:str = input('Enter a number (positive integer): ')
while( not validate(number) ):
    number = input('Error-Enter a positive integer number: ')
num:int = int(number)

print('Prime factors :')
print( primefactors(num) )