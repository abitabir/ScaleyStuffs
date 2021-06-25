#1.
dico1 = {"one":1, "two":2, "three":3}
dico2 = {"four":4, "five":5}

def concat_dico(dico1, dico2):
    concatenated_dico = {}
    for key, val in dico1.items():
        concatenated_dico[key] = val
    for key, val in dico2.items():
        concatenated_dico[key] = val
    return(concatenated_dico)

print(concat_dico(dico1, dico2))

#2.
dico1 = {"one":1, "two":2, "five":5}
dico2 = {"two": "10", "five":"101"}

def concat_dico(dico1, dico2):
    concatenated_dico = {}
    for key, val in dico1.items():
        concatenated_dico[key] = val
    for key, val in dico2.items():
        if key in concatenated_dico:
            concatenated_dico[key] = [concatenated_dico[key], val]
        else:
            concatenated_dico[key] = val
    return(concatenated_dico)

print(concat_dico(dico1, dico2))

