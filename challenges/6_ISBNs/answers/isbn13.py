#
# Check digit validation: ISBN-13
# suggested Python answer, version 1
# inspired by our pseudocode answer
#

def validate_isbn13(isbn :str) -> bool:
    # Initialize variables
    suma   :int = 0
    weight :int = 1

    # Iterate through the first 12 digits
    for i in range(12):
        digit :int = int(isbn[i])
        if (i + 1) % 2 == 0:
            # Set the weight of the digit to 3 to multiply even-indexed digits by 3
            weight = 3
        else:
            # Set the weight of the digit to 1 to just add odd-indexed digits
            weight = 1
        suma = suma + (digit * weight)

    # Calculate the checksum (checkDigit)
    checkDigit :int = 0
    remainder  :int = suma % 10
    if remainder == 0:
        checkDigit = 0
    else:
        checkDigit = 10 - remainder
    
    # Get the 13th digit only
    lastDigit :int = int(isbn[12])
    # Check if the checksum (checkDigit) matches the 13th digit input
    if checkDigit == lastDigit:
        return True
    else:
        return False


def find_character(input_string :str, character :str) -> int:
    for i in range(len(input_string)):
        if input_string[i] == character[0]:
            return i
    return -1  # Character not found


def replace_character(original_string, original_char, new_char) -> str:
    new_string = ''
    for i in range(len(original_string)):
        if original_string[i] == original_char:
            new_string = new_string + new_char
        else:
            new_string = new_string + original_string[i]
    return new_string


# Main
isbn13 :str = ''
original_isbn :str = ''
number :int = 0
check_digit :int = 0

while True:
    isbn13 = input('Enter ISBN: ')
    original_isbn = isbn13
    if '-' in isbn13:
        isbn13 = isbn13.replace('-', '')  # remove dashes
    if len(isbn13) == 13 and isbn13.isnumeric():
        break

number = int(isbn13[:12])     # or isbn13[:len(isbn)-1] or [:-1] to get the first 12 digits

if validate_isbn13(isbn13):
    print(f'{original_isbn} is a valid ISBN-13!')
else:
    print(f'{original_isbn} is an INVALID ISBN-13')