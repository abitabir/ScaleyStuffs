# much simpler than I T.T https://www.testengineerblog.com/post/2018-10-27-degree-of-an-array/

"""
4. Degree of an Array
Given an array of integers, its degree is defined as the number of occurrences of the element that occurs most frequently in the array. Given a list of integers, determine two properties:

the degree of the array
the length of the shortest sub-array that shares that degree


Example

arr = [1, 2, 1, 3, 2]



The array has a degree of 2 based on the occurrences of values 1 and 2. The subarray of degree 2 based on the 1's is [1, 2, 1] and based on 2's is [2, 1, 3, 2]. Their lengths are 3 and 4, so the shortest is length 3. Return the shortest length.



Function Description

Complete the function degreeOfArray in the editor below. The function must return an integer denoting the minimum size of the subarray such that the degree of the subarray is equal to the degree of the array.



degreeOfArray has the following parameter(s):

    int arr[n]:  an array of integers indexed from 0 to n-1



Return

    int:  the minimum size of the subarrays that have a degree equal to the degree of the array



Constraints

1 ≤ n ≤ 105
1 ≤ arr[i]≤ 106


Input Format For Custom Testing
Sample Case 0
Sample Input

STDIN    Function
-----    --------
5    →   arr[] size n = 5
1    →   arr = [1, 2, 2, 3, 1]
2
2
3
1
Sample Output

2
Explanation

The array arr  has a degree of 2 based on elements values 1 and 2 because each occurs two times. The subarrays with a degree of 2 are:

[1, 2, 2, 3, 1], which has a length of 5.
[2, 2], which has a length of 2.


Return minimum( 2, 5 ) = 2
"""


def creating_dico_of_occurances(arr):
    dico = {-1: 0}
    for item in arr:
        if item in dico:
            dico[item] += 1
        else:
            dico[item] = 1
    dico.pop(-1)  # or del dico[-1]
    return dico


# def finding_mode_or_modes(dico):  # less efficent methinks? more iterative
#     mode = [-1]
#     for key in dico:
#         if mode[0] == -1 or dico[key] > dico[mode[0]]:
#             mode = [key]
#         elif dico[key] == dico[mode[0]]:
#             mode.append(key)
#     return mode


def finding_degree_and_modes(dico):
    # degree is the number of occurrences of the element(orand//&s) that occurs most frequently in the array
    modes = set()
    mode = max(dico, key=dico.get)  # returns one of the keys with the highest values
    modes.add(mode)
    degree = dico[mode]  # variable holds max of all values in the dico
    for key in dico:
        if dico[key] == degree:
            modes.add(key)
    return modes, degree


def finding_subarrays_with_same_degree_as_array(array, modes, degree):
    subarrays = {}
    for mode in modes:
        subarray = []
        mode_count = 0
        index = 0
        while mode_count < degree and index < len(array):  # until all occurrence of the mode have been added to the subarray
            element = array[index]
            if element == mode:
                mode_count += 1
            if mode_count > 0:  # starting adding to array from when first occurrence of mode found
                subarray.append(element)
            index += 1
        subarrays[mode] = subarray  # technically, I don't even need a memory of the subarray XO but it's good for debugging
    return subarrays


def finding_subarrays_with_same_degree_as_array(array, modes, degree):
    subarrays = {}
    for mode in modes:
        subarray = []
        mode_count = 0
        index = 0
        while True:  # until all occurrence of the mode have been added to the subarray
            element = array[index]
            if element == mode:
                mode_count += 1
            if mode_count > 0:  # starting adding to array from when first occurrence of mode found
                subarray.append(element)
            index += 1
            if mode_count < degree and index < len(array):
                break
        subarrays[mode] = subarray  # technically, I don't even need a memory of the subarray XO but it's good for debugging
    return subarrays


def minimum_length_of_subarray_with_same_degree_as_array(subarrays, array):
    # smallest_subarray = subarrays[min(subarrays, key=len(subarrays.get))]  # holding one of smallest subarrays,
    # buuut method dun seem to work with [1,4,2,6,2,3,3,1,5,12,5]
    # max_key_and_val = max(dico.items())  # returns
    # smallest_subarray = min(subarrays.items())  # contains (x, y) tuple where x is greatest key and y is corresponding value
    smallest_subarray_length = len(array)
    for mode in subarrays:  # fine, after much reluctance, iteration is the way to go
        subarray = subarrays[mode]
        if len(subarray) < smallest_subarray_length:
            smallest_subarray_length = len(subarray)
    return smallest_subarray_length


def degreeOfArrayNaive(array):  # very naive and longwinded, though it did pass all of the tests alhamdulillah
    output = 0
    if array != []:
        dico_of_occurrences = creating_dico_of_occurances(array)
        modes, degree = finding_degree_and_modes(dico_of_occurrences)
        subarrays_with_same_degree_as_array = finding_subarrays_with_same_degree_as_array(array, modes, degree)
        output = minimum_length_of_subarray_with_same_degree_as_array(subarrays_with_same_degree_as_array, array)
    return output


def degreeOfArray(array):  # this version is smarter and more easier on eyes, but not as efficient, time limit exceeded
    def _degree_of_array(array):
        from collections import Counter  # we can do this as we are only importing Counter from the module
        # Counter is a container/object that tracks how many times equivalent values are added, niftily implementing the
        # same algorithms for which other languages commonly use bag or multiset data structures
        # all three of the following would return Counter({'b': 3, 'a': 2, 'c': 1})
        # collections.Counter(['a', 'b', 'c', 'a', 'b', 'b']) == collections.Counter({'a':2, 'b':3, 'c':1}) == collections.Counter(a=2, b=3, c=1)
        C = Counter(array)
        degree = max(C.values())
        return degree

    def _shortest_subarray_length(array, subarrays):
        output = len(array)
        for subarray in subarrays:
            if len(subarray) < output:
                output = len(subarray)
        return output

    # remember, cannae add unhashable type list to set - not that we really need it heres, hum
    # list comprehension adding all subarrays of array only if they contain same degree (occurrences of mode/most common
    # number) - is meant to be more efficent than usual loopings
    array_degree = _degree_of_array(array)  # make separate variable as opposed to calling function every time in every
    # iteration of list comprehension
    all_possible_subarrays = [array[i:j] for i in range(len(array)) for j in range(i + 1, len(array) + 1) if _degree_of_array(array[i:j]) == array_degree]
    # above line has O(n^2) complexity due to nested list
    # returning the length of the smallest array in the list
    #>return len(min(all_possible_subarrays))  # incorrect answers given using this so have to iterate using _shortest_subarray_length fucntion
    shortest_subarray_length = _shortest_subarray_length(array, all_possible_subarrays)
    return shortest_subarray_length


import time
start_time = time.time()
print(degreeOfArray([1,4,2,6,2,3,3,1,5,12,5]))
print("My first program took", float(time.time() - start_time), "to run")
second_start_time = time.time()
print(degreeOfArrayNaive([1,4,2,6,2,3,3,1,5,12,5]))
print("My second program took", float(time.time() - second_start_time), "to run")
# these timings take into account time it takes to assign to the start_time variables as well
# it is important to note that time taken may also be affected by background processes in the CPU
# I don't really trust this module's reliability tho...
