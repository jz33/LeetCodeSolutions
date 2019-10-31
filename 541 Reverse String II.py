'''
541. Reverse String II
https://leetcode.com/problems/reverse-string-ii/

Given a string and an integer k, you need to reverse the first k characters for every 2k characters counting from
the start of the string. If there are less than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters,
then reverse the first k characters and left the other as original.

Example:

Input: s = "abcdefg", k = 2
Output: "bacdfeg"
'''
class Solution:
    def reverseStr(self, s: str, k: int) -> str:
        res = []
        for i in range(0, len(s), k*2):
            res.append(s[i : min(i+k, len(s))][::-1])
            # 2nd string can be null. s[len(s):] is null
            res.append(s[min(i+k, len(s)) : min(i+k*2, len(s))])
        return ''.join(res)
