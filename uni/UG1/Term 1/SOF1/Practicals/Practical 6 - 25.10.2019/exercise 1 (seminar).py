def is_palindrome(word):
    word_list = list(word.lower())
    for character in word_list:
        if character == "," or " " or "'" or "!":
            del character
    reverse_word_list = word_list.copy()
    reverse_word_list.reverse()
    for i in range(len(word_list)):
        if word_list[i] != reverse_word_list[i]:
            return("False")
        else:
            return("Treu")

purported_palindrome = str(input("This program checks if the string you enter is a palindrome, excepting blank spaces and commas and apostrophes and exclaimation marks. Enter the purported palindrome string to check if it is indeed a palindrome."))

print("The supposition that the string you entered was a palindrome is infact", is_palindrome(purported_palindrome), ".")
