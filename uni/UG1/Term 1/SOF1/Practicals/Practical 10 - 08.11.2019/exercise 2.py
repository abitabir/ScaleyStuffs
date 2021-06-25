#1.
def converting_data_from_text_file_into_data_can_manipulate(filename):
    with open(filename) as g:
        lines = {}
        for line in g:
            string = ""
            if not line.startswith("#"):
                for character in line:
                    if character.isnumeric() or character == "." or character == ",":
                        string += character
                line = string.split(",")
                key = line[0]
                value = line[1]
                lines[key] = value
        return(lines)


try:
    #"precipitations-Europe.txt" and "precipitations-NAmerica.txt" and "precipitations-world.txt" files opening
    f = open("precipitations_records.txt", "w+")
    precipitations_europe_dico = converting_data_from_text_file_into_data_can_manipulate("precipitations-Europe.txt")
    precipitations_north_america_dico = converting_data_from_text_file_into_data_can_manipulate(
        "precipitations-NAmerica.txt")
    precipitations_world_dico = converting_data_from_text_file_into_data_can_manipulate("precipitations-world.txt")
except IOError as error:
    print("an errror has occured [file doesn't exist or sommat]")
    print(error)
else:
    f.write("#The selected annual precipitation records from Europe, North America and the World.\n")
    #since sorted(precipitations_europe_dico) == sorted(precipitations_north_america_dico) == sorted(precipitations_world_dico):
    for year_key in sorted(precipitations_world_dico):
        f.write(year_key)
        f.write(": ")
        f.write(precipitations_europe_dico[year_key])
        f.write(", ")
        f.write(precipitations_north_america_dico[year_key])
        f.write(", ")
        f.write(precipitations_world_dico[year_key])
        f.write("\n")
    f.close()

# 2. Write a function  that
# does the same thing as in (1). The function should collate the data from all the files in
# the list filenames (note, the filenames is a list of string) and save the collated
# data into the file named outputfile (note outputfile is a string representing the
# name of the file)

#2.

filenames = ["precipitations-Europe.txt", "precipitations-NAmerica.txt", "precipitations-world.txt"]
outputfile = "precipitations_records.txt"
def collate_precipitation(filenames, outputfile):
    ...yadayadayada