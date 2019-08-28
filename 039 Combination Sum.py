"""
039 Combination Sum
https://leetcode.com/problems/combination-sum/
An iterative DP way
"""
def combinationSum(candidates, target):
    """
    :type candidates: List[int]
    :type target: int
    :rtype: List[List[int]]
    """
    # buf is a 3-D matrix. buf[i] contains all the combination sums to i
    buf = [[] for _ in xrange(target+1)]
    buf[0].append([])
    
    for c in candidates:
        for i in xrange(c,target+1):
            for ls in buf[i-c]:
                buf[i].append(ls + [c])

    return buf[target]
