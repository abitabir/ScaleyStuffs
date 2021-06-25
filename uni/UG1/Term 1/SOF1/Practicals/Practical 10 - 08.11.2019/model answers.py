#exercise 1
try:
    datafile = open('Data/precipitations-europe.txt')
except IOError as err:
    print ('The following error occurred:',err)
else:
    data = datafile.readlines()
    datafile.close() # we have read the full content of the file so we can close it
    min_precipitation = []
    max_precipitation = []
    average_precipitation = 0.0
    row = 1 # first line should be omitted

    while row < len(data):
        
        cells = data[row].split(',')
        cells[0] = int(cells[0])
        cells[1] = float(cells[1])
        if (len(min_precipitation) == 0 or
            cells[1] < min_precipitation[1]):
            min_precipitation = [cells[0], cells[1]]

        if (len(max_precipitation) == 0  or
            cells[1] > max_precipitation[1]):
            max_precipitation = [cells[0], cells[1]]
            
        average_precipitation += cells[1]

        row += 1
        
    print ("min precipitation was", min_precipitation[1], end='')
    print (" and it occurred in",min_precipitation[0],)
    
    print ("max precipitation was", max_precipitation[1], end='')
    print (" and it occurred in",max_precipitation[0])
        
    print ("the average precipitation in last century was",
           average_precipitation/(len(data)-1))


    


#exercise 2a
datarecords = {}    # keys are years, value are list of three floats:
                    # precipitation for Europe, NAmerica, World
list_of_files = ['Data/precipitations-europe.txt',
               'Data/precipitations-NAmerica.txt',
               'Data/precipitations-world.txt']
valid_list_of_files = []

for filename in list_of_files:
    try:
        datafile = open(filename)
    except IOError as err:
        print ('The following error occurred:',err)
    else:
        valid_list_of_files.append(filename)
        data = datafile.readlines()
        datafile.close()
        row = 1 # first line should be ommitted
        while row < len(data):
            
            cells = data[row].split(',')

            # convert each cell to its appropriate type rather than keeping
            # all cells as string
            cells[0] = int(cells[0])
            cells[1] = float(cells[1])
            if cells[0] in datarecords:
                datarecords[cells[0]].append(cells[1])
            else:
                # must create a list containing a single element
                datarecords[cells[0]] = [cells[1]]

            row += 1


## This section of the code deals with writing the collated data to
## a text file (.CSV)
output_file = None
try:
    output_file = open('Data/collatedFiles.txt','w')
except IOError as err:
    print ('The following error occurred:',err)
else:
    # write the header of the file, e.g. column names
    output_file.write('Years,')
    output_file.write(','.join(valid_list_of_files))
    output_file.write('\n')
    output_file.flush()

    # write the data. item is a tuple containing item[0]: the key (e.g. year)
    # and item[1] the list of values (three in this case) corresponding the
    # precipitation for that particular year.
    for item in sorted(datarecords.items()):
        output_file.write(str(item[0]))
        for value in item[1]:
            output_file.write(',')
            output_file.write(str(value))
        output_file.write('\n')
        output_file.flush()
finally:
    if output_file is not None:
        output_file.close()


#exercise 2b
def read_datafile(fileName):
    try:
        datafile = open(fileName)
    except IOError as err:
        print ('The following error occurred:',err)
        raise   # We don't want to deal with the error here
                # We let the calling function deal with it.
    else:
        data = datafile.readlines()
        datarecords = {}
        datafile.close()
        row = 1 # first line should be ommitted
        while row < len(data):
            
            cells = data[row].split(',')
            if cells[0] in datarecords:
                raise ValueError() # there should not be duplicate year in the file
            else:
                datarecords[int(cells[0])] = float(cells[1])

            row += 1
        return datarecords
    


