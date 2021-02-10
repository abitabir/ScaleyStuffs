"""
You are inside question view of Geological Sorting

1h 16m left
Skip to main content
ALL

1
2
3
4
1. Geological Sorting
A team of geologists attempting to measure the differences in carbon-dated volcanic materials and non-volcanic materials. You need to compare the volcanic material with non-volcanic material of the same carbon-dated age in order to establish a base for testing.

You are given 2 arrays, volcanic and nonVolcanic. Find a list of materials with identical dates between both arrays. Return this list in descending order (i.e, the highest age followed by second highest, with the lowest age at the end).



For example, you are given the following two arrays:

volcanic = [7000, 13400, 7000, 14000] ,and
nonVolcanic = [7000, 13400, 150000, 7000]


Your return array should show: result = [13400, 7000, 7000]



The date 7000 is present twice in both input arrays. Therefore, there are two matches and both should be returned in the output array. Likewise, 13400 is present in both arrays and should be returned in the output array. However, there is no matching number for 150000 in volcanic or 14000 in nonVolcanic, so these two numbers should not be returned in result.



Function Description

Complete the function sortIntersect in the editor below. The function must return an array (in descending order) of the dates of matching pairs that can be created between volcanic and nonVolcanic.



sortIntersect has the following parameter(s):

    volcanic[volcanic[0],...volcanic[n-1]]:  an array of integers

    nonVolcanic[nonVolcanic[0],...nonVolcanic[o-1]]:  an array of integers



Constraints

5 ≤ n, o ≤ 1,000

6,600 ≤ volcanic[i], nonVolcanic[j] ≤ 18,300



Input Format for Custom Testing
Sample Case 0
Sample Input 0

5
7000
7000
12000
13000
6900
7
6910
7010
7000
12000
18000
15000
10450
Sample Output 0

12000
7000
Explanation

volcanic = {7000, 7000, 12000, 13000, 6900} 

nonVolcanic = {6910, 7010, 7000, 12000, 18000, 15000, 10450}

sortIntersect(volcanic, nonVolcanic) = {12000, 7000}



The integers 12000 and 7000 appear in both arrays. Although there is a second piece of volcanic material with the same 7000-year age, it has no equivalent in non-volcanic material, so it cannot be duplicated in the output array.

"""

def sortIntersect(volcanic, nonVolcanic):
    volcanic.sort()
    volcanic = volcanic[::-1]  # to descending order
    nonVolcanic.sort()
    nonVolcanic = nonVolcanic[::-1]
    result = []
    index = 0
    while volcanic != [] and nonVolcanic != []:
        # as long one of them is not empty, we shall continue to remove elements according to conditions
        # the deletions occur to make sure first elements of both lists have a small range/to confusions when comparing
        print(result, volcanic, nonVolcanic)
        if volcanic[index] == nonVolcanic[index]:
            # if both are present, remove both elements from both arrays and add element to result
            result.append(volcanic[index])
            del volcanic[index]
            del nonVolcanic[index]
        else:
            if volcanic[index] > nonVolcanic[index]:
                # means first element of this list is greater than first elements of that list AND all its subsequent
                # elements, as rememember we sorted it into descending order
                del volcanic[index]
            else:  # since volcanic[index] < nonVolcanic[index]
                del nonVolcanic[index]
    return result

print(sortIntersect([5, 6, 7,8,34, 6], [45, 6767, 6, 4 ,6, 7, 8]))