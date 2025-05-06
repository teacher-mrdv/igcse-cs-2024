# Counts the number of digits of an integer by using floor division by 10
def digits(number: int) -> int:
    counter: int = 0
    while number > 0:
        number = number // 10
        counter = counter + 1
    return counter

# True is the number is a palindrom, False otherwise
def isPalindrome(number: int) -> bool:
    # counter used to calculate the power of 10 that the number has to be divided by to get the first (leftmost) digit
    counter: int = digits(number) - 1
    # copy of the number used to extract the first/left half of the digits
    number1: int = number
    # copy of the number used to extract the second/right half of the digits
    number2: int = number
    # comparisons to do between left and right digits
    to_do: int = digits(number) // 2
    palindrome: bool = True         #  assume it is a palindrome
    while to_do > 0:
        tens:  int = 10 ** counter  #  power of 10 needed to extract the leftmost digit
        left:  int = number1 // tens # extracts the leftmost digit from the number
        right: int = number2 % 10   #  extracts the last digit from the number
        counter = counter - 1       # we are done with the first pair of digits (left & rightmost)
        number1 = number1 - (left * tens)   # remove the leftmost digit by subtraction
        number2 = number2 // 10     # remove the last (rightmost) digit (dividing the number by 10)
        to_do = to_do - 1           # 1 less pair of digits to check
        if left != right:           # if any pair of digits are different, the number is not a palindrome
            return False
    return True

# let's do some testing!
print('isPalindrome(123454321) = ', isPalindrome(123454321))
print('isPalindrome(2101012)   = ', isPalindrome(2101012))
print('isPalindrome(1221)  = ', isPalindrome(1221))
print('isPalindrome(12345) = ', isPalindrome(12345))
print('isPalindrome(1234) = ', isPalindrome(1234))
print('isPalindrome(1234) = ', isPalindrome(1234))
print('isPalindrome(2002) = ', isPalindrome(2002))
