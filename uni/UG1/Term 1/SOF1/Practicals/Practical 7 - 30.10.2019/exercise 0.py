
months_of_year = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}

roman_keys_arabic_numbers = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}

first_seven_elements_of_periodic_table = {"H": "hydrogen", "He": "helium", "Li": "lithium", "Be": "beryllium", "B": "boron", "C": "carbon", "N": "nitrogen"}

roman = {}

roman[100000] = "T"
roman[1000] = "M"
roman[500] = "D"
roman[100] = "K"
roman[50] = "L"
roman[10] = "X"
roman[5] = "V"
roman[1] = "I"

roman[100] = "C"
del roman[100000]
print(roman)
