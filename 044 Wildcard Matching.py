'''
44 Wildcard Matching
https://oj.leetcode.com/problems/wildcard-matching/

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input:
s = "aa"
p = "*"
Output: true
Explanation: '*' matches any sequence.

Example 3:

Input:
s = "cb"
p = "?a"
Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:

Input:
s = "adceb"
p = "*a*b"
Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:

Input:
s = "acdcb"
p = "a*c?b"
Output: false
'''
 def isMatch(self, txt: str, pat: str) -> bool:
        '''
        DP iterative method based on regular expression matching
        '''
        # dp[i][j] means whether pat[i:] matches txt[j:]
        # Notice i and j can be length of the string, which
        # represents the empty txt or pat       
        dp = [[False] * (len(txt) + 1) for _ in range(len(pat) + 1)]

        for i in range(len(pat), -1, -1):
            for j in range(len(txt), -1, -1):
                matchCurrrent = i < len(pat) and j < len(txt) and (pat[i] == txt[j] or pat[i] == '?')

                if i == len(pat) and j == len(txt):
                    # Of course, empty txt matches empty pat
                    dp[i][j] = True

                elif i < len(pat) and pat[i] == '*':
                    # If current pat is '*', 2 cases when dp[i][j] can be true:
                    # 1. Skip it, which means * matches nothing, and so pat[i+1:] must match txt[i:]
                    # 2. If pat[i:] matches txt[j+1:], since * matches anything, and it can be extended
                    # to the char on txt[j], and therefore pat[i:] can match txt[j:]
                    # This is the diffrent part to Regular Expression Matching
                    dp[i][j] = dp[i+1][j] or (j < len(txt) and dp[i][j+1])

                else:
                    # If current pat is not '*' or pat is empty, matches current and move both 1 step
                    dp[i][j] = matchCurrrent and dp[i+1][j+1]

        return dp[0][0]
