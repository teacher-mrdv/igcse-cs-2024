#
# Check digit validation: ISBN-13
# suggested Python answer
#

def is_valid_isbn13(isbn :str) -> bool:
    # length and type checks
    if find_character(isbn, '-') != -1:
        isbn = replace_character(isbn, '-', '')  # remove dashes
    if len(isbn) != 13 or not isbn.isnumeric():
        return False

    check_digit :int = int(isbn[12]) # or isbn[len(isbn)-1] or [-1]
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
    check_sum :int = 10 - (suma % 10)
    if check_sum == 10:
        check_sum = 0

    # Check if the checksum matches the 13th digit
    return check_sum == check_digit


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

isbn13 :str = input('Enter ISBN: ')
while not is_valid_isbn13(isbn13):
    isbn13 = input('Error. Invalid ISBN-13. Re-enter ISBN: ')
print(f'Valid ISBN-13 input: {isbn13}')