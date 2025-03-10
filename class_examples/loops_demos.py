#
# Examples of different loops in pseudocode and Pyhon equivalents
# These algorithms add only positive integers until 0 is input.
# Note that it ignores the negatives.
#
''' Pseudocode
DECLARE N, S : INTEGER
N <- 1
S <- 0
WHILE N <> 0:
    OUTPUT "Enter a positive number (Negatives ignored): "
    INPUT N
    IF N > 0
      THEN
        S = S + N
    ENDIF
OUTPUT S
'''
n :int = -1 # any value for n that will get into the while loop
s :int = 0
while n != 0:
    n = int(input('Enter a positive number (Negatives ignored): '))
    if n > 0:
        s = s + n
print(s)

''' Pseudocode
DECLARE N, S : INTEGER
S <- 0
REPEAT
    OUTPUT "Enter a positive number (Negatives ignored): "
    INPUT N
    IF N > 0
      THEN
        S = S + N
    ENDIF
UNTIL N <= 0
OUTPUT S
'''

s :int = 0
while True:     # equivalent to REPEAT / always run
    n = int(input('Enter a positive number (Negatives ignored):7 '))
    if n > 0:
        s = s + n
    # the lines below should go at the end of the while loop. Mind nested loops!
    if n == 0:  # until this condition is True.
        break   # when it becomes True, exit the while loop.
print(s)


