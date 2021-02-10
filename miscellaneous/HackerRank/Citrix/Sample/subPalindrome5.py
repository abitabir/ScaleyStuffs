"""
5. Sub-palindrome
A palindrome is a string that reads the same forward and backward, e.g. 121 or tacocat. A substring is a contiguous subset of characters in a string. Given a string s, how many distinct substrings of s are palindromic?



Example

s = "mokkori"



Some of its substrings are [m, o, k, r, i, mo, ok, mok, okk, kk, okko]. There are 7 distinct palindromes [m, o, k, r, i, kk, okko].



Function Description

Complete the function palindrome in the editor below.



palindrome has the following parameter(s):

    string s:  a string

Returns:

    int: the number of distinct palindromes as an integer.



Constraints

1 ≤ |s| ≤ 5000
Each character s[i] ∈ ascii[a-z]


Input Format for Custom Testing
Sample Case 0
Sample Input 0

STDIN     Function Parameters
-----     -------------------
aabaa  →  s = "aabaa"
Sample Output 0

5
Explanation 0

Palindromic substrings are [a, aa, aabaa, aba, b].

The substring 'a' occurs 4 times, but is counted only once. Similarly, the substring 'aa' occurs twice but counts as one distinct palindrome.

The number of distinct palindromes is 5.

"""

def palindrome(string):
    # getting all the valid substrings of a string through iterations and adding to set via set comprehension
    distinct_palindromic_substrings = set(string[i:j] for i in range(len(string)) for j in range(i + 1, len(string) + 1) if string[i:j] == string[i:j][::-1])
    return len(distinct_palindromic_substrings)

def palindromee(string):
    from itertools import combinations
    distinct_palindromic_substrings = set(string[x:y] for x, y in combinations(range(len(string) + 1), r=2) if string[x:y] == string[x:y][::-1])
    return len(distinct_palindromic_substrings)


print(palindrome("mokkori"))
print(palindrome(""))
print(palindrome("121"))

