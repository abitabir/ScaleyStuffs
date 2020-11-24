
def rasterise(list_1D, width):
    if len(list_1D) % width != 0:
        return None
    else:
        list_2D = []
        for i in range(int(len(list_1D)/width)):
            list_in_lists = []
            list_2D.append(list_1D[width*i:width*(i+1)])
        return(list_2D, list_1D, width)

out_put, in_put, width = rasterise([1,2,3,4,5,6,7,8], 4)

print("rasterising the list", in_put, "into lists within list of width", width, "gives you", out_put)
