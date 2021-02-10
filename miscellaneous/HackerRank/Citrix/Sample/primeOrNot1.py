"""
1. Prime or Not?
Given an integer, if the number is prime, return 1. Otherwise return its smallest divisor greater than 1.



Example

n = 24



The number 24 is not prime: its divisors are [1, 2, 3, 4, 6, 8, 12, 24]. The smallest divisor greater than 1 is 2.



Function Description

Complete the function isPrime in the editor below.



isPrime has the following parameter(s):

    long n:  a long integer to test

Returns

    int: if the number is prime, return 1; otherwise returns the smallest divisor greater than 1



Constraints

2 ≤ n ≤ 1012
Input Format for Custom Testing
Sample Case 0


Sample Input 0

STDIN      Function
-----      --------
2      →   n = 2


Sample Output 0

1


Explanation 0

As 2 is a prime number, the function returns 1.
"""

def isPrime(n):
    divisor = 1
    divisors = []
    while divisor < n and len(divisors) < 3:
        if n % divisor == 0:
            divisors.append(divisor)
        divisor += 1
    if len(divisors) == 1:
        return 1
    else:
        return divisors[1]