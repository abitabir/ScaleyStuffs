sample_text = (" As Python s creator, I'd like to say a few words about its "+
              "origins adding a bit of personal philosophy. "+
              "Over six years ago in December I was looking for a "+
              "hobby programming project that would keep me occupied "+
              "during the week around Christmas. My office, "+
              "a government run research lab in Amsterdam would be closed "+
              "but I had a home computer and not much else on my hands "+
              " I decided to write an interpreter for the new scripting "+
              "language  I had been thinking about lately a descendant of ABC "+
              "that would appeal to UnixC hackers I chose Python as a "+
              "working title for   the project being in a slightly irreverent "+
              "mood and a big fan of Monty Python s Flying Circus.  ")

######################### EXERCISE 1 ##########################################

def split_text(text):
    result = []
    wordUnderConstruction = ''

    for char in text:
        
        if char.isalpha(): # continue to build the word
            wordUnderConstruction = wordUnderConstruction + char
            
        else: #probably end of a word as not an alpabet charater
            if wordUnderConstruction != '': #we are at the end of a word
                result.append(wordUnderConstruction)
                wordUnderConstruction = ''  # reinitialise to empty string
                                            # to start new word
            else:       # Thees two lines of code could be ommited. given for
                        # clarification and pedagogical purpose.
                pass    # do nothing, probably met several non alphabet characters
                        # in row



    if wordUnderConstruction != '': # be careful of not ommitting the last word in
                                    # case the text does not finish with a punctuation
        result.append(wordUnderConstruction)

    return result

######################### EXERCISE 2 ##########################################

def split_text_by(text, separator=' '):
    result = []
    wordUnderConstruction = ''

    for char in text:        
        if char in separator:
            if wordUnderConstruction != '': 
                result.append(wordUnderConstruction)
                wordUnderConstruction = ''              
        else: 
            wordUnderConstruction = wordUnderConstruction + char

    if wordUnderConstruction != '': # be careful of not ommitting the last word in
                                    # case the text does not finish with a punctuation
        result.append(wordUnderConstruction)

    return result

print(split_text_by(sample_text,',.'))

######################### EXERCISE 3 ##########################################

def get_words_frequencies(text):
    """
    Below I show the type of data structure I picked to solve the problem.
    A list is preferred to tuple as we need to change the frequencies value
    often and tuples are immutable.
    Soon, we will discover a new built-in data structure 'dict' (for
    dictionary) that is more suitable for this particular problem.
    """
    
    output = [] # a list of lists [[word1, freq1], [word2, freq2], ...]
    
    list_words = splitText(text.lower())
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

######################### EXERCISE 4 ##########################################

def flatten(lst):
    output = []
    for elements in lst:
        output += elements
        
    return output

print(flatten([[],[1,2],[3,4,5,6],[],[],[7],[8,9],[]]))
print(flatten([[3,4,5,6]]))

######################### EXERCISE 5 ##########################################

def rasterise(data, width):
    if len(data) % width: # In Python, and many other languages, 0 is seen as
                          # False whilst other number are considered as True        
        return None
    else:
        output = []
        for i in range(0, len(data), width):
            output.append(data[i:i+width])
            
        return output

print(rasterise([1,2,3,4,5,6,7,8],4))
print(rasterise([1,2,3,4,5,6,7],4))

######################### EXERCISE 6 ##########################################

def sum_column(table):
    if len(table) > 0:
        columns = len(table[0])
        output = columns * [0]
        for row in table:
            if len(row) != columns:
                return None
            for index in range(len(row)):
                output[index] += row[index]

        return output
    return None

print(sum_column([[1,2,3],[4,5,6],[7,8,9]]))
                
            
