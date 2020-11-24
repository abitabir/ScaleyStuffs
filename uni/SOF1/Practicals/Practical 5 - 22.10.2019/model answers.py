############################ Exercise 1 #######################################
grain_weight = 30 #in mg
current_square = 1 #first square initialised
total_grain = 1
for index in range(2,65) : #counting from second square and 65 not included
    current_square *= 2
    total_grain += current_square

    # a nice presentation
    if(current_square * 30 < 1e3):
        print ('the weight on square', index, 'is',
               str(int(current_square * 30)),'mg.')
    elif(current_square * 30 < 1e6):
        print ('the weight on square', index, 'is',
               str(int(current_square * 30 / 1e3)),'g.')
    elif(current_square * 30 < 1e9):
        print ('the weight on square', index, 'is',
               str(int(current_square * 30 / 1e6)),'kg.')
    elif(current_square * 30 < 1e15):
        print ('the weight on square', index, 'is',
               str(int(current_square * 30 / 1e9)),'tons.')
    elif(current_square * 30 < 1e18):
        print ('the weight on square', index, 'is',
               str(int(current_square * 30 / 1e15)),'million tons.')
    elif(current_square * 30 < 1e21):
        print ('the weight on square', index, 'is',
               str(int(current_square * 30 / 1e18)),'billion tons.')
    else:
        print ('the weight on square', index, 'is',
               str(int(current_square * 30 / 1e21)),'trillion tons.')
        

total_weight = total_grain *30 #in mg

if(total_weight < 1e3):
    print ('the total weight is:', str(total_weight),'mg.')
elif(total_weight < 1e6):
    print ('the total weight is:', str(total_weight/1e3),'g.')
elif(total_weight < 1e9):
    print ('the total weight is:', str(total_weight/1e6),'kg.')
elif(total_weight < 1e15):
    print ('the total weight is:', str(total_weight/1e9),'tons.')
elif(total_weight < 1e18):
    print ('the total weight is:', str(total_weight/1e15),'million tons.')
elif(total_weight < 1e21):
    print ('the total weight is:', str(int(total_weight/1e18)),'billion tons.')
else:
    print ('the total weight is:', str(total_weight/1e21),'trillion tons.')

print ('Which is equivalent to', int(total_weight / 678e15),
       'years of the world wide production.')



############################ Exercise 4 #######################################


sample_text = (" As Python s creator I d like to say a few words about its "+
              "origins adding a bit of personal philosophy "+
              "Over six years ago in December I was looking for a "+
              "hobby programming project that would keep me occupied "+
              "during the week around Christmas My office "+
              "a government run research lab in Amsterdam would be closed "+
              "but I had a home computer and not much else on my hands "+
              " I decided to write an interpreter for the new scripting "+
              "language  I had been thinking about lately a descendant of ABC "+
              "that would appeal to UnixC hackers I chose Python as a "+
              "working title for   the project being in a slightly irreverent "+
              "mood and a big fan of Monty Python s Flying Circus")

def get_words_starting_with(text, letter):
    list_words = text.split()
    output = []
    for word in list_words:
        if (word.lower().startswith(letter.lower())
            and word not in output):
            output.append(word)

    return output

def get_words_frequencies(text):
    # Below I show the type of data structure I picked to solve the problem.
    # A list is preferred to tuple as we need to change the frequencies value
    # often and tuples are immutable.
    # Soon, we will discover a new built-in data structure 'dict' (for
    # dictionary) that is more suitable for this particular problem,
    
    output = [] # a list of lists [[word1, freq1], [word2, freq2], ...]
    
    list_words = text.lower().split()
    for word in list_words:
        word_in_list = False

        # Check if the word has been already encountered in the text and
        # has therefore a frequency greater or equal to 1.
        for index in range(len(output)):
            if output[index][0] == word: # the word exists in the list,
            # so must add 1 to its with frequency
                output[index][1] += 1
                word_in_list = True
                           
        if not word_in_list: # the word does not exist in the list,
            # so must add it with frequency 1
            output.append([word, 1])

    return output

    

print(get_words_starting_with(sample_text, 'a')) 
print(get_words_frequencies(sample_text)) 


############################ Exercise 5 #######################################

# Here I have made the design decision to add the alphabet as a parameter.
# This makes my function more flexible and easy to reuse. I will be able to
# use the function with the English alphabet, the French one or any symbols
# I may want to use.
def caesar_encrypt(alphabet, shift, plaintext):
    cypher_text = ""
    for letter in plaintext:
        if letter in alphabet:
            index = alphabet.index(letter)
            substitution_index = (index + shift) % len(alphabet)
            cypher_text = cypher_text + alphabet[substitution_index]
        else:
            cypher_text = cypher_text + letter

    return cypher_text

# As we use an alphabet  to encrypt, you must also pass that alphabet when
# we are decrypting the cypher.
def caesar_decrypt(alphabet, shift, cypher_text):
    plaintext = ""
    for letter in cypher_text:
        if letter in alphabet:
            index = alphabet.index(letter)
            substitution_index = (index - shift) % len(alphabet)
            plaintext = plaintext + alphabet[substitution_index]
        else:
            plaintext = plaintext + letter

    return plaintext


# The brute force approach here is to try all possible shift given an alphabet
# and look at which output make sense. A cleverer approach would be to use
# character frequency analysis.
def hacks_caesar(alphabet, cypher_text):
    # this is a "brute force" algorithm
    for shift in range(len(alphabet)):
        print ("key:", shift, "->", caesar_decrypt(alphabet, shift, cypher_text))


#################### Test for Exercise 5 ####################
alphabet = "abcdefghijklmnopqrstuvwxyz"

plain = "the good news about computers is that they do what "\
        "you tell them to do. the bad news is that they do what "\
        "you tell them to do."

key = 5

cypher = caesar_encrypt(alphabet, key, plain)

print (cypher)
print (plain)
print (caesar_decrypt(alphabet, key, cypher))

hacks_caesar(alphabet, cypher)


############################ Exercise 6 #######################################


vector = eval(input("Enter a vector [x, y, ..]: "))
scalar = float(input("Enter a scalar: "))

def scalar_product(scalar, vector):
    prod = []    
    for number in vector:
        prod = prod + [number * scalar]

    return prod

def vector_addition(vector1, vector2):
    if(len(vector1) == len(vector2)):
        sum_vector = []
        index = 0
        while index < len(vector1):
            sum_vector = sum_vector + [vector1[index] + vector2[index]]
            index +=1

        return sum_vector
    else:
        print ("cannot add vectors with different dimensions.")
        return None


#################### Test for Exercise 5 ####################
        
vector1 = eval(input("Enter a vector [x, y, ..]: "))
scalar = float(input("Enter a scalar: "))
print("scalar product is:", scalar_product(scalar, vector1))
vector2 = eval(input("Enter a vector [x, y, ..]: "))

   
