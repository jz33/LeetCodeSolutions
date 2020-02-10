'''
821. Shortest Distance to a Character
https://leetcode.com/problems/shortest-distance-to-a-character/

Given a string S and a character C, return an array of integers representing the shortest distance
from the character C in the string.

Example 1:

Input: S = "loveleetcode", C = 'e'
Output: [3, 2, 1, 0, 1, 0, 0, 1, 2, 2, 1, 0]
 

Note:

S string length is in [1, 10000].
C is a single character, and guaranteed to be in string S.
All letters in S and C are lowercase.
'''
class Solution:
    def shortestToChar(self, S: str, C: str) -> List[int]:
        size = len(S)
        zeros = [i for i in range(size) if S[i] == C]
        zi = 0
        result = [0] * size
        for i, e in enumerate(S):
            zz = zeros[zi]
            if i == zz:
                if zi + 1 < len(zeros):
                    zi += 1
            else:
                if i > zz:
                    result[i] = i - zz
                elif zi == 0:
                    result[i] = zz - i
                else:
                    result[i] = min(zz - i, i - zeros[zi-1])
        return result
                
                
