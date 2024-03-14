'''
1358. Number of Substrings Containing All Three Characters
https://leetcode.com/problems/number-of-substrings-containing-all-three-characters/

Given a string s consisting only of characters a, b and c.

Return the number of substrings containing at least one occurrence of all these characters a, b and c.

Example 1:

Input: s = "abcabc"
Output: 10
Explanation: The substrings containing at least one occurrence of the characters a, b and c
are "abc", "abca", "abcab", "abcabc", "bca", "bcab", "bcabc", "cab", "cabc" and "abc" (again). 

Example 2:

Input: s = "aaacb"
Output: 3
Explanation: The substrings containing at least one occurrence of the characters a, b and c are "aaacb", "aacb" and "acb". 

Example 3:

Input: s = "abc"
Output: 1

Constraints:
    3 <= s.length <= 5 x 10^4
    s only consists of a, b or c characters.
'''
class Solution:
    '''
    Simpler hashmap solution
    '''
    def numberOfSubstrings(self, src: str) -> int:
        result = 0
        # The seen records the last-seen index of 'a' or 'b' or 'c'.
        # It is an array so it's easy to get min
        # If a char is -1 it means it is not seen yet
        seen = [-1] * 3
        for i, c in enumerate(src):
            seen[ord(c) - ord('a')] = i
            # If substring [a : b] is valid, all substrings [a-1:b]...[0:b] are valid
            # Then, get the 1st appearance of the valid substring, which is min(seen)
            # If there is a char not yet appear, min(seen) will be -1
            result += 1 + min(seen)
        return result