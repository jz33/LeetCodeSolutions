'''
49. Group Anagrams
https://leetcode.com/problems/group-anagrams/

Given an array of strings, group anagrams together.

Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output:
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
Note:

All inputs will be in lowercase.
The order of your output does not matter
'''
PRIMES =[2, 3, 5, 7, 11 ,13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 107]

class Solution:
    '''
    Use Prime product, can overflow
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        book = collections.defaultdict(list) # {hash : [strings]}
        for s in strs:
            # Compute hash by multiply chars
            h = 1
            for c in s:
                h *= PRIMES[ord(c) - ord('a')]
            book[h].append(s)
        return book.values()
      
class Solution:
    '''
    Use char histogram
    '''
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        A = ord('a')
        res = collections.defaultdict(list) # {char histogram : [strings]}
        for s in strs:
            histo = [0] * 26
            for c in s:
                histo[ord(c) - A] += 1
            res[tuple(histo)].append(s)
        return res.values()
