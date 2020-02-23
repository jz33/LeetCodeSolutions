'''
616. Add Bold Tag in String
https://leetcode.com/problems/add-bold-tag-in-string/

Given a string s and a list of strings dict, you need to add a closed pair of bold tag <b> and </b> to
wrap the substrings in s that exist in dict. If two such substrings overlap, you need to wrap them together by
only one pair of closed bold tag. Also, if two substrings wrapped by bold tags are consecutive, you need to combine them.

Example 1:

Input: 
s = "abcxyz123"
dict = ["abc","123"]
Output:
"<b>abc</b>xyz<b>123</b>"

Example 2:

Input: 
s = "aaabbcc"
dict = ["aaa","aab","bc"]
Output:
"<b>aaabbc</b>c"
Note:

The given dict won't contain duplicates, and its length won't exceed 100.
All the strings in input have length in range [1, 1000].
'''
class Solution:
    def addBoldTag(self, s: str, d: List[str]) -> str:
        # Get all occurence of each word of d in s
        intervals = []
        for word in d:
            intervals += [[i, i + len(word)] for i in range(len(s)) if s.startswith(word, i)]
            
        if not intervals:
            return s
        
        # Merge intervals
        intervals.sort()
        merged = []
        prev = intervals[0]
        for curr in intervals:
            if curr[0] > prev[1]:
                merged.append(prev)
                prev = curr
            else:
                prev[1] = max(prev[1], curr[1])
        merged.append(prev)
                
        # Insert bold tags
        res = []
        if merged[0][0] > 0:
            res.append(s[:merged[0][0]])
            
        for i, t in enumerate(merged):
            start, end = t
            res.append('<b>')
            res.append(s[start : end])
            res.append('</b>')
            if i + 1 < len(merged):
                res.append(s[end : merged[i+1][0]])
                
        if merged[-1][1] < len(s):
            res.append(s[merged[-1][1]:])
            
        return ''.join(res)
