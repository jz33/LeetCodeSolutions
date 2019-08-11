'''
003 Longest Substring Without Repeating Characters.py
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
def lengthOfLongestSubstring(s: str) -> int:
    '''
    Using sliding window method. No need to delete from cache
    '''
    if len(s) < 2:
        return len(s)

    buf = {} # char : index
    left = 0 # the left margin
    res = 0
    for i, e in enumerate(s):
        if e in buf:
            # Simply forward the left margin
            # Notice buf[e] can be less than left
            left = max(left, buf[e] + 1)
        res = max(res, i - left + 1)
        buf[e] = i
    return res
