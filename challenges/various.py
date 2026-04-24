def even_odd(n):
    if n % 2 == 0:
        result = "Even"
    else:
        result = "Odd"
    return result

print( 5, "is", even_odd(5) )
print( 52, "is", even_odd(52) )

def oneToFive():
    for counter in range(1, 6):
        print( counter )
# end of oneTo5 function

def largest(n, m):
    if n > m:
        return n
    else:
        return m
# end of largest function

oneToFive()
print(largest(5,67))
print(largest(57,7))
print(largest(5, 5))