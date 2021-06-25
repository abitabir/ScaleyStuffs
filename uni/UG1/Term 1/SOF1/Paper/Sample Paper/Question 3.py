"""
3 (15 marks) Built-in data structures: Dictionary
The code for this question must be written in the provided file question_3.py.
A two-out-of-five code is an encoding scheme which uses five bits consisting of exactly three 0s
and two 1s to represent a decimal digit. This provides ten possible combinations, enough to
represent the digits 0–9. This scheme can detect all single bit-errors, all odd numbered bit-errors
and some even numbered bit-errors (for example the flipping of both 1-bits). The weights
assigned to the bit positions are 7-4-2-1-0. For example, 2 is encoded as 00101 and 9 as 10100.
However, in this scheme, zero is encoded specially, using the 7+4 combination (binary 11000)
that would naturally encode 11.
Implement a function two_out_five(message) where:
• message is a string of 0s and 1s representing a number. For example the string
"000111100000110" represents the number 103.
• the returned value should be a string representing the number in decimal. For example,
given the string "000111100000110" as parameter, the return value is the string "103".
• if message is not a string, the function must raise a TypeError.
• if the message contains any characters that are not 1s or 0s, or has been corrupted, for
example has missing digits (like "0011"), or has one or more bits flipped (that is a 1
becomes a 0 during transmission
"""

# my pretty eh version
def two_out_of_five(message):
    if not isinstance(message, str):
        raise TypeError("Parameter must be of type string.")
    if set(message) != {'1', '0'}:
        raise ValueError("Parameter must be a binary string.")
    if len(message) % 5 != 0:
        raise ValueError("Parameter has lost data.")
    index = 0
    decoded_message = ""
    while index < len(message):
        submessage = message[index:index + 5]
        if submessage.count('1') != 2:# or message.count('0') != 3: #kinda redundant
            raise ValueError("Parameter has corrupted data.")
        first_index_of_one = submessage.find('1')
        print(submessage)
        second_index_of_one = submessage.replace('1', '0', 1).find('1') #deleting first 1 so can find index of second
        print(second_index_of_one)
        index_set = {first_index_of_one, second_index_of_one}
        if index_set == {1, 0}: #special case
            decoded_message += '0'
        else:
            decoded_submessage = 0
            if 0 in index_set:
                decoded_submessage += 7
            if 1 in index_set:
                decoded_submessage += 4
            if 2 in index_set:
                decoded_submessage += 2
            if 3 in index_set:
                decoded_submessage += 1
                print(index_set)#
#            if 4 in index_set: #quite redundant
#                decoded_submessage += 0
            decoded_message += str(decoded_submessage)
        index += 5
    return decoded_message

print(two_out_five("00011001010011001001010100110010001100101010011000"))

# Lilly's pretty snazzy version
def two_out_five(message):
    encoding = [7, 4, 2, 1, 0]
    result = ''
    if not isinstance(message, str):
        raise TypeError()

    if len(message) % 5 != 0:
        raise ValueError()

    if message.count('1') + message.count('0') != len(message):
        raise TypeError('Invalid character(s) in the message!')

    for index in range(0, len(message), 5):
        word = message[index:index + 5]
        if word == '11000':
            result += '0'
        elif word.count('1') != 2:
            raise ValueError('Invalid number of 1s in a word!')
        else:
            number = 0
            for pos in range(len(word)):
                number += int(word[pos]) * encoding[pos]

            result += str(number)

    return result