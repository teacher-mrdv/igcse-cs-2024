#
# Check digit validation: ISBN-13
# suggested Python answer
#

def validate_isbn13(isbn :str) -> bool:
    # Initialize the sum
    suma :int = 0

    # Iterate through the first 12 digits
    for i in range(12):
        digit :int = int(isbn[i])
        if (i + 1) % 2 == 0:
            # Multiply even-indexed digits by 3
            suma += (digit * 3)
        else:
            # Add odd-indexed digits directly
            suma += digit

    # Calculate the checksum
    checkSum :int = 10 - (suma % 10)
    if checkSum == 10:
        checkSum = 0

    # Check if the checksum matches the 13th digit
    return checkSum == int(isbn[12])


def find_character(input_string :str, character :str) -> int:
    for i in range(len(input_string)):
        if input_string[i] == character[0]:
            return i
    return -1  # Character not found


def replace_character(original_string, original_char, new_char) -> str:
    new_string = ''
    for i in range(len(original_string)):
        if original_string[i] == original_char:
            new_string += new_char
        else:
            new_string += original_string[i]
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

number = int(isbn13[:-1])     # or isbn13[:len(isbn)-1] or [:12]
check_digit = int(isbn13[-1]) # or isbn13[len(isbn)-1:] or [12]

if validate_isbn13(isbn13):
    print(f'{original_isbn} is a valid ISBN-13!')
else:
    print(f'{original_isbn} is an INVALID ISBN-13')