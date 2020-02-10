'''
https://leetcode.com/discuss/interview-question/502496/google-onsite-substrings-that-dont-have-every-character-in-an-alphabet

I botched this question in a Google onsite interview but worked out the solution later.

Suppose you have a string, haystack, and a set of characters which may or may not appear in that string, alphabet.
(No characters appear in alphabet more than once, because it's a set.)
How many non-empty sub-strings of haystack do not contain every character in alphabet?
Write a function that accepts haystack and alphabet as input and returns an answer to this question as an integer.

Example:

Input: haystack = "cab", alphabet = ['a', 'c']
Output: 4
Explanation:
We can enumerate all 6 non-empty substrings of `cab`:
"c" - this does not have `a`.
"a" - this does not have `c`.
"ca" - this has every entry in `alphabet`.
"b" - this does not have `a` or `c`.
"ab" - this does not have `c`.
"cab" - this has every entry in `alphabet`.
4 of these substrings don't have every answer, so the function should return 4.
'''
from collections import Counter
from typing import List, Set

class Solution:
    def countOfSubStringContainsNotAllChar(self, haystack: str, alphabet: Set[str]) -> int:
        '''
        Sliding window
        '''
        # left pointer
        left = 0 

        # States
        charCount = 0
        chars = Counter()

        # Result
        total = 0

        for i, c in enumerate(haystack):
            # add
            chars[c] += 1
            if c in alphabet and chars[c] == 1:
                charCount += 1

            # shrink
            while charCount == len(alphabet):
                lc = haystack[left]
                left += 1
                chars[lc] -= 1
                if c in alphabet and chars[lc] == 0:
                    charCount -= 1

            # update result
            total += i - left + 1

        return total


sol = Solution()

testcases = [
('cab', {'a', 'c'}),
('abcdef', {'b', 'c'})
]

for haystack, alphabet in testcases:
    print(sol.countOfSubStringContainsNotAllChar(haystack, alphabet))
