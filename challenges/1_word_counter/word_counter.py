# guess = input('Enter word/phrase: ')
sentence = 'hello dear Grade nine world'    # we use this for quick testing
sentence_length = len(sentence)
sentence = sentence.strip() # remove spaces at before and after the sentence
spaces_counter = 1
for character in sentence:	# iterating over each character in the sentence/string
    if character == " ":
        spaces_counter = spaces_counter + 1

print(sentence)
print("Number of words = " + str(spaces_counter))

