#text = str(input("This program splits a text into elements of a list at every place where there is a character that is not a letter or number. Enter a string for it to be split so."))

sample_text = "As Python's creator, I'd like to say a few words about its origins."

def split_text(text):
    output = []
    element = ""
    for character in text:
        if character.isalnum():
            element += character
        else:
            if element != "":
                output.append(element)
                element = ""
    return(output)

print(split_text(sample_text))
