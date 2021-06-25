number_of_rows = int(input("Input the number of rows you want the right angle triangle made out of alternating 1s and 0s to have."))
numbers_in_rows = 0

for i in range(number_of_rows):
    row = ""
    if i % 2 == 1:
        for j in range(i):
            if j % 2 == 0:
                row = row + "1"
            else:
                row = row + "0"
    
    if i % 2 == 0:
        for j in range(i):
            if j % 2 == 1:
                row = row + "1"
            else:
                row = row + "0"

    print(row)
