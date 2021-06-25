# #1.
# try:
#     with open("precipitations-Europe.txt") as f:
#         for line in f:
#             if not line.startswith("#"):
#                 print(line)
# except IOError as error:
#     print("file doesn't exist")
#     print(error)

# #2.
# try:
#     f = open("precipitations_min_avg_max_display_script.txt", "w+")
# except IOError as error:
#     print("an errror has occured")
#     print(error)

#3.
def converting_data_from_text_file_into_data_can_manipulate(filename):
    with open(filename) as g:
        lines = []
        for line in g:
            string = ""
            if not line.startswith("#"):
                for character in line:
                    if character.isnumeric() or character == "." or character == ",":
                        string += character
                line = string.split(",")
                lines.append(line)
        return(lines)

def getting_data_solely_from_data(data):
    sole_data = []
    for list_in_list in data:
        sole_data.append(float(list_in_list[1]))
    return(sole_data)

def min_precipitation_index(sole_data, data):
    min_data = min(sole_data)
    for index in range(len(data)):
        if min_data == float(data[index][1]):
            return(index)

def max_precipitation_index(sole_data, data):
    max_data = min(sole_data)
    for index in range(len(data)):
        if max_data == float(data[index][1]):
            return(index)

def avg_precipitation(sole_data, data):
    total = 0
    count = len(sole_data)
    for value in sole_data:
        total += value
    average = round(total/count, 2)
    average = str(average)
    return(average)


try:
    filename = "precipitations-Europe.txt"  #from here change all subsquent 'filename's
    f = open("precipitations_min+avg+max_display_script.txt", "w+")
except IOError as error:
    print("an errror has occured [file doesn't exist or sommat]")
    print(error)
else:
    #finally getting round to using the three-four methods defined above
    data = converting_data_from_text_file_into_data_can_manipulate(filename)
    sole_data = getting_data_solely_from_data(data)
    min_data_index = min_precipitation_index(sole_data, data)
    max_data_index = max_precipitation_index(sole_data, data)
    avg_data = avg_precipitation(sole_data, data)
    f.write("The minimum precipitation from the data in " + filename + " is " + data[min_data_index][1] + " in the year of " + data[min_data_index][0] + ".\n")
    f.write("The maximum precipitation from the data in " + filename + " is " + data[max_data_index][1] + " in the year of " + data[max_data_index][0] + ".\n")
    f.write("The average precipitation from the data in " + filename + " is " + avg_data + ".")
    f.close()