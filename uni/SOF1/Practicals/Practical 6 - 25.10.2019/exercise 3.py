#text = str(input("Enter the text for which you want the occurances of words returned."))

sample_text = (" As Pythons creato I d like to say a few words about its "+
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
              "mood and a big fan of Monty Pythons Flying Circus")

def createDictionary(text):
    dictionary_text = []
    text_list = text.split()
    for word in text_list:
        if word not in dictionary_text and word.lower() not in dictionary_text:
            dictionary_text.append(word)
    return(dictionary_text)

def getWordsFrequency(text, dictionary_text):
    word_count = []
    for j in range(len(dictionary_text)):
        word_count.append(0)
    for i in range(len(dictionary_text)):
        words = text.split()
        for word in words:
            if word == dictionary_text[i] or words[j].lower() == dictionary_text[i]:
                word_count[i] += 1
    return(word_count)

dico_text = createDictionary(sample_text)
print(dico_text)

word_frequency = getWordsFrequency(sample_text, dico_text)

for i in range(len(dico_text)):
    print("The word '" + dico_text[i] + "' has", word_frequency[i], "occurences.")
