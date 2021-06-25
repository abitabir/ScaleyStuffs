number_of_rows = int(input("Input the number of rows you want the symmetrical isosceles made out of increasing (alphabetically) letters to have. Note: number of rows must be less than 26, as there are only 26 letters in the English alphabet, duh."))
numbers_in_rows = 0
count = 1
alphabet = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M", "N", "O", "P", "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
import math

for i in range(number_of_rows):
    row = " " * (2*(number_of_rows-i-1))
    for j in range(int(math.ceil((2*i)+1)/2)):
        row += alphabet[j]
        row += " "
    for k in range(1, int(math.floor((2*i)+1)/2)):
        row += alphabet[int(math.ceil((2*i)+1)/2)-k-1]
        row += " "
    print(row)
