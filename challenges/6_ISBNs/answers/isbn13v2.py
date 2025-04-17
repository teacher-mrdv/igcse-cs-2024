#
# Check digit validation: ISBN-13
# suggested Python answer, version 2
#

def is_valid_isbn13(isbn: str) -> bool:
	# remove dashes, if any found
	if find_character(isbn, '-') != -1:
		isbn = replace_character(isbn, '-', '')

	# length and type checks
	if len(isbn) != 13 or not isbn.isnumeric():
		return False

	# Initialize variables
	suma: int = 0
	weight: int = 1
	
	# Iterate through the first 12 digits
	for i in range(12):
		digit: int = int(isbn[i])
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
	return checkDigit == lastDigit


def find_character(input_string :str, character :str) -> int:
	for i in range(len(input_string)):
		if input_string[i] == character[0]:
			return i
	return -1  # Character not found


def replace_character(original_string: str, original_char: str, new_char: str) -> str:
	new_string = ''
	for i in range(len(original_string)):
		if original_string[i] == original_char[0]:
			new_string += new_char
		else:
			new_string += original_string[i]
	return new_string


# Main

isbn13 :str = input('Enter ISBN: ')
while not is_valid_isbn13(isbn13):
	isbn13 = input('Error. Invalid ISBN-13. Re-enter ISBN: ')
print(f'Valid ISBN-13 input: {isbn13}')