'''
Word Break II
https://leetcode.com/problems/word-break-ii/
'''
def wordBreakRec(s, src):
    ret = [s] if s in src else []
    # At least 1 suffix is in dict
    for i in xrange(len(s)-1,-1,-1):
        if s[i:] in src: break
    else:     
        return ret # Not found
    
    # Loop each prefix
    for i in xrange(1,len(s)):
        prefix = s[:i]
        if prefix in src:
            tails = wordBreakRec(s[i:],src)
            for t in tails:
                ret.append(prefix + ' ' + t)
    return ret

def wordBreakFromTail(s,src):
    '''
    Best DP approach from tail
    'ref' contains all word breaks in s[k:]
    '''
    ref = {len(s) : ['']}
    for i in xrange(len(s)-1,-1,-1):
        values = []
        for j in xrange(i+1, len(s)+1):
            sub = s[i:j]
            if sub in src:
                for suffix in ref.get(j,[]):
                    if suffix == '':
                        values.append(sub)
                    else:
                        values.append(sub + ' ' + suffix)
        ref[i] = values
    return ref.get(0,[])

def wordBreak2(s,src):
    '''
    A DP approach from head
    'ref' contains all word breaks in s[:k]
    '''
    ref = {0 : ['']}
    for i in xrange(len(s)):
        for j in xrange(i+1, len(s)+1):
            values = ref.get(j,[])
            sub = s[i:j]
            if sub in src:
                for prefix in ref.get(i,[]):
                    if prefix == '':
                        values.append(sub)
                    else:
                        values.append(prefix + ' ' + sub)
            ref[j] = values
    return ref.get(len(s),[])

s = 'catsanddog'
ref = set(["cat", "cats", "and", "sand", "dog"])
r = wordBreakRec(s,ref)
for row in r: print row
