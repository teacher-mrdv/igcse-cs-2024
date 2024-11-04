'''
Division Method
https://www.math-only-math.com/methods-of-prime-factorization.html

(Start with 2 as the smallest prime)
Divide the number by the smallest prime number which divides the number exactly (number modulo smallest_prime = 0).
Divide the quotient again by the smallest or the next smallest prime number if it is not exactly divisible by the smallest prime number.
Repeat the process until the quotient becomes 1.

'''

number = int(input('Enter a number: '))
factor = 2
print('Prime factors :')
while number > 1:
    if number % factor == 0:
        print(factor, end = ' ')
        number = number // factor
    else:
        factor = factor + 1
