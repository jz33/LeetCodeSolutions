'''
763. Partition Labels
https://leetcode.com/problems/partition-labels/

A string S of lowercase letters is given. We want to partition this string into as many parts as possible so that
each letter appears in at most one part, and return a list of integers representing the size of these parts.

Example 1:
Input: S = "ababcbacadefegdehijhklij"
Output: [9,7,8]

Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits S into less parts.
Note:

S will have length in range [1, 500].
S will consist of lowercase letters ('a' to 'z') only.
'''
class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        book = {} # {char : last appeared index}
        for i, c in enumerate(S):
            book[c] = i
        
        left = 0 # left index of interval, inclusive
        last = 0 # last index this char appears
        res = []
        for i,c in enumerate(S):
            last = max(last, book[c])                         
            if i == last:
                res.append(i - left + 1)
                left = i + 1
        return res
