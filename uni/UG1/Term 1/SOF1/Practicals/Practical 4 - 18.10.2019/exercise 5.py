def sum_list_in_list(data):
    total = 0
    output = []
    for row in data:
        for value in row:
            total += value
        output.append(total)
    return(output)

data = [[1,2,3], [2], [1, 2, 3, 4]]

output = sum_list_in_list(data)

print(output)
