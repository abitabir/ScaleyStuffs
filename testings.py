
def flatten(mlist):   # not so snazzy flattening multidimensional array list
    def _flattening(lst, flattened=[]):  # possible to pass list through as parameter and have it be changed by
        # functions within functions cuz lists are mutable
        if isinstance(lst[0], int):  # base case - not going into list if it contains integer/not passing int in as lst
            # parameter, catching variable before that
            flattened.append(lst[0])  # only appending when we are sure it is an int!
        else:  # splitting into part we're looking at - first index, and then the rest passed through other function
            _flattening(lst[0], flattened)
        _flattening(lst[1:], flattened)
        return flattened
    flattened = _flattening(mlist)  # have to define variable flattened because it was not predefined within this scope
    return flattened


print(flatten([1,[2,3],4]))