def guess(letter, word, mask):
    new_mask = ""
    counter = 0
    while counter < len(word):
        if word[counter] == letter:
            new_mask += letter
        else:
            new_mask += mask[counter]
        counter = counter + 1
    return new_mask

def initialise_mask(word):
    mask = ""
    for char in word:
        mask += "-"
    return mask

word = "parallel"
mask = initialise_mask(word)
tries = 5
while tries > 0:
    print("You have " + str(tries) + " tries.")
    letter = input("Enter a letter: ")
    letter = letter[0]
    mask = guess(letter, word, mask)
    if letter not in word:
        tries -= 1
    print(mask)
    if "-" not in mask:
        print("You won!")
        break
    
if "-" in mask:
    print("You lost.")
    