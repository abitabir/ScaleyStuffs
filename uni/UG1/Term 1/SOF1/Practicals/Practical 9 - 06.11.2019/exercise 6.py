#0
f = open('numberss.txt', 'w+')
f.write('1 30 4 5\n8 12 19 1\n5 5 10')
f.close()

#1.
#I dunnooooo

#2.
#with open(filename, 'r') as in_file:
def sum_numbers_per_line(fileline):
    numbers = fileline.split()
    total = 0
    for number in numbers:
        total += int(number)
    return(total)

#3.

def sum_from_file(filename):
    """Returns sum of all numbers in a file.""" #4.
    f = open(filename, 'r')
    filelines_list = f.readlines()
    total = 0
    for fileline in filelines_list:
        total += sum_numbers_per_line(fileline)
    f.close()
    return(total)

print(sum_from_file('numberss.txt'))