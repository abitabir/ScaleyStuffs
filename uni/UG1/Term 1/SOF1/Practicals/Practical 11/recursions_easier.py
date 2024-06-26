# but I did these after the recursions harder, hmmm lollies


def is_power_recursively(a, b):
    """
    is a a power of b?
    """
    if b == 0:
        if a == 0:  # 0^x = 0 (x != 0)
            return True
        else:  # 0^0 is undefined
            return False
    elif a == 1:  # case for b^0 = 1, b != 0
        return True
    elif a == b:  # b to power 1 gives a
        return True
    elif a % b == 0:
        return is_power_recursively(int(a/b), b)
    else:
        return False

def is_power_iteratively(a, b):
    dividing = a
    is_power_of = True  # assuming it is true, until it is proven it is not true
    while dividing >= b and is_power_of:  # need good end conditions for while loops
        if dividing % b == 0:
            dividing /= b
        else:
            is_power_of = False
    return is_power_of

print(is_power_recursively(27, 3))
print(is_power_iteratively(27, 3))


def find_factorial_recursively(summing):
    if summing == 0 or summing == 1:  # base cases when multiplying - if you multiply everything by 0, it all gown
        return summing
    else:
        return summing * find_factorial_recursively(summing - 1)

print(find_factorial_recursively(3))


def sum_digits_recursively(summing):
    if summing < 0:
        return sum_digits_recursively(-summing)
    elif len(str(summing)) == 1:  # OR elif 0 <= number < 10:
        return summing
    else:
        # OR
        # quotient = number // 10
        # digit = number % 10
        # return digit + sum_digits(quotient)
        return int(str(summing)[0]) + sum_digits_recursively(int(str(summing)[1:]))

print(sum_digits_recursively(345))


def recursive_sum(number_list):
    if len(number_list) == 0:  # base case when adding, catches last possible slices
        return 0  # only adding to the cumulation
    else:
        return number_list[0] + recursive_sum(number_list[1:])


print(recursive_sum([1, 2, 3, 4, 5]))


def is_elfish_using_find(word):
    output = False
    if len(word) >= 3:
        contains_e = True if word.find("e") != -1 else False
        contains_l = True if word.find("l") != -1 else False
        contains_f = True if word.find("f") != -1 else False
        output = contains_e and contains_l and contains_f
    return output


def is_elfish_using_set(word):
    output = False
    word_set = set(word)
    if len(word_set) >= 3:
        output = "e" in word_set and "l" in word_set and "f" in word_set
    return output


def is_only_elfish_recursively(word):  # if word only contains letters specified in the pattern
    pattern = "elf"
    if len(word) == 1:
        return word[0] in pattern  # no need to process anymore after thissss
    else:
        return word[0] in pattern and is_only_elfish_recursively(word[1:])


def is_elfish_recursively(word):  # but not really good implementation, really
    pattern = "elf"
    def _slicing_word(sliced_word, pattern, record=[0, 0, 0]):
        if sliced_word[0] in pattern:  # cheeky decisions really not the point of recursion, hum
            if sliced_word[0] == pattern[0]:
                record[0] += 1
            elif sliced_word == pattern[1]:
                record[1] += 1
            else:
                record[2] += 1
        if len(word) == 1:
            return record
        else:
            _slicing_word(sliced_word[1:], pattern, record)

    record = _slicing_word(word, pattern)
    return record[0] and record[1] and record[3]

print(is_only_elfish_recursively("elffff"), "hey")
print(is_only_elfish_recursively("nay"), "hey")



def is_elfish_lillian(word):
    def elfish(word, pattern):
        if pattern == []:
            return True
        elif word == '':
            return False
        elif word[0] in pattern:
            pattern.remove(word[0])
            return elfish(word[1:], pattern)
        else:
            return elfish(word[1:], pattern)

    return elfish(word,['e', 'l', 'f'])


