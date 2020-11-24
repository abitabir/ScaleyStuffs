sample_text = (" As Pythons creato I d like to say a few words about its " +
              "origins adding a bit of personal philosophy " +
              "Over six years ago in December I was looking for a " +
              "hobby programming project that would keep me occupied " +
              "during the week around Christmas My office " +
              "a government run research lab in Amsterdam would be closed " +
              "but I had a home computer and not much else on my hands " +
              " I decided to write an interpreter for the new scripting " +
              "language  I had been thinking about lately a descendant of ABC " +
              "that would appeal to UnixC hackers I chose Python as a " +
              "working title for   the project being in a slightly irreverent " +
              "mood and a big fan of Monty Pythons Flying Circus")

letter_input = str(input("Enter the letter so that all the words beginning with said letter in the string text are returned only once, along with their frequency in the text."))

def get_words_starting_with(text, letter):
    output = []
    text_list = text.split()
    for word in text_list:
        if (word.lower().startswith(letter.lower())
            and word not in output):
            output.append(word)
    return(output)

def word_frequency_counting(text, output):
    wordcount = []
    for j in range(len(output)):
        wordcount.append(0)
        for i in range(len(text)):
            if text[i] == output[j]:
                wordcount[j] = 1
    return(wordcount)

print("Here you go!")

dico_text = get_words_starting_with(sample_text, letter_input)
word_frequency = word_frequency_counting(sample_text, dico_text)

for i in range(len(dico_text)):
    print("in the sample text", dico_text[i], "has word frequency", word_frequency[i]+1)

print("~ The End ~")
