from typing import List, Tuple
'''
https://leetcode.com/discuss/interview-question/385870/Google-or-Onsite-or-Word-Break-III
Given a sentence without spaces s and a dictionary dict,
you have to find the way to break the sentence in the minimum number of individual dictionary words.
If there're multiple solutions, return any of them.

Example 1:

Input: s = "bedbathandbeyand", dict = ["bed", "bath", "bat", "and", "hand", "bey", "beyand"]
Output: ["bed", "bath", "and", "beyand"] or ["bed", "bat", "hand", "beyand"]
Example 2:

Input: s = "catsandog", dict = ["cats", "dog", "sand", "and", "cat"]
Output: []
'''
class Solution:
    def wordBreak3(self, word: str, book: List[str]) -> List[List[str]]:
        size = len(word)
        myBook = set(book)
        dp = [[] for _ in range(size+1)]
        dp[0].append([])

        for i in range(1, size+1):
            for j in range(i-1,-1,-1):
                if len(dp[j]) > 0:
                    suffix = word[j:i]
                    if suffix in myBook:
                        if len(dp[i]) == 0 or len(dp[j][0]) + 1 < len(dp[i][0]):
                            # Replace
                            dp[i] = [path + [suffix] for path in dp[j]]
                        elif len(dp[j][0]) + 1 == len(dp[i][0]):
                            # Increase
                            dp[i] += [path + [suffix] for path in dp[j]]

        return dp[-1]


sol = Solution()

word= "bedbathandbeyand"
book = ["bed", "bath", "bat", "and", "hand", "bey", "beyand"]
print(sol.wordBreak3(word, book))
