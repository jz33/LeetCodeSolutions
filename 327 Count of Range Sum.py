'''
Count of Range Sum
https://leetcode.com/problems/count-of-range-sum/
Need to handle int overflow to make it pass
'''
def upper_bound(arr,tag):
    i = 0 
    j = len(arr) - 1
    while i < j:
        m = (i + j >> 1)
        if arr[m][0] > tag:
            j = m - 1
        else:
            i = m + 1
    return i if arr[i][0] > tag else i + 1

def lower_bound(arr,tag):
    i = 0
    j = len(arr) - 1
    while i < j:
        m = (i + j >> 1)
        if arr[m][0] < tag:
            i = m + 1
        else:
            j = m - 1
    return i if arr[i][0] >= tag else i + 1

def countRangeSum(nums, lower, upper):
    """
    :type nums: List[int]
    :type lower: int
    :type upper: int
    :rtype: int
    """
    arr = [(0,-1)]
    ac = 0
    for i,e in enumerate(nums):
        ac += e
        arr.append((ac,i))
    arr.sort()

    ctr = 0
    for ac,i in arr:
        lt = lower_bound(arr,ac+lower)
        rt = upper_bound(arr,ac+upper)
        for j in xrange(lt,rt):
            if arr[j][1] < i:
                ctr +=1
    return ctr

nums = [-2,5,-1];print(nums)
lower = -2
upper = 2

print countRangeSum(nums,lower,upper)
