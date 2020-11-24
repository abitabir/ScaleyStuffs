def to_upper_case(input_file, output_file):
    try:
        f = open(input_file,'r')
        g = open(output_file, 'w+')
    except IOError as err:
        print("something has gone wrong")
        print(err)
    else:
        line = f.readlines()
        for element in line:
            g.write(element.upper())
        f.close()

to_upper_case('sentencesfull.txt', 'sentencesfullof.txt')

def to_upper_case_model_answer(input_file, output_file):
    data_in = []    
    with open(input_file, 'r') as in_file:
        data_in = in_file.readlines()
        
    with open(output_file, 'w+') as out_file:
        for data in data_in:
            out_file.write(data.upper())