def digits(number: int) -> int:
    counter: int = 0
    while number > 0:
        number = number // 10
        counter = counter + 1
    return counter

def isPalindrome(number: int) -> bool:
    counter: int = digits(number) - 1
    number1: int = number
    number2: int = number
    to_do: int = digits(number) // 2
    palindrome: bool = True
    while to_do > 0:
        tens:  int = 10 ** counter
        left:  int = number1 // tens
        right: int = number2 % 10
        counter = counter - 1
        number1 = number1 - (left * tens)
        number2 = number2 // 10
        to_do = to_do - 1
        if left != right:
            return False
    return True

print(isPalindrome(123454321))
print(isPalindrome(1221))
print(isPalindrome(12345))
print(isPalindrome(1234))
    
            
    
    
