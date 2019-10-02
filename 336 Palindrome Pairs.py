'''
336. Palindrome Pairs
Given a list of unique words, find all pairs of distinct indices (i, j) in the given list,
so that the concatenation of the two words, i.e. words[i] + words[j] is a palindrome.

Example 1:

Input: ["abcd","dcba","lls","s","sssll"]
Output: [[0,1],[1,0],[3,2],[2,4]] 
Explanation: The palindromes are ["dcbaabcd","abcddcba","slls","llssssll"]

Example 2:

Input: ["bat","tab","cat"]
Output: [[0,1],[1,0]] 
Explanation: The palindromes are ["battab","tabbat"]
'''
class Solution:
    def palindromePairs(self, words: List[str]) -> List[List[int]]:
        res = []
        book = dict(zip(words, range(len(words)))) # word : index

        '''
        For a string: '012345'
        If substring '012' is palindromic, then we need '543' in book
        If substring '' is palindromic (of course), then we need '543210'
        '''
        for i, word in enumerate(words):           
            for j in range(len(word)+1): 
                left = word[:j]
                leftReversed = left[::-1]
                right = word[j:]
                rightReversed = right[::-1]

                if left == leftReversed:
                    k = book.get(rightReversed, -1)
                    if k != -1 and k != i:
                        res.append([k,i])

                # Need len(right) > 0 to avoid duplicats
                # Think case [abcd, dcba]
                if len(right) > 0 and right == rightReversed:
                    k = book.get(leftReversed,-1)
                    if k != -1 and k != i:
                        res.append([i,k])

        return res
