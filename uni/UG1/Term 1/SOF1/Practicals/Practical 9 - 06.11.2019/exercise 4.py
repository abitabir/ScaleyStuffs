def print_file_contents_in_uppercase():
    f = None
    try:
        f = open('sentencesfull.txt', 'r')
    except IOError:
        print("something has gone wrong")
    else:
        line = f.readlines()
        for element in line:
            print(element.upper())
    finally:
        if f != None:
            f.close()

print_file_contents_in_uppercase()

def print_file_contents_in_uppercase_v2():
    with open('sentencesfull.txt', 'r') as input_file:
        for line in input_file:
            print(line.upper())

print_file_contents_in_uppercase_v2()