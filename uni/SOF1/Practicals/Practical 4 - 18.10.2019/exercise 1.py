given_number = str(input("Enter the number for which you want the sum of the digits."))
digits = list(given_number)
print(sum(int(x) for x in digits))
