import inspect
'''
Group Shifted Strings
https://leetcode.com/problems/group-shifted-strings/
'''
def groupStrings(strings):
    """
    :type strings: List[str]
    :rtype: List[List[str]]
    """
    map = {}
    for s in strings:
        hash = []
        for i in xrange(1,len(s)):
            diff = ord(s[i]) - ord(s[i-1])
            if diff < 0 : diff += 26
            hash.append(diff)
        tup = tuple(hash)
        v = map.get(tup,[])
        v.append(s)
        map[tup] = v
    
    res = []
    for v in map.itervalues():
        res.append(sorted(v))
    return res
     
ls = []
print inspect.getfile(__builtin__)
