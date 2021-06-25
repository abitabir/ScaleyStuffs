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

letter_input = str(input("Enter the letter so that all the words beginning with said letter in the string text are returned."))

def get_words_starting_with(text, letter):
    letter = letter.lower()
    text_list = text.split()
    altered_text = text.lower()
    altered_text = altered_text.split()
    for word in range(len(altered_text)):
        letters = list(altered_text[word])
        if letter == letters[0]:
            print(text_list[word])

print("Here you go!")

get_words_starting_with(sample_text, letter_input)

print("~ The End ~")
