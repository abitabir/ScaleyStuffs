#1.

numbers_string = str(input("Enter the series of positive numbers with spaces that you want the number of even numbers in printed."))

numbers_list = numbers_string.split()
even_number_count = 0

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
    if numbers_list[i] % 2 == 0:
         even_number_count += 1

print("There are", even_number_count, "even numbers in the series of positive numbers you inputted.")

#2.

numbers_string = str(input("Enter the series of positive numbers with spaces that you want the number of even numbers in printed."))

numbers_list = numbers_string.split()
even_numbers_count = 0
even_numbers = []

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
    if numbers_list[i] % 2 == 0:
         even_numbers_count += 1
         even_numbers.append(numbers_list[i])

print("There are", even_numbers_count, "distinct even numbers in the series of positive numbers you inputted:")

for j in range(len(even_numbers)):
    print(even_numbers[j])

#3.

numbers_string = str(input("Enter the series of positive numbers with spaces that you want the number of even numbers in printed."))

numbers_list = numbers_string.split()
even_numbers_count = 0
even_numbers = []

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
    if numbers_list[i] % 2 == 0:
         even_numbers_count += 1
         even_numbers.append(numbers_list[i])

even_numbers.sort()

dictionary_of_numbers = dict.fromkeys(even_numbers)

for j in range(1, len(dictionary_of_numbers)):
    if even_numbers[j-1] == even_numbers[j]:
        del even_numbers[j]

print("There are", even_numbers_count, "distinct even numbers in the series of positive numbers you inputted:")

for k in range(len(even_numbers)):
    print(even_numbers[k])

#4.

