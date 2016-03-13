from itertools import izip
'''
336 Palindrome Pairs
https://leetcode.com/problems/palindrome-pairs/
'''
def palindromePairs(words):
    ls = []
    ref = dict(izip(words, xrange(len(words))))
    for i, w in enumerate(words):
        for j in xrange(0,len(w)+1):
            lt = w[:j]
            lr = lt[::-1]
            rt = w[j:]
            rr = rt[::-1]
            if lt == lr:
                k = ref.get(rr,-1)
                if k != -1 and k != i:
                    ls.append((k,i))
            if rt == rr:
                k = ref.get(lr,-1)
                if k != -1 and k != i:
                    ls.append((i,k))
    return list(set(ls))
