map = {}

def rec(pat, str):
    lp = len(pat)
    ls = len(str)
    if lp == 0: return ls == 0
    if lp > ls: return False
    
    first = pat[0]
    if first in map:
        val = map[first]
        lv = len(val)
        if lv > ls or str[:lv] != val: return False
        return rec(pat[1:], str[lv:])
    else:
        if lp == 1:
            return True if ls > 0 and str not in map.values() else False
        for i in xrange(1,ls + 1):
            val = str[:i]
            if val in map.values(): continue
            map[first] = val
            if rec(pat[1:], str[i:]): return True
            del map[first]
        return False
        
class Solution(object):
    def wordPatternMatch(self, pat, str):
        map.clear()
        return rec(pat,str)
