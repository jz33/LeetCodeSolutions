'''
Word Break II
https://leetcode.com/problems/word-break-ii/
'''
def wordBreakRec(s, src):
    '''
    Accepted
    '''
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

class Solution:
    '''
    Time limit Exceeded
    '''
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        size = len(s)
        book = dict(zip(wordDict, range(len(wordDict)))) # word : index

        # dp[i] contains all possible paths for s[:i]
        dp = [[] for _ in range(size+1)]
        dp[0].append([])
        
        for i in range(1, size+1):
            for j in range(i):
                # Build dp[i] based on dp[j] and s[j:i]
                for path in dp[j]:
                    index = book.get(s[j:i])
                    if index is not None:
                        # Only append index to save time
                        dp[i].append(path + [index])

        res = []
        for path in dp[-1]:
            res.append(' '.join([wordDict[index] for index in path]))
        return res
