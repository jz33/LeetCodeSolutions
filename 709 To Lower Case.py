'''
709. To Lower Case

Give a string, convert to all lowercase.
'''
class Solution:
    def toLowerCase(self, src: str) -> str:
        res = [None] * len(src)
        for i,c in enumerate(src):
            p = ord(c)
            if ord('A') <= p <= ord('Z'):
                res[i] = chr(p + 32) # ord('a') - ord('A') = 32
            else:
                res[i] = c
        return ''.join(res)
