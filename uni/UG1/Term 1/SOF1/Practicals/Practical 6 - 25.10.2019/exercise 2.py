#text = str(input("This program splits a text into elements of a list at every place where there is a character that is contained in a prespecified function parameter string of punctuations. Enter a string for it to be split as such."))

sample_text = "As Python's creator, I'd like to say a few words about its origins."

def split_text(text, seperators):
    output = []
    element = ""
    for character in text:
        if character in seperators:
            if element != "":
                output.append(element)
                element = ""
        else:
            element += character
    return(output)

print(split_text(sample_text, ",.'"))
