'''
Top K Frequent Elements 
https://leetcode.com/problems/top-k-frequent-elements/
'''
def topKFrequent(nums, count):
    histo = {}
    maxFreq = 0
    for n in nums:
        freq = histo.get(n,0) + 1
        maxFreq = max(maxFreq,freq)
        histo[n] = freq
        
    rev = {}
    for k,v in histo.iteritems():
        rev[v] = rev.get(v,[]) + [k]
    
    res = []
    while len(res) < count:
        res.extend(rev.get(maxFreq,[]))
        maxFreq -= 1
    return res[:count]
