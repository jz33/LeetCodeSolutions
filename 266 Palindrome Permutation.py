'''
266. Palindrome Permutation
https://leetcode.com/problems/palindrome-permutation/

Given a string s, return true if a permutation of the string could form a
palindrome and false otherwise.

Example 1:

Input: s = "code"
Output: false

Example 2:

Input: s = "aab"
Output: true

Example 3:

Input: s = "carerac"
Output: true

Constraints:
    1 <= s.length <= 5000
    s consists of only lowercase English letters.
'''
def geHistogram(src: str) -> List[int]:
    histogram = [0] * 26
    for c in src:
        histogram[ord(c) - ord('a')] += 1
    return histogram

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        histogram = geHistogram(s)
        oddy = 0
        for count in histogram:
            if count & 1 == 1:
                oddy += 1
            if oddy > 1:
                return False
        return True
