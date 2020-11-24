# but I did these after the recursions harder, hmmm lollies


def is_power_recursively(a, b):
    if a == b:
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
    if len(str(summing)) == 1:
        return summing
    else:
        return int(str(summing)[0]) + sum_digits_recursively(int(str(summing)[1:]))


print(sum_digits_recursively(345))


def recursive_sum(number_list):
    if len(number_list) == 0:  # base case when adding
        return 0
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


def something_ish(word, pattern):  # first slice pattern - and - then slice word - or
    if len(word) == 0 or len(pattern) == 0:  # catching errors and program crashings
        return "No."

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


def flatten(mlist):  # not so snazzy flattening multidimensional array list
    def _flattening(lst, flattened=[]):  # possibleto pass list through as parameter and have it be changed by functions
        # within functions cuz lists are mutable
        if isinstance(lst[0], int):  # base case
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
Exercise 6:
Write a recursive function merge(sorted_listA, sorted_listB) that merges the
two lists into a single sorted list and returns it. The two parameters are list of comparable
objects that are sorted in ascending order. For example, the lists contain only strings, or the
lists contain only numbers.

"""