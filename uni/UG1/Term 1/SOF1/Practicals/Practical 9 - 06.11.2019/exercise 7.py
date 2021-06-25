

#a)

def save_user_data(filename, user_dict):
    """Function erases previous data in file with fie name filename, if not creates new file, and prints user dictionary the amount of times it has been recorded as being used by the user in the same line as its textonyms."""
    f = open(filename, 'w+')
    for dict_key in user_dict:
        f.write(dict_key + ":")
        for lst in user_dict[dict_key]: # in list_of_lists
            this = (" "+lst[0])*int(lst[1])
            f.write(this)
        f.write("\n")
    f.close()

save_user_data('output.txt', {'4663':[['home', 5], ['good', 8], ['hood', 1]], '2':[['a', 50]]})

#b)

def read_from_file(filename):
    user_dict = {}
    f = open(filename, 'r')
    filelines_list = f.readlines()
    for line in filelines_list:
        line = line.split()
        set1 = set()
        for index in range(len(line)):
            if line[index].endswith(":"):
                key = ""
                for character in line[index]:
                    if character != ":":
                        key += character
            else:
                counts = line.count(line[index])
                set1.add((line[index], counts))
        lst = []
        for element in set1:
            lst.append(element)
        user_dict[key] = lst
        f.close()
    return(user_dict)

print(read_from_file('output.txt'))