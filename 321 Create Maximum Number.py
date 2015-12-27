from json import dumps
'''
321. Create Maximum Number
https://leetcode.com/problems/create-maximum-number/
https://leetcode.com/discuss/75756/share-my-greedy-solution
'''
def maxNumber1(arr, k):
    '''
    Max number for single array
    '''
    if k == 0 : return []
    size = len(arr)
    res = [0] * k
    r = 0
    m = k - size
    for i, e in enumerate(arr):
        # while len(arr) - i - 1 >= k - r - 1 and r >= 0 and e > res[r]
        while r >= max(m + i, 0) and e > res[r]:
            r -= 1
        r += 1
        if r == k: r -= 1
        else : res[r] = e
    return res

def greater(a1, p1, a2, p2):
    '''
    Compare 2 numbers from p1, p2
    '''
    l1 = len(a1)
    l2 = len(a2)
    while p1 < l1 and p2 < l2 and a1[p1] == a2[p2]:
        p1 += 1
        p2 += 1
    return p2 == l2 or p1 < l1 and a1[p1] > a2[p2]

def merge(a1,a2,k):
    '''
    Merge 2 numbers
    Possible optimization in greater compare
    '''
    res = [0] * k
    p1, p2 = 0, 0
    for r in xrange(0,k):
        if greater(a1,p1,a2,p2):
            res[r] = a1[p1]
            p1 += 1
        else:
            res[r] = a2[p2]
            p2 += 1
    return res

def maxNumber(nums1, nums2, k):
    """
    :type nums1: List[int]
    :type nums2: List[int]
    :type k: int
    :rtype: List[int]
    """
    l1 = len(nums1)
    l2 = len(nums2)
    res = [0] * k
    for i in xrange(max(0,k-l2),min(l1,k)+1):
        cand = merge(maxNumber1(nums1,i), maxNumber1(nums2,k-i),k)
        if greater(cand, 0, res, 0): res = cand
    return res
