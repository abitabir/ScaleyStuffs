'''
Created on 3 Nov 2016

@author: Lilian
'''

########### EXERCISE 1 ###################

# a_word = "a short string"
# output_file = open("exo1.txt", 'w')
# output_file.write(a_word)
# output_file.close()

########### EXERCISE 2 ###################

def save_list2file(sentences, filename):
    output_file = None
    try:
        output_file = open(filename, 'w')
    except IOError as err:
        print(err)
    else:
        for aSentence in sentences:
            output_file.write(aSentence + '\n')
    finally:
        if output_file is not None:
            output_file.close()

# Another way to do the try-except-finally for a I/O is to use <with> 
# The with statement manages the resource (in this case the file). Once
# the file is opened, the with statement will ensure the file will be
# closed once the block of code is finished. 
# Note that the with statement does not handle errors if not done 
# explicitely. So if the file <filename> does not exist, the program
# will crash. If you want to handle the exception, you must nest the with
# statement within a try-except.
def save_list2file_with(sentences, filename):
    with open(filename, 'w') as output_file:
        for aSentence in sentences:
            output_file.write(aSentence + '\n')
            

########### EXERCISE 3 ###################

def save_to_log(entry, logfile):
    logs = None
    try:
        logs = open(logfile, 'a')
    except IOError as err:
        print(err)
    else:
        logs.write(entry)
        logs.write('\n') # needed to enter the next entry to a newline
    finally:
        if logs is not None:
            logs.close()

     
        
########### EXERCISE 4 ###################

# with open('sentences.txt', 'r') as input_file:
#     for line in input_file:
#         print(line.upper())


########### EXERCISE 5 ###################

def to_upper_case(input_file, output_file):
    data_in = []    
    with open(input_file, 'r') as in_file:
        data_in = in_file.readlines()
        
    with open(output_file, 'w') as out_file:
        for data in data_in:
            out_file.write(data.upper())
    

########### EXERCISE 6 ###################
def sum_numbers(entry):
    total = 0
    numbers = entry.split()
    for number in numbers:
        total += int(number)
        
    return total
        

def sum_from_file(filename):
    total = 0
    with open(filename, 'r') as input_file:
        for line in input_file:
            total += sum_numbers(line)
            
    return total
                

################## TESTS ################################
save_list2file(["line 1", "line 2", "line 3"], "sentences.txt")
save_to_log("line 4", "sentences.txt")
save_to_log("line 5", "sentences.txt")
        
to_upper_case("sentences.txt", "upper.txt")
print("sum of 1 2 3 4 is 10?", sum_numbers("1 2 3 4") == 10)
print("sum of '   ' should be 0?", sum_numbers("   ") == 0)

print("sum of element in numbers.txt is 100", sum_from_file("numbers1.txt") == 100)

