from copy import deepcopy
'''
140 Word Break II
https://oj.leetcode.com/problems/word-break-ii/
'''
'''
A recursive approach with prefix check
Passed
'''
def wordBreak(tag, book):
    ret = []
    if tag == '': return ret
    
    # At least 1 suffix is in dict
    i = len(tag) - 1
    while i > -1:
        if tag[i:] in book: break
        i -= 1
            
    # Not found        
    if i == -1:return ret
    
    # Loop each prefix
    i = 0
    while i < len(tag)-1:
        prefix = tag[:i+1]
        if prefix in book:
            suffix = tag[i+1:]
            child = wordBreak(suffix,book)
            for c in child:
                ret.append(prefix + ' ' + c)
        i += 1
        
    if tag in book: ret.append(tag)
    return ret

'''
Debug
'''
def dump(mat):
    for r in mat:
        for c in r:
            print c,
        print
    print
 
'''
A DP approach, O(n^2)
But with intense memory usage, this will not pass
'''
def wordBreakDP(tag,book):
    ret = []
    if tag == '': return ret

    # $buf: [[end Index, word0,word1...]]
    buf = []
    
    # Found first prefix
    for i in xrange(0,len(tag)):
        prefix = tag[:i+1]
        if prefix in book:
            buf.append([i,prefix])
            break
    
    # Not found        
    if len(buf) == 0:return ret

    start = buf[0][0] + 1
    for i in xrange(start,len(tag)):
        # for each previous word break
        buf_len = len(buf)
        for j in xrange(0,buf_len):
            suffix = tag[buf[j][0]+1:i+1]
            if suffix in book:
                # add new entry
                entry = deepcopy(buf[j])
                entry.append(suffix)
                entry[0] = i
                buf.append(entry)
                
        # whole word in dict
        prefix = tag[:i+1]
        if prefix in book:
            buf.append([i,prefix])
        
    for b in buf:
        if b[0] == len(tag)-1:
            ret.append(' '.join(b[1:]))
    
    return ret
    
def main():
    tag = 'aaaaaaa'
    book = set(['aaaa','aaa'])
    
    rec = wordBreak(tag,book)
    print rec
    dps = wordBreakDP(tag,book)
    print dps
      
if __name__ == "__main__":
    main()
