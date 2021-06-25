def _cutting(length, prices):  # returning the max price if rod of length length cut
    # return prices[1] + recursive_rod_cutting(length - 1, prices)  # was
    cutting_prices = [prices[i] + recursive_rod_cutting(length - i, prices) for i in range(1, int(length/2) + 1)]
    # going through all the different ways you could cut including duplicate/half cuttings - so up until the median
    # e.g cutting rod of length 4 into 2 and 2
    return max(cutting_prices)


def _not_cutting(length, prices):
    return prices[length]  # one of the base cases - returning the price if rod of length length not cut


def recursive_rod_cutting(length, prices=[0, 1, 5, 8, 9, 10, 17]):
    """
    Function goes through all of the different ways of cutting up a rod, and returns the maximum price you could make
    out of a rod of length whatever, as long as a list is passed as a parameter, of the prices corresponding to the
    index as the rod length.
    """
    prices_of_various_cuts = []
    if length == 0 or length == 1:
        return prices[length]
    prices_of_various_cuts.append(_cutting(length, prices))
    prices_of_various_cuts.append(_not_cutting(length, prices))
    return max(prices_of_various_cuts)

print(recursive_rod_cutting(4))




# def get_key(dico, item):  # 'builtin_function_or_method' object is not iterable
#     for pair in dico.items:
#         if item == pair[1]:
#             return pair[0]

def get_key(dico, item):
    for key in dico:
        if dico[key] == item:
            return key


def _cutting_returning_dico(length, prices, various_cuts_by_cutting_once_with_prices={}):
    for i in range(1, int(length / 2) + 1):
        # various_cuts_by_cutting_once_with_prices[prices[i] + get_key(_recursive_rod_cutting_best_cut(length - i, prices), (length - i))] = [i, length - i]
        # above, was previous version, veRYYY longwindedly smh lol
        price = prices[i] + prices[length - i]
        various_cuts_by_cutting_once_with_prices[price] = [i, length - i]
    return various_cuts_by_cutting_once_with_prices


def _not_cutting_returning_dico(length, prices, various_cuts_by_cutting_once_with_prices={}):
    various_cuts_by_cutting_once_with_prices[prices[length]] = [length]
    return various_cuts_by_cutting_once_with_prices


# class dict: trying to add a new function to dict data type didn't work. also turns out there is already a method for this. called update. lol.
# https://stackoverflow.com/questions/4698493/can-i-add-custom-methods-attributes-to-built-in-python-types
#     def add_all(self, other):  # function adding all elements of one dico to the former
#         for key in other:
#             self[key] = other[key]
#         return


def recursive_rod_cutting_best_cut(length, prices=[0, 1, 5, 8, 9, 10, 17]):
    """
    Function goes through all of the different ways of cutting up a rod, and returns the best singular cut that'll give
    you the maximum price you could make out of a rod of length whatever, as long as a list is passed as a parameter, of
    the prices corresponding to the index as the rod length.
    """
    dico_of_all_cuts_and_prices_by_cutting_only_once = _recursive_rod_cutting_best_cut(length, prices)
    print(dico_of_all_cuts_and_prices_by_cutting_only_once)
    pair = max(dico_of_all_cuts_and_prices_by_cutting_only_once.items())
    return "cuts: " + str(pair[1]) + "\n" + "will give you monies of: " + str(pair[0])


def _recursive_rod_cutting_best_cut(length, prices=[0, 1, 5, 8, 9, 10, 17], various_cuts_by_cutting_once_with_prices={}):
    if length == 0 or length == 1:
    #    various_cuts_with_prices[[length]] = prices[length]  # unhashable type list, so prices as key though some cuts may be lost =S
        various_cuts_by_cutting_once_with_prices[prices[length]] = [length]
        return various_cuts_by_cutting_once_with_prices
    various_cuts_by_cutting_once_with_prices.update(_cutting_returning_dico(length, prices))
    various_cuts_by_cutting_once_with_prices.update(_not_cutting_returning_dico(length, prices))
    return various_cuts_by_cutting_once_with_prices


print(recursive_rod_cutting_best_cut(4))