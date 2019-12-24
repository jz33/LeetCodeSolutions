'''
890. Find and Replace Pattern
https://leetcode.com/problems/find-and-replace-pattern/

You have a list of words and a pattern, and you want to know which words in words matches the pattern.

A word matches the pattern if there exists a permutation of letters p so that after
replacing every letter x in the pattern with p(x), we get the desired word.

(Recall that a permutation of letters is a bijection from letters to letters:
every letter maps to another letter, and no two letters map to the same letter.)

Return a list of the words in words that match the given pattern. 

You may return the answer in any order.

Example 1:

Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
Output: ["mee","aqq"]
Explanation: "mee" matches the pattern because there is a permutation {a -> m, b -> e, ...}. 
"ccc" does not match the pattern because {a -> c, b -> c, ...} is not a permutation,
since a and b map to the same letter.
'''
class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        '''
        Same question to 205 Isomorphic Strings
        '''
        result = []
        for word in words:
            proj = {} # projections, patter[i] => word[i]
            used = set() # used word[i]
            
            for i, p in enumerate(pattern):
                if p in proj:
                    if word[i] != proj[p]:
                        break
                else:
                    if word[i] in used:
                        break
                    proj[p] = word[i]
                    used.add(word[i])
            else:
                result.append(word)
                
        return result
