'''
409. Longest Palindrome
https://leetcode.com/problems/longest-palindrome/

Given a string s which consists of lowercase or uppercase letters, return the length of the longest
palindrome
 that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome.

Example 1:

Input: s = "abccccdd"
Output: 7
Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

Input: s = "a"
Output: 1
Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:
    1 <= s.length <= 2000
    s consists of lowercase and/or uppercase English letters only.
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        histo = Counter(s)
        result = 0
        hasOdd = False
        for count in histo.values():
            if count % 2 == 0:
                result += count
            else:
                hasOdd = True
                result += count - 1
        return result + 1 if hasOdd else result