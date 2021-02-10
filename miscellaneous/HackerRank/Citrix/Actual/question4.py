"""
4. Calculate Region
There is a straight line of students of various heights. The students' heights are given in in the form of an array, in the order, they are standing in the line.

Consider the region of a student as the length of the largest subarray that includes that student's position, and in which that student's height is equal to maximum height among all students present in that subarray. Return the sum of the region of all students.



For example-

heights = [1, 2, 1]
The longest subarray in which the first student's height is equal to maximum height among all other students is [1]; thus, the length of the region of the first student is 1.
The longest subarray in which the second student's height is equal to maximum height among all other students is [1, 2, 1]; thus, the length of the region of the second student is 3.
The longest subarray in which the third student's height is equal to maximum height among all other students is [1]; thus, the length of the region of the third student is 1.
Thus, the sum of the lengths of all regions of all students is 1+3+1 = 5.

# so confusingly worded, really. You meant the subarray in which the student in question's height is the greatest of all the heights. uhhh okay.

Function Description

Complete the function calculateTotalRegion in the editor below. The function must return the desired sum of all regions.



calculateTotalRegion has the following parameter(s):

   heights: an array of the heights of students standing in the line



Constraints

1 ≤ length of heights ≤ 105
1 ≤ heights[i] ≤ 109


Input Format For Custom Testing
Sample Case 0
Sample Input For Custom Testing

3
1
2
1
Sample Output

5
Explanation

The input corresponds to the example given in the statement. The answer is 5 and it is explained in the statement.

Sample Case 1
Sample Input For Custom Testing

4
1
1
1
1
Sample Output

16
Explanation

For example :

heights [1,1,1,1]

The longest subarray in which first student's height is equal to maximum height among all other students is [1, 1, 1, 1], thus the region of the first student is 4.
The longest subarray in which the second student's height is equal to maximum height among all other students is [1, 1, 1, 1], thus the region of the second student is 4.
The longest subarray in which the third student's height is equal to maximum height among all other students is [1, 1, 1, 1], thus the region of the third student is 4.
The longest subarray in which the fourth student's height is equal to maximum height among all other students is [1, 1, 1, 1], thus the region of the fourth student is 4.
Thus, the sum of the region of all students is 4+4+4+4 = 16.
"""


def findAllValidSubarraysWithThisHeight(heights, height_index):
    all_possible_subarrays = [heights[i:j] for i in range(len(heights)) for j in range(i + 1, len(heights) + 1) if
                              containsHeightOfSpecificChildInQuestion(i, j, height_index) and isValidSubarray(
                                  heights[height_index], heights[i:j])]
    return all_possible_subarrays


def containsHeightOfSpecificChildInQuestion(i, j, height_index):
    # return i >= height_index and j > height_index  # was unfortunately this, cuz BUGGINESSES smh lol
    return i <= height_index and j > height_index  # cuz i is included in the slice whereas j is excluded


def isValidSubarray(height, subarray):  # if height of kid in question is the greatest height in the subarray/subcongaline
    return height == max(subarray)


def findSubarrayWithGreatestLength(subarrays):
    output = []
    for subarray in subarrays:
        if len(subarrays) > len(output):
            output = subarray
    return output


def calculateTotalRegion(heights):
    areas = []
    for height_index in range(len(heights)):
        subarrays = findAllValidSubarraysWithThisHeight(heights, height_index)
        print(subarrays)
        region_subarray = findSubarrayWithGreatestLength(subarrays)
        areas.append(len(region_subarray))
    return sum(areas)


print(calculateTotalRegion([1, 2, 1]))
