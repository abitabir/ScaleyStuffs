#########################EXERCISE 1#############################################

#######################    part 1    ###########################################
sentence = input('Enter a sentence: ')
output = ''
for letter in sentence:
    if letter != ' ':
        output += letter

print(output)




#######################    part 2    ###########################################
sentence = input('Enter a sentence: ')
output = ''

# We need to set up a FLAG that tells us if the next character is the first
# Character of the next word. We can use a boolean variable, let's call it
# first_letter. We need to assign the value True as the next character will
# be the first of the sentence and therefore the first of a word.
first_letter = True

for letter in sentence:
    if letter != ' ':
        if first_letter:
            # The character is the first of a word so must be
            # upper case
            output += letter.upper()
            first_letter = False
        else:
            output += letter.lower()
    else: #means that the next character will be the first one of a new word
        first_letter = True

print(output)




#######################    part 3    ###########################################
sentence = input('Enter a sentence: ')
output = ''

# We need to set up a FLAG that tells us if the next character is the first
# Character of the next word. We can use a boolean variable, let's call it
# first_letter. We need to assign the value True as the next character will
# be the first of the sentence and therefore the first of a word.
first_letter = True

# We also need an ACCUMULATOR to store the content of the current word we
# are buiding. We initialise the accumulator to an empty string ''.
current_word = ''

# Finally we need another ACCUMULATOR to build the list of word. It is
# initialised to an empty list [].
output = []

for letter in sentence:
    if letter.isupper():
        output.append(current_word)
        current_word = letter # we just started a new word
    else: #means that the next character will be the first one of a new word
        current_word += letter

# We must be careful, when we finished to go through the sentence, we did not
# add the last word.
output.append(current_word)
print(output)



