'''
5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/

Given a string s, return the longest palindromic substring in s.

Example 1:

Input: s = "babad"
Output: "bab"
Explanation: "aba" is also a valid answer.

Example 2:

Input: s = "cbbd"
Output: "bb"

Constraints:
    1 <= s.length <= 1000
    s consist of only digits and English letters.
'''
def getMaxPalindromicRange(word: str, left: int, right: int):
    '''
    Get the range of maximum palindrome in word
    @return: [left, right], both inclusive
    '''
    while left > -1 and right < len(word) and word[left] == word[right]:
        left -= 1
        right += 1
    # Be careful about the return, as left and Right are already invalid
    return left + 1, right - 1

class Solution:
    def longestPalindrome(self, word: str) -> str:
        maxLeft, maxRight = 0, 0
        for i in range(len(word)):
            left, right = getMaxPalindromicRange(word, i, i)
            if right - left > maxRight - maxLeft:
                maxLeft = left
                maxRight = right
            left, right = getMaxPalindromicRange(word, i, i + 1)
            if right - left > maxRight - maxLeft:
                maxLeft = left
                maxRight = right
        return word[maxLeft : maxRight + 1]
            
