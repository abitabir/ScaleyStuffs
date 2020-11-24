#1.
def reverse_dictionary(dico):
    reverse_dico = {}
    for key, val in dico.items():
        reverse_dico[val] = key
    return(reverse_dico)

dico = {"one":1, "two":2}

print(reverse_dictionary(dico))

#2.
def no_values_duplicates_found_check(dico):
    for key1, val1 in dico.items():
        for key2, val2 in dico.items():
            if key1 != key2:
                if val1 == val2:
                    return("None")
    return("T")

def reverse_dictionary(dico):
    reverse_dico = {}
    for key, val in dico.items():
        reverse_dico[val] = key
    return(reverse_dico)

dico = {"one":1, "two":2, "three":2}

if no_values_duplicates_found_check(dico) == "T":
    print(reverse_dictionary(dico))
else:
    print(no_values_duplicates_found_check(dico))
    print("As keys are unique, yet there are duplicate values that are to become keys within the values list, so reverse dictionary cannae be created.")