def something_ish(word, pattern):  # first slice pattern - and - then slice word - or -
#    if len(word) == 0 or len(pattern) == 0:  # catching errors and program crashings
#        return "No."
    if len(pattern) == 0:
        return True
    elif len(word) == 0:
        # as pattern is not empty
        return False

    def _slicing_pattern(word, sliced_pattern):
        if len(sliced_pattern) == 0 or len(sliced_pattern) == 1:  # base case
            return _slicing_word(word, sliced_pattern[0])
        else:
            return _slicing_word(word, sliced_pattern[0]) and _slicing_word(word, sliced_pattern[1:])

    def _slicing_word(sliced_word, sliced_pattern):  # slicing word for the current pattern slice 'iteration'/recursive traversal route
        if len(sliced_word) == 0 or len(sliced_word) == 1:
            return sliced_pattern[0] == sliced_pattern[0]
        else:
            return sliced_pattern[0] == sliced_pattern[0] or _slicing_word(sliced_word[1:], pattern)

    return _slicing_pattern(word, pattern)

print(something_ish("heyelfnelf", "elf"), "it is")  # pretty neat, if I do say so myself XP


def concise_lilly_something_ish(word, pattern):
    def _something_ish(word, pattern):
        if pattern == []:
            return True
        elif word == '':
            return False
        elif word[0] in pattern:
            pattern.remove(word[0])
            return _something_ish(word[1:], pattern)
        else:
            return _something_ish(word[1:], pattern)

    return _something_ish(word, list(pattern))


"""

Exercise 5:
Write a recursive function flatten(mlist) where mlist is a multidimensional list that
returns all the element from mlist into a one-dimensional list. Note, empty lists are ignored.
For examples:
>>> flatten([1,[2,3],4])
[1,2,3,4]
>>> flatten([1,[2,[3,[4]]]])
[1,2,3,4]
>>> flatten([1,2,3,4])
[1,2,3,4]
>>> flatten([1,[]])
[1]
"""

def flatten(mlist):   # mb not so snazzy flattening multidimensional array list
    def _flattening(lst, flattened=[]):  # possible to pass list through as parameter and have it be changed by
        # functions within functions cuz lists are mutable
        if lst == []:  # start recursing back, mate - can't find lst[0] if lst is empty, so error was being raised before this way of catchign error
            return
        elif isinstance(lst[0], int):  # base case - not going into list if it contains integer/not passing int in as lst
            print(lst[0])
            # parameter, catching variable before that
            # ensures lst is indeed always a list
            flattened.append(lst[0])  # only appending when we are sure it is an int!
        else:  # splitting into part we're looking at - first index, and then the rest passed through other function
            _flattening(lst[0], flattened)
        _flattening(lst[1:], flattened)
        return flattened
    flattened = _flattening(mlist)  # have to define variable flattened because it was not predefined within this scope
    return flattened


def flatten_without_inner_function_if_possibleh(mlist, output=[]):  # pretty snazzy flattening of multidimensional array list
    # output defaulted to empty list as there is not meant to be second parameter
    # list can be passed through as parameter and changed by functions within functions cuz lists are mutable
    if isinstance(mlist, int):
        output.append(mlist)
    elif len(mlist) != 0:  # if empty will return []
        flatten_without_inner_function_if_possibleh(mlist[0], output)
        flatten_without_inner_function_if_possibleh(mlist[1:], output)
    return output

#print(flatten([1,[2,3],4]))
print(flatten_without_inner_function_if_possibleh([1,[2,3],4]))



def concise_lilly_flatten(numbers):
    '''
    documentation for flatten(numbers)
    '''
    if numbers == []:
        return []
    elif isinstance(numbers, list):
        return concise_lilly_flatten(numbers[0]) + concise_lilly_flatten(numbers[1:])
    elif isinstance(numbers, (float, int)):
        return [numbers]
    else:
        raise TypeError("invalid type in the list")


"""
Exercise 6:
Write a recursive function merge(sorted_listA, sorted_listB) that merges the
two lists into a single sorted list and returns it. The two parameters are list of comparable
objects that are sorted in ascending order. For example, the lists contain only strings, or the
lists contain only numbers.
"""

def mergingSortedLists(lst1, lst2):
    if lst1 == [] or lst2 == []:
        return lst1 + lst2  # doesn't matter which order really
    elif lst1[0] <= lst2[0]:
        print(lst1[0])
        return [lst1[0]] + mergingSortedLists(lst1[1:], lst2)
    else:
        print(lst2[0])
        return [lst2[0]] + mergingSortedLists(lst1, lst2[1:])


print(mergingSortedLists([3, 4, 5, 6], [1, 2, 4, 6, 9]))

