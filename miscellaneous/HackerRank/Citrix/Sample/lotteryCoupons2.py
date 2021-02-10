"""
2. Lottery Coupons
There is a lottery with n coupons and n people take part in it. Each person picks exactly one coupon. Coupons are numbered consecutively from 1 to n, n being the maximum ticket number. The winner of the lottery is any person who owns a coupon where the sum of the digits on the coupon is equal to s. If there are multiple winners, the prize is split equally among them. Determine how many values of s there are where there is at least one winner and the prize is split among most people.



Example

n = 12



The list of coupon numbers generated from 1 to n is [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]. The sums of the digits are [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3]. The largest number of winners is 2 which will occur for coupons numbered [1, 10], [2, 11] and [3, 12]. The maximum number of possible winners occurs for any of these 3 possible values of s, so 3 is the answer.



Function Description

Complete the function lotteryCoupons in the editor below. The function must return the number of ways to choose s in such a way that there is at least one winner and the prize is split among the greatest number of people.


lotteryCoupons has the following parameter(s):

    n: an integer that represents the maximum coupon number



Constraints

1 ≤ n ≤ 104


Input Format For Custom Testing
Sample Case 0
Sample Input

STDIN     Function
-----     --------
3      →  n = 3


Sample Output

3


Explanation

The three lottery coupons are numbered 1, 2 and 3. The sum of the digits of the coupon numbers are 1, 2 and 3 respectively. There are three ways to choose s:

When s = 1, only the person with coupon number = 1 is the winner.
When s = 2, only the person with coupon number = 2 is the winner.
When s = 3, only the person with coupon number = 3 is the winner.

"""

# s is winning_sums

def creatingDico(n):
    dico = {-1: []}  # dico of digit sums keys to coupon numbers values in list
    for coupon_number in range(1, n + 1):  # exclusive 0, inclusive n
        digit_sum = 0
        for digit in str(coupon_number):
            digit_sum += int(digit)
        if digit_sum in dico:
            dico[digit_sum].append(coupon_number)
        else:
            dico[digit_sum] = [coupon_number]
    return dico


def maxNumberOfWinners(dico):
    max_number_of_winners = [-1]
    for sums in dico:
        if len(dico[sums]) > len(dico[max_number_of_winners[0]]):
            max_number_of_winners = [sums]
        elif len(dico[sums]) == len(dico[max_number_of_winners[0]]):
            max_number_of_winners.append(sums)
    return max_number_of_winners


def lotteryCoupons(n):
    dico = creatingDico(n)
    max_number_of_winners = maxNumberOfWinners(dico)
    return len(max_number_of_winners)

