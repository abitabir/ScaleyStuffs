number_of_rows = int(input("Input the number of rows you want the right angle triangle made out of increasing integers to have."))
numbers_in_rows = 0
count = 1

for i in range(number_of_rows):
    row = ""
    for j in range(i):
        if count < 9:
                row = row + "  " + str(count + 1)
                count += 1
        else:
                row = row + " " + str(count + 1)
                count += 1

    print(row)
