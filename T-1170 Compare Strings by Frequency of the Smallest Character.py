'''
1170. Compare Strings by Frequency of the Smallest Character
https://leetcode.com/problems/compare-strings-by-frequency-of-the-smallest-character/

Let's define a function f(s) over a non-empty string s, which calculates the frequency of the smallest character in s.
For example, if s = "dcce" then f(s) = 2 because the smallest character is "c" and its frequency is 2.

Now, given string arrays queries and words, return an integer array answer,
where each answer[i] is the number of words such that f(queries[i]) < f(W), where W is a word in words.

Example 1:

Input: queries = ["cbd"], words = ["zaaaz"]
Output: [1]
Explanation: On the first query we have f("cbd") = 1, f("zaaaz") = 3 so f("cbd") < f("zaaaz").

Example 2:

Input: queries = ["bbb","cc"], words = ["a","aa","aaa","aaaa"]
Output: [1,2]
Explanation: On the first query only f("bbb") < f("aaaa"). On the second query both f("aaa") and f("aaaa") are both > f("cc").
'''
def lowerBound(arr, target):
    '''
    Return the smallest index of arr whose element is bigger than target
    '''
    left = 0
    right = len(arr)-1
    bound = None
    while left <= right:
        mid = left + ((right-left)>>1)
        if arr[mid] > target:
            bound = mid
            right = mid - 1
        else:
            left = mid + 1
    return bound

class Solution:
    def sf(self, s: str) -> int:
        sc = None # smallest char
        cc = 0 # smallest char count
        for c in s:
            if sc is None or ord(c) < ord(sc):
                sc = c
                cc = 1
            elif c == sc:
                cc += 1
        return cc
        
    def numSmallerByFrequency(self, queries: List[str], words: List[str]) -> List[int]:        
        arr = sorted([self.sf(word) for word in words])
        ans = [0] * len(queries)
        for i, word in enumerate(queries):
            f = self.sf(word)
            b = lowerBound(arr, f)
            if b is not None:
                ans[i] = len(arr) - lowerBound(arr, f)
        return ans
