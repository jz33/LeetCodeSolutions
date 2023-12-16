'''
763. Partition Labels
https://leetcode.com/problems/partition-labels/

You are given a string s. We want to partition the string into as many parts as possible
so that each letter appears in at most one part.

Note that the partition is done so that after concatenating all the parts in order,
the resultant string should be s.

Return a list of integers representing the size of these parts.

Example 1:

Input: s = "ababcbacadefegdehijhklij"
Output: [9,7,8]
Explanation:
The partition is "ababcbaca", "defegde", "hijhklij".
This is a partition so that each letter appears in at most one part.
A partition like "ababcbacadefegde", "hijhklij" is incorrect, because it splits s into less parts.

Example 2:

Input: s = "eccbbbbdec"
Output: [10]

Constraints:
    1 <= s.length <= 500
    s consists of lowercase English letters.
'''
class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        appearances = {} # {char : last appeared index}
        for i, c in enumerate(s):
            appearances[c] = i
        
        left = 0 # left index of interval
        last = 0 # last index any char of the substring appears
        result = []
        for i, c in enumerate(s):
            last = max(last, appearances[c])                         
            if i == last:
                # This is the position where the last char of the substring
                result.append(i - left + 1)
                left = i + 1
        return result
