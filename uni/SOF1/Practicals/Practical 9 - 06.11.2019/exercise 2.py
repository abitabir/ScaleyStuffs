# version 1
# def save_list2file(sentences, filename):
#     f = open(filename, "a+") # opens existing, if not creates new (as denoted by +), file with file name filename, which is to have strings appended to it (so no rewriting the file =0)
#     for element in sentences:
#         f.write("\n" + element) # gap (\n) then element of list appended to filename
#     f.close()

# save_list2file(["this is one sentence", "this is another", "here is anotherrrr"], "sentencesfullof.txt")

# version 2

# def save_list2file(sentences, filename):
#     output_file = None
#     try:
#         output_file = open(filename, "a") # opens existing file with file name filename, which is to have strings appended to it (so no rewriting the file =0), if doesn't exist, program will crash, but caught by exception
#     except IOError:
#         print("Thou have inputted a filename which doesn't exist.")
#     else:
#         for element in sentences:
#             output_file.write("\n" + element) # gap (\n) then element of list appended to filename
#         output_file.close()
#     finally:
#         if output_file != None:
#             output_file.close()

# save_list2file(["this is one sentence", "this is another", "here is anotherrrr"], "sentencesfullof.txt")

# version 3

def save_list2file(sentences, filename):
    try:
        with open(filename, 'w') as output_file:
            for element in sentences:
                output_file.write(element + '\n')
    except IOError:
        print("whoops, dies is wrong")
    else:
        output_file.close()