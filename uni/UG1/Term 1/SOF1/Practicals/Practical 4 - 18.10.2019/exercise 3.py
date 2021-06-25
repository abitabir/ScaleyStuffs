
def binary_number_to_decimal_number(binary_number):
    binary_number_digits = list(str(binary_number))
    binary_number_digits.reverse()

    for h in range(len(binary_number_digits)):
        binary_number_digits[h] = int(binary_number_digits[h])

    decimal_number = 0

    for i in range(len(binary_number_digits)):
        decimal_number += binary_number_digits[i] * pow(2, i)
    return(decimal_number)

binary_number = input("Enter the binary number you want to convert into a decimal value.")
decimal_number = binary_number_to_decimal_number(binary_number)
print("The binary number", binary_number, "in decimal is", decimal_number)
