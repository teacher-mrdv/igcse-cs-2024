# Python 3 program to round-off a number  
# to given no. of significant digits
# This code is contributed by 
# Surendra_Gangwar
# minor modifications MRDV

from math import ceil, floor, pow

# Function to round - off the number
def round_off(x:float, sfs:int) -> float: 
    b = x 
    c = floor(x) 

    # Counting the no. of digits  
    # to the left of decimal point  
    # in the given no.
    i = 0; 
    while(b >= 1): 
        b = b / 10
        i = i + 1

    d = sfs - i 
    b = x
    b = b * pow(10, d) 
    e = b + 0.5
    if (float(e) == float(ceil(b))): 
        f = (ceil(b)) 
        h = f - 2
        if (h % 2 != 0): 
            e = e - 1
    j = floor(e) 
    m = pow(10, d) 
    j = j / m 
    return j 

# Driver Code
# Number to be rounded - off 
x = 139.59987

# No. of Significant digits  
# required in the no. 
sfs = 4

print( round_off(x, sfs) )
print( round_off(24.077, 3) )

