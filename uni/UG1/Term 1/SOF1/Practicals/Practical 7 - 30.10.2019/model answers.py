def display_dico(dico):
    for key in dico:
        print(key, '-->', dico[key])


# an alternative way to do the same thing
def display_dico2(dico):
    for key, val in dico.items():
        print(key, '-->', val)


def concat_dico(dico1, dico2):
    result = {}
    for key, val in dico1.items():
        result[key] = val

    for key, val in dico2.items():
        # here we assume no common keys between dico1 and dico2
        result[key] = val 

    return result


def concat_dico_advanced(dico1, dico2):
    result = {}
    for key, val in dico1.items():
        result[key] = val

    for key, val in dico2.items():
        if key in result:
            # here there is a common key
            # between dico1 and dico2
            result[key] = [dico1[key],dico2[key]]

        else:
            result[key] = val

    return result


def map_list(keys, values):
    mapped = {}
    for index in range(len(keys)):
        if keys[index] not in mapped:
            mapped[keys[index]] = values[index]
        else:
            print("Error: duplicate value", keys[index], "in the list of keys.")
            return None

    return mapped

def reverse_dictionary(dico):
    reversed = {}
    for key, val in dico.items():
        if val in reversed:
            print("Duplicate values in initial dictionary are not allowed.")
            return None
        else:
            reversed[val] = key

    return reversed

