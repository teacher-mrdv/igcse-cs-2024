n :int = 1
s :int = 0
while n > 0:
    n = int(input("enter a positive number: "))
    if n > 0:
        s = s + n
print(s)

'''
DECLARE N, S : INTEGER
N <- 1
S <- 0
WHILE N > 0:
    OUTPUT "Enter a positive number: "
    INPUT N
    IF N > 0
      THEN
        S = S + N
    ENDIF
OUTPUT S
'''