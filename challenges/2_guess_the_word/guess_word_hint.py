@@ -1,25 +0,0 @@
##
# this code is a hint to help you with the challenge of coding a simple game
# to guess a word in 5 tries, similar to the basics of hangman
# you will NEED to code your solution using methods/functions 'def'
# you may want to refer to the Python online documentation (Thonny uses Python 3.10),
# Think Python: How to Think Like a Computer Scientist 2nd edition and Python in a Nutshell
# AIs like chatGPT are not recommended as this is a problem exercise for your brain.
##

# secret = input('Enter secret word/phrase: ')
secret = 'parallel'		# we use this for quick testing
secret_length = len(secret)
mask  = ''				# the secret word, hidden
letter = input('Enter a letter: ')
letter = letter[0]		# whatever the input, just take the 1st character
counter = 0

while counter < secret_length:
    if secret[counter] == letter:
        mask += letter
    else:
        mask += '-'
    counter = counter + 1

print(mask)
