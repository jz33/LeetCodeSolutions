'''
10. Regular Expression Matching
https://leetcode.com/problems/regular-expression-matching/

Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.

Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the preceding element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".

Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".

Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore, it matches "aab".

Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
'''
def isMatch(txt: str, pat: str) -> bool:
    '''
    New DP iterative method
    '''
    # dp[i][j] means whether pat[i:] matches txt[j:]
    dp = [[False] * (len(txt) + 1) for _ in range(len(pat) + 1)]

    # Iterate from back, very special...
    for i in range(len(pat), -1, -1):
        for j in range(len(txt), -1, -1):
            matchCurrrent = i < len(pat) and j < len(txt) and (pat[i] == txt[j] or pat[i] == '.')

            if i == len(pat) and j == len(txt):
                # Of course, empty txt matches empty pat
                dp[i][j] = True

            elif i+1 < len(pat) and pat[i+1] == '*':
                # If next pat is '*', 2 cases when dp[i][j] can be true:
                # 1. Skip it, which means * at pat[i+1] nulldify pat[i], and so pat[i+2:] should match txt[j:]
                # 2. If pat[i:] matches txt[j+1:], which means char pat[i] matches char txt[j+1],
                # then if pat[i] matches txt[j], we have pat[i] == txt[j] == txt[j+1], and * at pat[i+1] can copy
                # this char (pat[i+1] can be replaces by that char), and so pat[i:] and txt[i:] can match.
                # Notice dp[i][j] cannot be inferredd based on dp[i+1][j+1] because '*' in front is meaningless
                dp[i][j] = dp[i+2][j] or matchCurrrent and dp[i][j+1]

            else:
                # If next pat is not '*' or pat is empty, matches current and move both 1 step
                dp[i][j] = matchCurrrent and dp[i+1][j+1]

    return dp[0][0]


from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        sl = len(s)
        pl = len(p)

        @lru_cache(None)
        def topDown(si: int, pi: int) -> bool:
            '''
            @si: index in s
            @pi: index in p
            '''
            # If pattern is empty, string must be empty
            if pi == pl:
                return si == sl

            isMatched = si < sl and (p[pi] == '.' or p[pi] == s[si]) 

            # If next pattern is '*', skip '*' or if current match, let '*' matches more than 1 char in string
            if pi + 1 < pl and p[pi + 1] == '*':
                return topDown(si, pi + 2) or isMatched and topDown(si + 1, pi)
            
            # If next pattern char is not '*' or pattern reached last char,
            # current must match and later must match too.
            return isMatched and topDown(si + 1, pi + 1)
        
        return topDown(0, 0)
