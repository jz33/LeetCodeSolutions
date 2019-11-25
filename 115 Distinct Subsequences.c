/*
115. Distinct Subsequences
https://leetcode.com/problems/distinct-subsequences/

Given a string S and a string T, count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string by deleting some (can be none)
of the characters without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^
Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
*/
/*
Let's say i is iterator of s, j is iterator of t,
then dp[i][j] = dp[i-1][j] + dp[i-1][j-1] if dp[i] == dp[j] else dp[i-1][j]
*/
int numDistinct(char * s, char * t)
{
    uint64_t i,j, upper, upperLeft;
    uint64_t* row;
    int ls = (int)strlen(s);
    int lt = (int)strlen(t);
    
    if (ls == 0 || lt > ls) return 0;
	if (lt == 0) return 1;
    
    row = (uint64_t*)calloc(lt, sizeof(uint64_t));
    
    for (i = 0; i < ls; i++)
    {
        // upperLeft is at least 1, which means if t is empty, therer is 1 distinct subsequence
        upperLeft = 1u;
        for (j = 0; j < lt; j++)
        {
            upper = row[j];
            row[j] = (s[i] == t[j] ? upperLeft + upper : upper);
            upperLeft = upper;
        }
    }
    i = row[lt-1];
    free(row);
    return (int)i;
}
