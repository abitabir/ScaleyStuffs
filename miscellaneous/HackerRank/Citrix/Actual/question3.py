"""
3. Disk Space Analysis


A company is performing an analysis on the computers at its main office. The computers
are spaced along a single row. For each group of contiguous computers of a certain length, that is, for each segment,
determine the minimum amount of disk space available on a computer. Return the maximum of these values as your answer.



Example

n = 4, the number of computers

space = [8, 2, 4, 6]

x = 2, the segment length



The free disk space of computers in each of the segments is [8, 2], [2, 4], [4, 6].  The minima of the three segments are [2, 2, 4].  The maximum of these is 4.



Function Description

Complete the function segment in the editor below.



segment has the following parameter(s):

    int x:  the segment length to analyze

    int space[n]:  the available hard disk space on each of the computers



Returns:

    int: the maximum of the minimum values of available hard disk space found while analyzing the computers in segments of length x



Constraints

1 ≤ n ≤ 106

1 ≤ x ≤ n

1 ≤ space[i] ≤ 109



Input Format for Custom Testing
Sample Case 0
Sample Input

STDIN     Function
-----     -----
1      →  length of segments x = 1
5      →  size of space n = 5
1      →  space = [1, 2, 3, 1, 2]
2
3
1
2


Sample Output

3


Explanation

The segments of size x = 1 are [1], [2], [3], [1], and [2]. Because each segment only contains 1 element, each value is minimal with respect to the segment it is in. The maximum of these values is 3.

"""

def diskSpaceAnalysis(segments_length, space_size, space):

    def segmentingValidly(segments_length, space_size, space):
        segments = [space[i:i + segments_length] for i in range(len(space) - segments_length + 1)]
        return segments

    segments = segmentingValidly(segments_length, space_size, space)
    return max(min(minning) for minning in segments)

print(diskSpaceAnalysis(1, 5, [1, 2, 3, 1, 2]))
print(diskSpaceAnalysis(2, 4, [8, 2, 4, 6]))
