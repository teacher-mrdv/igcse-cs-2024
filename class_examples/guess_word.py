# secret = input('Enter secret word/phrase: ')
secret = 'parallel'    # we use this for quick testing
secret_length = len(secret)
mask  = ''
letter = input('Enter a letter: ')
letter = letter[0]
counter = 0

while counter < secret_length:
    if secret[counter] == letter:
        mask += letter
    else:
        mask += '-'
    counter = counter + 1

print(mask)
