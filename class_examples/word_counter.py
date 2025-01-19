# guess = input('Enter word/phrase: ')
sentence = 'hello dear Grade nine world'    # we use this for quick testing
sentence_length = len(sentence)
spaces_counter = 1
for character in sentence:
    if character == " ":
        spaces_counter += 1

print(sentence)
print("Number of words = " + str(spaces_counter))

