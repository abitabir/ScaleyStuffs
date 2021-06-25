#########################EXERCISE 1#############################################

##def sum_digits(number):
##    digits = str(number)
##    total = 0
##    for val in digits:
##        total += int(val)
##
##    return total
##
##
##print(sum_digits(1234))




#########################EXERCISE 2#############################################

def pairwise_digits(number_a, number_b):
    # swap number if number_a has more digits than number_b. This is to
    # ensure number_a has always the smallest number of digits.
    if len(number_a) > len(number_b):
        number_a,number_b = number_b, number_a

    # Set the ouput to empty string. output is called an ACCUMULATOR
    output = ''

    # check for all digits in number_a have a corresponding digit in number_b
    # add a 0 or 1 depending on the comparison, add it to the output
    for index in range(len(number_a)):
        if number_a[index] == number_b[index]:
            output += '1'
        else:
            output += '0'
    # remember to pad the end of the output with 0s if number_b has more digits
    # than number_b
    output += '0'*(len(number_b)-len(number_a))
    return output
    
input_a = input('Enter a number: ')
input_b = input('Enter another number: ')


print(pairwise_digits(input_a, input_b))


#########################EXERCISE 3#############################################

#########################    V1: For Loop    ###################################

def to_base10(binary):
    decimal = 0
    for index in range(len(binary)):
        decimal += int(binary[index]) * pow(2,len(binary) - 1 - index)
    return decimal


binary = input('Enter a binary number: ')
print(to_base10(binary))

#########################    V2: While Loop  ###################################
def to_base10b(binary):
    decimal = 0
    index = 0
    power = len(binary) - 1
    while index < len(binary):
        decimal += int(binary[index]) * pow(2,power)
        power -= 1
        index += 1
        
    return decimal

binary = input('Enter a binary number: ')
print(to_base10b(binary))


######################### EXERCISE 4 ##########################################

rows = int(input('Enter number of rows: '))

output = ''
add_1 = True # flag to check if we add a 1 (True) or a 0 (False)

for row in range(rows + 1):
    # If a row is even, we start with a 1, otherwise with a 0
    if row % 2 == 0:
        add_1 = True
    else:
        add_1 = False
        
    for index in range(row + 1):
        if add_1:
            output += '1'
        else:
            output += '0'
        add_1 = not add_1 # change flag from True to False and vice versa

    output += '\n' # once we finished to add row+1 characters go to newline

print(output)

######################### EXERCISE 7 ##########################################

# I need a reprsentation of the alphabet.
# I decided on a string but list is fine as well.
alphabet = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

output = ''
for row in range(rows):
    # I need to calculate how many blank spaces need to be added in front
    # of each row. This varies from row to row.
    output += (rows - row - 1) * '  ' # padding the front of row with space

    # Adds the letter in ascending alphabet order using index to find the
    # character in the alphabet
    for index in range(row + 1):
        output += alphabet[index] + ' ' # going up the alphabet

    
    # Adds the letter in descending alphabet order using index to find the
    # character in the alphabet. Must be careful not to add the middle
    # character twice.
    #
    # Note: range(4,0,-1) returns values from 4 to 0 (excluded), that is
    # 4 then 3, 2, 1. You should read the documentation for range.
    for index in range(row, 0, -1):
        output += alphabet[index - 1] + ' ' # going down the alphabet

    output += '\n'

print('--------------------------------------------')
print(output)
