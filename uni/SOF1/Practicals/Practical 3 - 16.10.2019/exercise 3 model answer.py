#########################EXERCISE 3#############################################

#######################    part 4    ###########################################
# Dealing with the inputs
table = []
sudoku_size = 4
for times in range(sudoku_size):
    data = input('Enter 4 digits (0..4) separated by a space: ')
    digits = data.split()
    for index in range(sudoku_size):
        digits[index] = int(digits[index])
    table.append(digits)

# Dealing with the output
hline = '+-+-+-+-+\n'
output = hline
for row in table:
    for element in row:
        if element == 0:
            output += '| ' # Use blank space rather than 0
        else:
            output += '|'+str(element)
    output += '|\n' # must add the last vertical line of table and go to newline
    output += hline

print(output)






