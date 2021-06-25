# Exercise 3: Hard.
# For this exercise, we will be using the file .
# Your job is to read the data from the file, calculate the number of days of air frost (af), the
# total amount of rain (mm), and the total amount of sunshine (hours) for each year. You must
# save your calculations in a Comma Separated file (.csv), where the rows are the data for each
# year, and the columns is the calculation for each attribute.
# Try to open the file using MS Excel to see if you saved the data correctly




def converting_data_from_text_file_into_data_can_manipulate(filename):
    with open(filename) as g:
        lines = {}
        for line in g:
            if not line.startswith("#"):
                line = line.split(",")
                key = line[0]
                value = line[2:]
                if line[0] not in lines.keys():
                    lines[key] = value
                else:
                    for index in range(len(lines[key])):
                        lines[key][index] = round((float(lines[key][index]) + float(value[index])), 2)
            
        return(lines)

print(converting_data_from_text_file_into_data_can_manipulate("aberporth_meteorological_data.txt"))