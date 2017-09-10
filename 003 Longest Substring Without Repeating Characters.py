'''
003 Longest Substring Without Repeating Characters.py
https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
'''
class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) < 2: return len(s)
        lt = 0
        ml = 1 # max length
        ref = {s[0]:0} # char : index
        for i in xrange(1,len(s)):
            c = s[i]
            prev = ref.get(c)
            if prev is None:
                ml = max(ml,i-lt+1)
            else:
                for k in xrange(lt,prev+1):
                    del ref[s[k]]
                lt = prev + 1
            ref[c] = i
        ml = max(ml,len(s)-lt)
        return ml
