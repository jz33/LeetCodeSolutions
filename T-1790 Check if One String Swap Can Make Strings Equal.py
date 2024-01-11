'''
1790. Check if One String Swap Can Make Strings Equal
https://leetcode.com/problems/check-if-one-string-swap-can-make-strings-equal/

You are given two strings s1 and s2 of equal length.
A string swap is an operation where you choose two indices in a string (not necessarily different) and swap the characters at these indices.

Return true if it is possible to make both strings equal by performing at most one string swap on exactly one of the strings.
Otherwise, return false.

Example 1:

Input: s1 = "bank", s2 = "kanb"
Output: true
Explanation: For example, swap the first character with the last character of s2 to make "bank".

Example 2:

Input: s1 = "attack", s2 = "defend"
Output: false
Explanation: It is impossible to make them equal with one string swap.

Example 3:

Input: s1 = "kelb", s2 = "kelb"
Output: true
Explanation: The two strings are already equal, so no string swap operation is required.

Constraints:
    1 <= s1.length, s2.length <= 100
    s1.length == s2.length
    s1 and s2 consist of only lowercase English letters
'''
class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        firstDiff = None # None, [0, len(s1)] or -1
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                if firstDiff == -1: # swapped before
                    return False
                if firstDiff is None:
                    firstDiff = i
                else: # needs swap
                    if s1[firstDiff] == s2[i] and s1[i] == s2[firstDiff]:
                        firstDiff = -1
                    else:
                        return False
        return firstDiff is None or firstDiff == -1
