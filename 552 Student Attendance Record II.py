'''
552. Student Attendance Record II

Given a positive integer n, return the number of all possible attendance records with length n,
which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or
more than two continuous 'L' (late).

Example 1:

Input: n = 2
Output: 8

Explanation:
There are 8 records with length 2 will be regarded as rewardable:
"PP" , "AP", "PA", "LP", "PL", "AL", "LA", "LL"
Only "AA" won't be regarded as rewardable owing to more than one absent times. 
Note: The value of n won't exceed 100,000.
'''
MOD = 10**9+7

class Solution:
    def checkRecord(self, n: int) -> int:
        # Build day 1, ['P', 'L', 'A']
        total = 3 # total count
        L1 = 1 # string with 1 ending 'L', including AL
        L2 = 0 # string with 2 ending 'L', including ALL
        A = 1 # string contains 1 "A", including AL & ALL
        AL = 0 # string contains 1 "A", 1 ending 'L'
        ALL = 0 # string contains 1 "A", 2 ending 'L'

        for i in range(1, n):
            # Append 'P'
            new_total = total
            new_A = A

            # Append 'L'
            new_L1 = total - L1 - L2
            new_L2 = L1
            new_AL = A - AL - ALL
            new_ALL = AL
            new_A += A - ALL
            new_total += total - L2

            # Apply 'A'
            new_A += total - A
            new_total += total - A

            total = new_total % MOD
            L1 = new_L1
            L2 = new_L2
            A = new_A % MOD
            AL = new_AL
            ALL = new_ALL

        return total
