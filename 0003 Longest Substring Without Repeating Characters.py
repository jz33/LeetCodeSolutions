'''
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring
without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3
Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1
Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3
Explanation: The answer is "wke", with the length of 3.
Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:
    0 <= s.length <= 5 * 104
    s consists of English letters, digits, symbols and spaces.
'''
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = {}
        maxLength = 0
        left = 0 # left index of the substring window
        for i, e in enumerate(s):
            if e in seen:
                # Not left = seen[e] + 1, as left can > seen[e] + 1
                left = max(left, seen[e] + 1)
            seen[e] = i
            maxLength = max(maxLength, i - left + 1)
        return maxLength
