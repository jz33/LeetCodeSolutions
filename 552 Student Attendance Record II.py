'''
552. Student Attendance Record II

Given a positive integer n, return the number of all possible attendance records with length n, which will be regarded as rewardable. The answer may be very large, return it after mod 109 + 7.

A student attendance record is a string that only contains the following three characters:

'A' : Absent.
'L' : Late.
'P' : Present.
A record is regarded as rewardable if it doesn't contain more than one 'A' (absent) or more than two continuous 'L' (late).

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

class Node:
    def __init__(self):
        self.total = 0 # total count
        self.L1 = 0 # string with 1 ending 'L', including AL
        self.L2 = 0 # string with 2 ending 'L', including ALL
        self.A = 0 # string contains 1 "A", including AL & ALL
        self.AL = 0 # string contains 1 "A", 1 ending 'L'
        self.ALL = 0 # string contains 1 "A", 2 ending 'L'

    def modd(self):
        self.total %= MOD
        self.L1 %= MOD
        self.L2 %= MOD
        self.A %= MOD
        self.AL %= MOD
        self.ALL %= MOD
        return self
        
    def __str__(self):
        return r'{}, {}, {}, {}, {}, {}'.format(self.total, self.L1, self.L2, self.A, self.AL, self.ALL)

    
class Solution:
    def checkRecord(self, n: int) -> int:
        '''
        Day[i] solely depends on Day[i-1]
        '''
        # Build day 1, ['P', 'L', 'A']
        day = Node()
        day.total = 3 # string with no "L" ending
        day.L1 = 1
        day.A = 1

        for i in range(1, n):
            newDay = Node()

            # Append 'P'
            newDay.total = day.total
            newDay.A = day.A

            # Append 'L'
            newDay.L1 = day.total - day.L1 - day.L2 # L0
            newDay.L2 = day.L1
            newDay.AL = day.A - day.AL - day.ALL # A0
            newDay.ALL = day.AL
            newDay.A += day.A - day.ALL
            newDay.total += day.total - day.L2

            # Apply 'A'
            newDay.A += day.total - day.A
            newDay.total += day.total - day.A

            day = newDay.modd()

        return day.total
