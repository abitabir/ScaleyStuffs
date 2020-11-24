#1.
def map_list(keys, values):
    dico = {}
    for index in range(min(len(keys), len(values))):
        dico[keys[index]] = values[index]
    return(dico)

print(map_list(["un", "two"], [1,2]))

#2.
def no_keys_duplicates_found_check(keys):
    for i in range(len(keys)):
        for j in range(len(keys)):
            if i != j:
                if keys[i] == keys[j]:
                    return("None")
    return("T")
                
def map_list2(keys, values):
    dico = {}
    for index in range(min(len(keys), len(values))):
        dico[keys[index]] = values[index]
    return(dico)

##list_of_keys = ["un", "two"]
##list_of_values = [1,2]

list_of_keys = ["un", "two", "un"]
list_of_values = [1,2]

if no_keys_duplicates_found_check(list_of_keys) == "T":
    print(map_list(list_of_keys, list_of_values))
else:
    print(no_keys_duplicates_found_check(list_of_keys))
    print("As keys are unique, yet there are duplicate keys within the keys list.")
