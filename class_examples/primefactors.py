a = int(input('Enter a number to factorise: '))
for i in range(2, a+1):
    if a % i == 0:
        prime = True
        for j in range(2, i):
            if i % j == 0:
                prime = False
                break;
        if prime == True:
            print(i)
