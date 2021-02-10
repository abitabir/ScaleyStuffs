"""
3. Shifting Strings
The following operations on a string are defined:

Left Shift: A single circular rotation of the string in which the first character becomes the last character and all other characters are shifted one index to the left. For example, abcde becomes bcdea after one left shift and cdeab after two left shifts.
Right Shift: A single circular rotation of the string in which the last character becomes the first character and all other characters are shifted one index to the right. For example, abcde becomes eabcd after one right shift and deabc after two right shifts.


Example

s = 'abcdefg'

leftShifts = 2

rightShifts = 4



The string abcdefg shifted left by 2 positions is cdefgab. The string cdefgab shifted right by 4 positions is fgabcde, the string to return.



Function Description

Complete the function getShiftedString in the editor below.



getShiftedString has the following parameter(s):

    string s:  the string to shift

    int leftShifts: number of shifts left

    int rightShifts:  number of shifts right



Returns:

    string: a string shifted left or right



Constraints

1 ≤ length of s ≤ 105
0 ≤ leftShifts, rightShifts ≤ 109
String s consists of lowercase English alphabetic letters only, ascii[a-z].


Input Format for Custom Testing
Sample Case 0
Sample Input 0

STDIN           Function
-----           --------
abcd     →      s = "abcd"
1        →      leftShifts = 1
2        →      rightShifts = 2



Sample Output 0

dabc


Explanation 0

Initially, s is abcd.

leftShifts = 1 : abcd → bcda
rightShifts = 2 : bcda → abcd → dabc
The function then returns dabc.
"""


def getShiftedStringLoopy(s, leftShifts, rightShifts):
    output = s
    # if s.islower() and 100001 > len(s) > 1 and leftShifts > -1 and rightShifts > -1 and 1000000001 > leftShifts != rightShifts < 1000000001:
    if len(s) > 1 and leftShifts != rightShifts:
        if leftShifts > len(s):
            leftShifts = leftShifts % len(s)
        elif rightShifts > len(s):
            rightShifts = rightShifts % len(s)
        if leftShifts > rightShifts:
            leftShifts -= rightShifts
            rightShifts = 0
        elif rightShifts > leftShifts:
            rightShifts -= leftShifts
            leftShifts = 0
        else:
            leftShifts = 0
            rightShifts = 0
        for shift in range(1, leftShifts + 1):
            output = output[1:] + output[0]
        for shift in range(1, rightShifts + 1):
            output = output[-1] + output[:-1]
    return output


print(getShiftedStringLoopy("abcd", 0, 2476925))


def getShiftedString(string, left_shifts, right_shifts):

    def _doctoring_shifts_for_efficency(left_shifts, right_shifts):
        if left_shifts > right_shifts:
            left_shifts -= right_shifts
            right_shifts = 0
            if left_shifts > len(string):
                left_shifts = left_shifts % len(string)
        elif right_shifts > left_shifts:
            right_shifts -= left_shifts
            left_shifts = 0
            if right_shifts > len(string):
                right_shifts = right_shifts % len(string)
        else:
            left_shifts = 0
            right_shifts = 0
        return left_shifts, right_shifts

    output = string
    if len(string) > 1 and left_shifts != right_shifts:
        left_shifts, right_shifts = _doctoring_shifts_for_efficency(left_shifts, right_shifts)
        if right_shifts != 0:
            output = output[-right_shifts:] + output[:-right_shifts]
        if left_shifts != 0:
            output = output[left_shifts:] + output[:left_shifts]
    return output

print(getShiftedString("abcdefg", 2, 4))
print(getShiftedString("abcd", 0, 2476925))
print(getShiftedString("1243514", 4352, 513))



