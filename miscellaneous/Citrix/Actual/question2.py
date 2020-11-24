
"""
2. Equal Levels
Two signals are being generated as part of a simulation. A program monitors the signals. Whenever the two signals become equal at the same time, the frequency is noted. A record is maintained for the maximum simultaneous frequency seen so far. Each time a higher simultaneous frequency is noted, this variable (maxequal) is updated to the higher frequency.



Note:

Both signals start at time t=0, but their durations might be different. In this case, the comparison of equality is performed only until the end of the shorter signal.
If both signals have equal frequencies at a given time but the frequency is less than or equal to the current maximum frequency, maxequal, is not updated.


The running times of both signals are given, denoted by n and m respectively. During the course of the simulation, how many times is the maxequal variable updated?



Example

signalOne = [1, 2, 3, 3, 3, 5, 4]

signalTwo = [1, 2, 3, 4, 3, 5, 4]







Each of the first three signals match and are increasing, so maxequal is updated 3 times to 1, 2 and then 3.

At the fourth time, they are not equal.

At the fifth, they are equal to 3. Since maxequal contains 3 already, it is not updated.

At the sixth time, both signals are equal to 5. This is greater than maxequal = 3, so now maxequal = 5.

At the final time, signals are equal to 4. Since 4 is less than maxequal, it is not updated.

maxEqual was updated a total of 4 times.



Function Description



Complete the updateTimes function in the editor below.



updateTimes has the following parameter(s):

    int signalOne[n]: the frequencies of the first signal

    int signalTwo[m]: the frequencies of the second signal

Return

    int:  the number of updates



Constraints

1 ≤ n ≤ 105
0 ≤ signalOne[i] ≤ 109
1 ≤ m ≤ 105
0 ≤ signalTwo[i] ≤ 109


Input Format For Custom Testing
Sample Case 0
Sample Input For Custom Testing

STDIN     Function
-----     --------
5    →    signalOne[] size n = 5
1    →    signalOne = [1, 2, 3, 4, 1]
2
3
4
1
5    →    signalTwo[] size m = 5
5    →    signalTwo = [5, 4, 3, 4, 1]
4
3
4
1
Sample Output

2
Explanation





The frequencies are equal during three periods, with frequencies 3, 4 and 1.

The maximum frequency is updated twice at 3, and 4, since 4 is greater than 3.

It is not updated when their values are 1 because 1 is less than the current maxequal = 4.

"""


def updateTimes(signalOne, signalTwo):
    maxequal = None
    updated_count = 0
    minSignal = signalOne if len(signalOne) > len(signalTwo) else signalTwo
    for time_index in range(len(minSignal)):
        if signalOne[time_index] == signalTwo[time_index]:
            if maxequal is not None:
                if signalOne[time_index] > maxequal:
                    maxequal = signalOne[time_index]
                    updated_count += 1
            else:
                maxequal = signalOne[time_index]
                updated_count += 1
    return updated_count

print(updateTimes([1, 2, 3, 2, 54, 5, 4], [1, 2, 3, 2, 45, 5, 4]))