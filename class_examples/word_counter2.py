# guess = input('Enter word/phrase: ')
sentence = 'hello dear Grade 9 world'    # we use this for quick testing
sentence_length = len(sentence)
spaces_counter = 1
for i in range(sentence_length):
    if sentence[i] == " ":
        spaces_counter += 1

print(sentence)
print("Number of words = " + str(spaces_counter))


