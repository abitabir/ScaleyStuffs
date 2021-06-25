def  pairwise_digits(first_given_number, second_given_number):
    output = ''
    
    first_digits = list(str(first_given_number))
    second_digits = list(str(second_given_number))

    if len(first_digits) > len(second_digits):
        longer_digits = first_digits
        shorter_digits = second_digits
    else:
        shorter_digits = first_digits
        longer_digits = second_digits

    for i in range(len(shorter_digits)):
        if longer_digits[i] == shorter_digits[i]:
            output = output + '1'
        else:
            output = output + '0'

    for j in range((len(longer_digits)-len(shorter_digits))):
        output = output + '0'

    return(output)

first_given_number = input('Enter the first of the two numbers whose digits you want to compare.')
second_given_number = input('Enter the second of the two numbers whose digits you want to compare.')

print(pairwise_digits(first_given_number, second_given_number))
