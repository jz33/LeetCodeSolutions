'''
935. Knight Dialer
https://leetcode.com/problems/knight-dialer/

A chess knight can move as indicated in the chess diagram below:
 
This time, we place our chess knight on any numbered key of a phone pad (indicated above),
and the knight makes N-1 hops.  Each hop must be from one key to another numbered key.

Each time it lands on a key (including the initial placement of the knight),
it presses the number of that key, pressing N digits total.

How many distinct numbers can you dial in this manner?

Since the answer may be large, output the answer modulo 10^9 + 7.

Example 1:

Input: 1
Output: 10

Example 2:

Input: 2
Output: 20

Example 3:

Input: 3
Output: 46
'''
MOD = 10**9+7

class Solution:
    def getNext(self, i: int) -> int:
        if i == 0:
            return [4,6]
        elif i == 1:
            return [6,8]
        elif i == 2:
            return [7,9]
        elif i == 3:
            return [4,8]
        elif i == 4:
            return [3,9,0]
        elif i == 5:
            return []
        elif i == 6:
            return [1,7,0]
        elif i == 7:
            return [2,6]
        elif i == 8:
            return [1,3]
        elif i == 9:
            return [2,4]
        
    def knightDialer(self, N: int) -> int:
        row = [1] * 10
        for _ in range(1, N):
            newRow = [0] * 10
            for i in range(10):
                for j in self.getNext(i):
                    newRow[j] = (newRow[j] + row[i]) % MOD
            row = newRow
        return sum(row) % MOD
