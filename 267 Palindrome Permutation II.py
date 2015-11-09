from collections import Counter
'''
267 Palindrome Permutation II
https://leetcode.com/problems/palindrome-permutation-ii/

Notice the algorithm to generate permutation is exponential time
'''
def permutations(input, repeat = None):
    '''
    :type input: List
    :type repeat: Int
    :rtype: Generator[tuple]
    Iteratively compute permutation of input without duplicates
    BFS, O(n!)
    '''
    repeat = len(input) if repeat is None else r
    queue = []
    for i,v in enumerate(input):
        if i > 0 and v == input[i-1]: continue
        queue.append(([v],input[:i]+input[i+1:]))
    for j in xrange(1,repeat):
        newQ = []
        for q in queue:
            prev = q[0]
            src = q[1]
            for i,v in enumerate(src):
                if i > 0 and v == src[i-1]: continue 
                newQ.append((prev + src[i:i+1], src[:i] + src[i+1:]))
        queue = newQ
    for q in queue:
        yield tuple(q[0])
    
def permutations2(counter, pool, sofar):
    '''
    DFS
    '''
    noMore = True
    for k in counter.keys():
        if counter[k] == 0: continue
        counter[k] -= 1
        permutations2(counter, pool, k + sofar)
        counter[k] += 1
        noMore = False
    if noMore: pool.append(sofar)
  
def generatePalindromes(s):
    """
    :type s: str
    :rtype: List[str]
    """
    all = Counter(s)
    oddy = 0
    single = ''
    counter = Counter()
    for k, v in all.iteritems():
        if v % 2 == 1:
            oddy += 1
            single = k
        counter[k] = v // 2
    if oddy > 1: return []        
    pool = []
    permutations2(counter, pool, '')
    return [''.join(p + single + p[::-1]) for p in pool]
    
class Solution(object):
    def generatePalindromes(self, s):
        return generatePalindromes(s)
        
