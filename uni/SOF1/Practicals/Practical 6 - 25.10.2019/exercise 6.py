table = [[1,2,3], [4,5,6], [7,8,9]]

def sum_column(table):
    if len(table) > 0:
        columns = len(table[0])
        output = columns * [0]
        for row in table:
            if len(row) != columns:
                return None
            for index in range(len(row)):
                output[index] += row[index]
        return output
    return None

print(sum_column(table))
