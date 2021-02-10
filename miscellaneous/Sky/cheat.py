# finding the correct password upon input dico mapping letters correct to the tested password strings and list input possible passwords

def testingPasswords(dico, possibles):
    for candidate in possibles:
        for (test_string, correct_chars) in dico.items():
            same_chars = 0
            visited = set()
            for letter in candidate:
                if letter not in visited:
                    same_chars += test_string.count(letter)
                visited.add(letter)
            if same_chars == correct_chars:  # if these two lines commented out we get False, thus
                #return (True, candidate)     # ensuring we have selected the one and only true answer
                return candidate
    return False

def passwordTestsInputConversionToDicoProgramCanWorkWith(list_input):
    dico = {}
    for index in range(1, len(list_input), 2):  # second index should be int as per input instruction
        try:
            if isinstance(int(list_input[index]), int):
                dico[list_input[index - 1]] = int(list_input[index])  # the integer is relevant to the preceding password test
        except ValueError:
            print("Invalid format of inputs inputted, smh, read the specifications, human")
    return dico


perhapses = str(input("Please enter the candidates for the password, seperated by a space.")).split()

password_tests = passwordTestsInputConversionToDicoProgramCanWorkWith(str(input("Please enter the strings tested for the password,"
                  " seperated by spaces, with the number of characters correct"
                  " in the string following the test string it is applicable to")).split())

# if manual testing with first test case:
# perhapses = {"little34": 2, "rhyno12": 2}  # unique keyyyys remember
# password_tests = ["taller12", "crowded23", "mouse83", "limes52", "thread15", "house49"]

result = testingPasswords(password_tests, perhapses)

if result is not False:
    print("The correct password has been deduced... It is ", result)
else:
    print("The correct password could not be deduced =(")
