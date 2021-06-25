"""
2 (15 marks) Basic Programming Structure
The code must be written in the provided file question_2.py.
The repetition code is one of the most basic error-correcting codes. The code repeats every data
bit multiple times in order to ensure that it was sent correctly. For instance, if the data bit to be
sent is a 1, an n = 3 repetition code will send 111. If the three bits received are not identical, an
error occurred during transmission. If the channel is clean enough, most of the time only one bit
will change in each triple. Therefore, 001, 010, and 100 each correspond to a 0 bit, while 110,
101, and 011 correspond to a 1 bit, with the greater quantity of digits that are the same (’0’ or a
’1’) indicating what the data bit should be.
Implement a function detect_correct(word) with the following requirements:
• The parameter word is a 3-repetition code word (a string of 0s and 1s).
• The function returns a tuple containing the decoded word as first element and the number
of errors in the word as second element. The decoded word is a string of 0s and 1s. For
example. given the input 000111001, the function should return (’010’,1) as the
last three bits contains two 0s and one 1. This means that at least one error has occurred
and the last three bits must therefore be decoded and corrected to a 0.
• The function must raise a ValueError if the length of the word is not a multiple of 3, or
if the string contains characters other than 1 and 0.
• The function must raise a TypeError if the parameter word is not a string.
Finally, write the docstring for this function (5 marks). Note, the docstring must follow one of the
following guidelines; PEP 0257, NumPy, or Google documentation style.
"""

def detect_correct(word):
    """Returns a tuple containing the decoded binary string and number of errors
        detected and corrected from the parameter word.
Parameter: word. Must be of length multiple of three, contain only 1s and 0s,
        and can only be of type string otherwise ValueError, ValueError,
        TypeError are raised respectively.
"""
    if len(word) % 3 != 0:
        raise ValueError("Parameter can only be of length multiple of three.")
    if set(word) != {'0', '1'}:
        raise ValueError("Parameter can only contain 1s or 0s.")
    if type(word) != str:
        raise TypeError("Parameter can only be string type.")
    decoded = ""
    errors = 0
    index = 0
    while index < len(word):
        if word[index] == word[index + 1] == word[index + 2]:
            decoded += word[index]
        else:
            errors += 1
            decoded += str(round(int(word[index]) + int(word[index + 1])
                                 + int(word[index + 2])/2))
        index += 3
    return (decoded, errors)

#corrections: Decodes and corrects 3-repetition coded binary message. Paramater/Args. OH forgot errors


print(detect_correct("000111001"))