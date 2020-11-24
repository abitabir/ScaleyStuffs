#codemaker_code = list(input("Codemaker, enter a five digit number that you want the Codebreaker to attemot to break:"))

import random
codemaker_code = list(str(random.randint(10000, 99999)))
print(codemaker_code)

codebreaker_code = list(str(input("The code you have to break has been generated. Codebreaker, enter a five digit numbered guess with which you want to break the code:")))
result_list = []
result = ""

for i in range(5):
    if codemaker_code[i] == codebreaker_code[i]:
        result_list.append("R")
        repeat = i
    else:
        for j in range(5):
            #if j == repeat:
                #pass
            if codemaker_code[i] == codebreaker_code[j]:
                result_list.append("B")

result_list.sort()
result = result.join(result_list)
print(result)