def collate_precipitations(filenames,output_filename):
    '''
    Collate the data of all the files where the name is in the list of string
    filenames and store the collated data in the file whose name is given by
    the parameter output_filename (a string). files that cannot be opened are simply
    ignored. It is assumed that the data in each file is correct and complete,
    e.g. all contains the same years. Note no checking is done regarding the
    validity of the data.
    The data is written as a CSV file.
    
    '''
    list_datarecords = {}    # keys are years, value are list of three floats:
                    # precipitation for Europe, NAmerica, World or whatever the 
                    # files past in parameters
    valid_list_of_files = []
    for name in filenames:
        try:
            datarecords = read_datafile(name)
        except IOError as err:
            print ('The following error occurred:',err)
        except ValueError as err:
            print ("duplicate year in file", name)
        else:
            valid_list_of_files.append(name)
            for item in datarecords.items():
                if item[0] in list_datarecords:
                    list_datarecords[item[0]].append(item[1])
                else:
                    list_datarecords[item[0]] = [item[1]]

    ## This section of the code deals with writing the collated data to
    ## a text file (.CSV)
    outputfile = None
    try:
        outputfile = open(output_filename,'w')
    except IOError as err:
        print(err)
        raise
    else:
        # write the header of the file, e.g. column names
        outputfile.write('Years,')
        outputfile.write(','.join(valid_list_of_files))
        outputfile.write('\n')
        outputfile.flush()

        # write the data. item is a tuple containing item[0]: the key (e.g. year)
        # and item[1] the list of values (three in this case) corresponding the
        # precipitation for that particular year.
        for item in sorted(list_datarecords.items()):
            outputfile.write(str(item[0]))
            for value in item[1]:
                outputfile.write(',')
                outputfile.write(str(value))
            outputfile.write('\n')
            outputfile.flush()
    finally:
        if outputfile is not None:
             outputfile.close()



##########################################
##      TESTS
#########################################

    
list_of_files = ['Data/precipitations-europe.txt',
           'Data/precipitations-NAmerica.txt',
           'Data/precipitations-world.txt']

collate_precipitations(list_of_files, 'Data/collated.txt')

#exercise 3
# IN THIS MODEL ANSWER, WE ARE USING A SCRIPT, TRY TO TRANSFORM THE SCRIPT
# INTO ONE OR MORE FUNCTION. DISCUSS WITH ONE OF YOUR PEER YOUR SOLUTION,
# ESPECIALLY HOW MANY FUNCTIONS WOULD YOU USE, WHAT EACH FUNCTION SHOULD DO,
# WHAT ARE THE PARAMETERS AND RETURNED VALUES IF ANY.
#
# ANOTHER IMPROVEMENT IS TO WRITE THE DATA LIKE 971.4000000000001 AS 971.4. 
# SEARCH HOW TO FORMAT A STRING BEFORE WRITING THE STRING INTO A FILE.

##########  READING THE DATA FROM FILE ###########

dataFile = open('Data/aberporth_meteorological_data.txt')
data = dataFile.readlines()
dataFile.close()

row = 2 # data starts at row 2 (third row)
yearRecord = {} #keys are years, values are the list of attribute [frost, rain, sunshine]

while row < len(data):
    
    cells = data[row].split(',')
    if cells[0] in yearRecord:
        record = yearRecord.get(cells[0])
        for index in range(4, len(cells)): # 4 as the data we are interested in is in the 5th-7th columns
            record[index - 4] += float(cells[index]) # -4 is the offset for the indices
    else:
        record = []
        for index in range(4, len(cells)):
            record.append(float(cells[index]))

        yearRecord[cells[0]] = record

    row += 1


###### WRITING THE SUMMARY FILE ########
summaryDataFile = open('Data/aberporth_meteorological_data_summary.txt','w')

summaryDataFile.write(data[0])
cells = data[1].split(',')
cells = [cells[0]] + cells[4:] # append the header of each column
summaryDataFile.write(','.join(cells))
summaryDataFile.flush()

for item in sorted(yearRecord.items()):
    line = item[0]
    for value in item[1]:
        line += ',' +str(value)
            
    summaryDataFile.write(line)
    summaryDataFile.write('\n')
    summaryDataFile.flush()


summaryDataFile.close()

