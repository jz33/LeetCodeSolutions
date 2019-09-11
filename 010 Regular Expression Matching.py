'''
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
    # Notice i and j can be length of the string, which
    # represents the empty txt or pat       
    dp = [[False] * (len(txt) + 1) for _ in range(len(pat) + 1)]

    for i in range(len(pat), -1, -1):
        for j in range(len(txt), -1, -1):
            matchCurrrent = i < len(pat) and j < len(txt) and (pat[i] == txt[j] or pat[i] == '.')

            if i == len(pat) and j == len(txt):
                # Of course, empty txt matches empty pat
                dp[i][j] = True

            elif i + 1 < len(pat) and pat[i+1] == '*':
                # If next pat is '*', skip it or assume it matches more than 1 txt char
                dp[i][j] = dp[i+2][j] or matchCurrrent and dp[i][j+1]

            else:
                # If next pat is not '*' or pat is empty, matches current and move both 1 step
                dp[i][j] = matchCurrrent and dp[i+1][j+1]

    return dp[0][0]


def isMatch(st,si,pt,pi):
    '''
    Old Recursive methd
    st : string, si: string index
    pt : pattern, pi: pattern index
    Notice Python substring is deep copy
    '''
    # if pattern is empty, string must be empty
    if pi >= len(pt): # pi can be larger than len(pt)
        return si == len(st)
    
    # if string is empty, next pattern must be '*'
    if si == len(st):
        return pi+1 < len(pt) and pt[pi+1] == '*' and isMatch(st,si,pt,pi+2)
    
    # if next pattern is not '*' or pattern reached last char
    if pi+1 < len(pt) and pt[pi+1] != '*' or pi + 1 == len(pt):
        return (pt[pi] == '.' or pt[pi] == st[si]) and isMatch(st,si+1,pt,pi+1)
    
    # next pattern is '*': Skip '*' or assume '*' matches more than 1 chars
    return isMatch(st,si,pt,pi+2) or (pt[pi] == '.' or pt[pi] == st[si]) and isMatch(st,si+1,pt,pi)
