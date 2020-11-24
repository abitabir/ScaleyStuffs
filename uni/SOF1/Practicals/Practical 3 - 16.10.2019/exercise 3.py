#1.

four_digits = str(input("Enter four digits, each seperated by a space."))

four_digits_list = four_digits.split()

for i in range(len(four_digits_list)):
    four_digits_list[i] = int(four_digits_list[i])

print(four_digits_list)

#2.

four_lists_of_four_digits = []

for i in range(4):
    if i == 1:
        four_digits = str(input("Enter four digits, each seperated by a space."))
    else:
        four_digits = str(input("Enter four digits again, each seperated by a space."))
        
    four_digits_list = four_digits.split()

    for i in range(len(four_digits_list)):
        four_digits_list[i] = int(four_digits_list[i])

    four_lists_of_four_digits.append(four_digits_list)

print(four_lists_of_four_digits)

#3.

four_lists_of_four_digits = []

for i in range(4):
    if i == 0:
        four_digits = str(input("Enter four digits, each seperated by a space."))
    else:
        four_digits = str(input("Enter four digits again, each seperated by a space."))
        
    four_digits_list = four_digits.split()

    four_lists_of_four_digits.append(four_digits_list)

sudoku = ""

for i in range(4):
    print("+-+-+-+-+")
    for j in range(4):
        sudoku = sudoku + "|"
        sudoku = sudoku + four_lists_of_four_digits[i][j]
    sudoku = sudoku + "|"
    print(sudoku)
    sudoku = ""
print("+-+-+-+-+")

#4.

four_lists_of_four_digits = []

for i in range(4):
    if i == 0:
        four_digits = str(input("Enter four digits, each seperated by a space."))
    else:
        four_digits = str(input("Enter four digits again, each seperated by a space."))
        
    four_digits_list = four_digits.split()

    four_lists_of_four_digits.append(four_digits_list)

sudoku = ""

for i in range(4):
    print("+-+-+-+-+")
    for j in range(4):
        if four_lists_of_four_digits[i][j] == "0":
            four_lists_of_four_digits[i][j] = " "
        sudoku = sudoku + "|"
        sudoku = sudoku + four_lists_of_four_digits[i][j]
    sudoku = sudoku + "|"
    print(sudoku)
    sudoku = ""
print("+-+-+-+-+")

#5.
