#1.
input_sentence = str(input("Enter the sentence from which you want to remove all whitespace."))
output_sentence = ""

for i in range(len(input_sentence)):
    if input_sentence[i] != " ":
        output_sentence = output_sentence + input_sentence[i]

print(output_sentence)

### just realised, could have used input_list = input_sentence.split()

#2.

input_sentence = str(input("Enter the sentence which you want to be returned in CamelCase."))
output_sentence = ""

for i in range(len(input_sentence)):
    if i == 0:
        output_sentence = output_sentence + (input_sentence[i]).upper()
    elif input_sentence[i] != " ":
        if input_sentence[i-1] == " ":
            output_sentence = output_sentence + (input_sentence[i]).upper()
        else:
            output_sentence = output_sentence + (input_sentence[i]).lower()

print(output_sentence)

#3.

input_sentence = str(input("Enter the sentence in CamelCase which you want returned as a printed list."))
output_list = []
word = ""

for i in range(len(input_sentence)):
    if input_sentence[i].islower():
        word = word + input_sentence[i]
    else:
        output_list.append(word)
        word = input_sentence[i]
# one last time for the last word XO
output_list.append(word)
word = input_sentence[i]
# deleting the first empty string element in the output_list
del output_list[0]
print(output_list)
