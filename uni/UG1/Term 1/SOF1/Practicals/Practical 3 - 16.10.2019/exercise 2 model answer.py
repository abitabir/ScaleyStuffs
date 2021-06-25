#########################EXERCISE 2#############################################

#######################    part 1    ###########################################
sentence = input('Enter a sentence: ')
numbers = sentence.split()
count_even = 0
for a_number in numbers:
    a_number = int(a_number)
    if a_number % 2 == 0:
        count_even = count_even + 1 # you could also write count_even += 1

print('There are',count_even,'even numbers.')

#########################    part 2    ###########################################
sentence = input('Enter a sentence: ')
numbers = sentence.split()
count_even = 0
even_numbers = []

for a_number in numbers:
    a_number = int(a_number)
    if a_number % 2 == 0:
        count_even = count_even + 1 # you could also write count_even += 1
        even_numbers.append(a_number)

print('There are',count_even,'even numbers:', even_numbers)



#######################    part 3    ###########################################
sentence = input('Enter a sentence: ')
numbers = sentence.split()
count_even = 0
even_numbers = []

for a_number in numbers:
    a_number = int(a_number)
    if (a_number % 2 == 0
        and a_number not in even_numbers):
        # The number is not already in the list so we add it
        count_even += 1 
        even_numbers.append(a_number)

print('There are',count_even,'distinct even numbers:', even_numbers)





