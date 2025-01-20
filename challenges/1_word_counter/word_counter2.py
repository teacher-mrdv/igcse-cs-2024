# guess = input('Enter word/phrase: ')
sentence = 'hello dear Grade 9 world'    # we use this for quick testing
sentence = sentence.strip() # remove spaces at before and after the sentence
sentence_length = len(sentence)
spaces_counter = 1
for i in range(sentence_length):
    if sentence[i] == " ":	# slicing the sentence 1 character at a time and checking for a space
        spaces_counter += 1 # abbreviation of spaces_counter = spaces_counter + 1

print(sentence)
print("Number of words = " + str(spaces_counter))


