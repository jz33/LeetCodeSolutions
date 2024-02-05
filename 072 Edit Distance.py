'''
72. Edit Distance
https://leetcode.com/problems/edit-distance/

Given two strings word1 and word2,
return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

    Insert a character
    Delete a character
    Replace a character

Example 1:

Input: word1 = "horse", word2 = "ros"
Output: 3
Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:

Input: word1 = "intention", word2 = "execution"
Output: 5
Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

Constraints:
    0 <= word1.length, word2.length <= 500
    word1 and word2 consist of lowercase English letters.
'''
class Solution:
    '''
    1-D space
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        if len(word1) > len(word2):
            word1, word2 = word2, word1

        # Initialize dp like each word1 char to empty string
        dp = list(range(len(word1) + 1))

        for i2 in range(len(word2)):
            upperLeft = dp[0]
            dp[0] = i2 + 1
            for i1 in range(len(word1)):
                upper = dp[i1+1]
                left = dp[i1]
                if word2[i2] == word1[i1]:
                    dp[i1+1] = upperLeft
                else:
                    dp[i1+1] = min(upperLeft, upper, left) + 1
                upperLeft = upper
        return dp[-1]
    
class Solution:
    '''
    http://rosettacode.org/wiki/Levenshtein_distance
    '''
    def minDistance(self, word1: str, word2: str) -> int:
        # buf[i][j] means the distance of words2[:i] to words1[:j]
        buf = [[0] * (len(word1)+1) for _ in range(len(word2)+1)]
        
        # Initialize buf.
        # buf[0][0] is 0, of course
        # Distance of empty word to words2[:i] is i
        for i in range(len(word2)):
            buf[i+1][0] = i+1
            
        # Distance of empty word to words1[:j] is j
        for j in range(len(word1)):
            buf[0][j+1] = j+1
        
        for i in range(len(word2)):
            for j in range(len(word1)):
                if word2[i] == word1[j]:
                    buf[i+1][j+1] = buf[i][j]
                else:
                    buf[i+1][j+1] = min(buf[i][j], buf[i][j+1], buf[i+1][j])+1
        
        return buf[len(word2)][len(word1)]
