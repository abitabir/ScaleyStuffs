
def flatten(list_2D):
    list_1D = []
    for i in range(len(list_2D)):
        for j in range(len(list_2D[i])):
            list_1D.append(list_2D[i][j])
    return(list_1D, list_2D)


list_1D, list_2D = flatten([[1,2],[3,4,5,6],[7],[8,9]])

print(list_2D, "flattened is", list_1D)

list_1D, list_2D = flatten([[1,2],[],[7],[]])

print(list_2D, "flattened is", list_1D)
