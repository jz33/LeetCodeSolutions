'''
291 Word Pattern II
https://leetcode.com/problems/word-pattern-ii/
'''
maxDepth = -1
def rec(pattern, pi, word, wi, ref, rev, depth = 0):
    global maxDepth
    maxDepth = max(depth,maxDepth)
    depth += 1
    if pi == len(pattern): return wi == len(word)
    if wi == len(word): return False
    
    pc = pattern[pi]
    val = ref.get(pc,'')
    if val == '':
        for i in xrange(wi+1,len(word)+1):
            rv = word[wi:i]
            if rv not in rev:
                ref[pc] = rv
                rev[rv] = True
                if rec(pattern,pi+1,word,i,ref,rev,depth+1) is True:
                    return True
                else:
                    del ref[pc]
                    del rev[rv]
        return False
    else:
        lv = len(val)
        if wi+lv > len(word) or word[wi:wi+lv] != val:
            return False
        else:
            return rec(pattern,pi+1,word,wi+lv,ref,rev,depth+1)

pattern = 'aaaa'
word = 'asdasdasdasd'
ref = {}
rev = {}
print rec(pattern,0,word,0,ref,rev)
print maxDepth            
