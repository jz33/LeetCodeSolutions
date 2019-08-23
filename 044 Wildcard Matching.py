'''
44 Wildcard Matching
https://oj.leetcode.com/problems/wildcard-matching/
'?' matches any single char
'*' matches 0 or more any chars
https://leetcode.com/discuss/38645/128ms-o-1-space-python-solution
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
                    # If current pat is '*', either is matches 0 character,
                    # Or let it matches current txt. Notice dp[i][j+2] is True,
                    # dp[i][j] is also True, but it is covered by dp[i][j+1]
                    dp[i][j] = dp[i+1][j] or (j < len(txt) and dp[i][j+1])

                else:
                    # If next pat is not '*' or pat is empty, matches current and move both 1 step
                    dp[i][j] = matchCurrrent and dp[i+1][j+1]

        return dp[0][0]
