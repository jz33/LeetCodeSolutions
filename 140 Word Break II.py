'''
40. Word Break II
https://leetcode.com/problems/word-break-ii/

Given a non-empty string s and a dictionary wordDict containing a list of non-empty words,
add spaces in s to construct a sentence where each word is a valid dictionary word.
Return all such possible sentences.

Note:

The same word in the dictionary may be reused multiple times in the segmentation.
You may assume the dictionary does not contain duplicate words.

Example 1:

Input:
s = "catsanddog"
wordDict = ["cat", "cats", "and", "sand", "dog"]
Output:
[
  "cats and dog",
  "cat sand dog"
]

Example 2:

Input:
s = "pineapplepenapple"
wordDict = ["apple", "pen", "applepen", "pine", "pineapple"]
Output:
[
  "pine apple pen apple",
  "pineapple pen apple",
  "pine applepen apple"
]
Explanation: Note that you are allowed to reuse a dictionary word.

Example 3:

Input:
s = "catsandog"
wordDict = ["cats", "dog", "sand", "and", "cat"]
Output:
[]
'''
class Solution:
    '''
    DFS will scope down the problem very quickly
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not wordDict:
            return []
        
        book = set(wordDict)
        maxSize = len(max(wordDict, key = len)) # max size of the word in dict
        solutions = {} # solution cache of s[i:]
        solutions[len(s)] = ['']
        
        def dfs(i: int) -> List[str]:
            sol = []
            if i not in solutions:
                # to make sure s[i:j] in book, then j-i <= maxSize
                for j in range(i+1, min(maxSize+i+1, len(s)+1)):
                    suffix = s[i:j]
                    if suffix in book:
                        for sub in dfs(j):
                            sol.append(suffix + (sub and ' ' + sub))
                solutions[i] = sol              
            else:
                sol = solutions[i]
            return sol
        
        return dfs(0)        

class Solution:
    '''
    This solutin will result "Time Limit Exceeded" for case:
    "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaabaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
["a","aa","aaa","aaaa","aaaaa","aaaaaa","aaaaaaa","aaaaaaaa","aaaaaaaaa","aaaaaaaaaa"]
    Because the solution built-up is exponential
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        if not wordDict:
            return []
        
        size = len(s)
        maxSize = len(max(wordDict, key = len)) # max size of the word in dict
        book = dict(zip(wordDict, range(len(wordDict)))) # {word : index}

        # dp[i] contains all possible paths for s[:i]
        dp = [[] for _ in range(size+1)]
        dp[0].append([])
        
        for i in range(1, size+1):
            # Build dp[i] based on dp[j] + s[j:i]
            # Of course len(s[j:i]) <= maxSize
            for j in range(i-1,max((i-maxSize), 0) - 1,-1):
                if len(dp[j]) > 0:
                    suffix = s[j:i]
                    index = book.get(suffix)
                    if index is not None:
                        dp[i] += [path + [index] for path in dp[j]]

        return [' '.join(wordDict[i] for i in path) for path in dp[-1]]
