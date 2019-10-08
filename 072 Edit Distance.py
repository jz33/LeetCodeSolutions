'''
72. Edit Distance

Given two words word1 and word2, find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:

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
'''
class Solution:
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
