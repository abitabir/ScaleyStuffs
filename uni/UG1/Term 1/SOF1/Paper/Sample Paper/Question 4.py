"""
4 (15 marks) I/O
The code for this question must be written in the provided file question_4.py.
The aim of this question is to implement a function that reads a table from a csv file, and store it
into a dictionary before returning it. For example, the table shown in Figure 1(a) is stored in a csv
file shown in Figure 1(b).
(a)
Commodity, USA, Canada, Europe, China, India, Australia
Wheat,61.7,27.2,133.9,121,94.9,22.9
Rice Milled,6.3, -,2.1,143,105.2,0.8
Oilseeds,93.1,19,28.1,59.8,36.8,5.7
Cotton,17.3, -,1.5,35,28.5,4.6
(b)
Figure 1: (a) a table in a spreadsheet, and (b) its storage in a csv file.
Page 3 of 7 Continued.
Implement a function import_from_CSV(filename) that takes a string representing the
path to a file and returns a dictionary
The function must raise an IOError if the format of the file does not respect the description below.
The format of the csv file is as follow:
• The first row contains the header of each column separated by a comma. For example,
the table in Figure 1 contains countries in the header of the column.
• The following rows contains the data, where the first element contains the row title (the
commodity in Figure 1), followed by a comma, and then the data for each column
separated by a comma.
• There is no empty line in the file.
• If there is no data in a cell, a ’-’ (dash sign) is used instead.
• If there is a row with too few or too many entries, the function must raise an IOError.
The format of the returned dictionary is as follow:
• The keys of the dictionary are the names of the countries.
• The values are dictionaries containing the data for each country. The keys of these
dictionaries are names of commodities, the values are the quantity produced by that
country for a given commodity. If there is no data for the given commodity (that is a dash
in the csv file), the commodity must not be included in the dictionary. For example, cotton
must not be in the dictionary for Canada. Note, a ’-’ (dash) is different than the value 0.
From the csv file given in Figure 1(b), a sample of the returned dictionary would be:
{’Canada’:{’Wheat’:27.2,’Oilseeds’:19}, ’USA’:{’Wheat’:61.7, ’Cotton’:17.3,...}, ...}
"""

import csv

def import_from_CSV(filename):
    with open(filename, 'r') as file:
        header = file.readline()
        if header.isspace():
            raise IOError
        header = header.split(',')
        for index in range(len(header)):
            header[index] = header[index].strip()
        data = []
        for row in file:
            line = row.split(',')
            if len(line) == len(header):
                for index in range(len(line)):
                    line[index] = line[index].strip()
                data.append(line)
            else:
                raise IOError
        output = dict()
        index = 1
        for country in header[1:]:
            country_data = dict()
            for commodity in data:
                if commodity[index] == '-':
                    pass
                elif commodity[index] != '':
                    country_data[commodity[0]] = float(commodity[index])
                else:
                    raise IOError
            output[country] = country_data
            index += 1
        return output

#import_from_CSV('data//crop_production.csv')